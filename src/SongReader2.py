# SongReader Class

import cv2
import numpy as np
import pytesseract as tess

class SongReader(object):
    
    def __init__(self, path):
        
        try:
            self._vidcap = cv2.VideoCapture(path)
        except Exception:
            print("error opening file")
            self._vidcap = None

        self._songs = set() # avoid duplicates of song names

        # for conversion
        self._frame_rate = 0.2

        # for template match
        self._template = "template.png"

    def convert(self):
        sec = 0
        count = 1
        print("converting frame")
        
        self._vidcap.set(cv2.CAP_PROP_POS_MSEC, sec*1000)
        has_frames, image = self._vidcap.read()
        while has_frames:
            
            # check frame matches template
            if self._match(image):
                print("    %i image matched" % count)
                count += 1

                # crop
                image_info = self._crop(image)

                # read song information in image
                self._read(image_info)

            sec = round(sec + self._frame_rate, 2)
            has_frames, image = self._vidcap.read()

    def get_song_information(self):
        return self._songs

    # matches an image to the template image
    def _match(self, image):
        template = cv2.imread(self._template, 0)
        w, h = template.shape[::1]
        
        img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        thresh = 0.8
        loc = np.where(res >= thresh)

        print("  matching image")

        if loc[0].size > 0:
            return True
        return False

    # crops an image around the song information
    def _crop(self, image):
        # problematic
        left = 0
        top = 650
        right = 600
        bottom = 800
        return image[top:bottom, left:right]

    # reads the text in the image (MUST BE CROPPED)
    # adds text to Songs{}
    def _read(self, image):

        print("        adding song")
        text = tess.image_to_string(image)
        song = self._get_song(text)
        self._songs.add(song)


    # takes read string and converts into (name, artist)
    def _get_song(self, s):
        name = ""
        artist = ""

        i = 0
        while not s[i] == "\n":
            name += s[i]
            i += 1

        for x in range(i, len(s)):
            if not s[x] == "\n":
                artist += s[x]

        return name, artist 
