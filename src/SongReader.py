# SongReader Class
# Import:
#   Path : String - path to video file
#   Songs: List[(String,String)] - List[(Name, Artist)] - list of songs

import cv2
import numpy as np
import pytesseract as tess
from PIL import Image

class SongReader:

    def __init__(self, path):

        try:
            self.__vidcap = cv2.VideoCapture(path) # Video
        except Exception:
            print("error opening video file")
            self.__vidcap == None

        self.__template = "template.png" # String template image for UI match
        self.__frames = [] # Image
        self.__song_frames = []
        self.__cropped_frames = []
        self.__songs = [] # (str, str)
 
    def __write_templates(self):
        for i in range(len(self.__song_frames)):
            name = "test/matched/match_"+str(i)+".png"
            cv2.imwrite(name, self.__song_frames[i])

    def __write_cropped(self):
        count = 0
        for frame in self.__cropped_frames:
            name = "test/cropped/crop_"+str(count)+".png"
            cv2.imwrite(name, frame)
            count += 1
       
    def get_song_information(self):
        
        print("converting mp4 to frames")
        self.__convert()
        
        print("templating matching")
        self.__match()

        print("printing templates")
        self.__write_templates()

        print("cropping images")
        self.__crop()
    
        print("printing test frames")
        self.__write_cropped()

        print("reading text")
        self.__get_text()
        return self.__songs

    def __save_frames(self, image):
        self.__frames.append(image)

    def __get_frame(self, sec):
        self.__vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
        has_frames, image = self.__vidcap.read()
        if has_frames:
            self.__save_frames(image)
        return has_frames

# convert mp4 to invidiual frames
    def __convert(self):
        sec = 0
        frame_rate = 0.1
        count = 1

        success = self.__get_frame(sec)
        while success:
            count += 1
            sec = round(sec + frame_rate, 2)
            success = self.__get_frame(sec)

# filter out frames that dont match the template UI
    def __match(self):
        template = cv2.imread(self.__template, 0)
        w, h = template.shape[::1]

        for image in self.__frames:
            img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
            thresh = 0.8
            loc = np.where(res >= thresh)

            # check template matches
            if loc[0].size > 0:
                self.__song_frames.append(image)

# crop images around song details
    def __crop(self):
        left = 0
        top = 650
        right = 600
        bottom = 800

        for image in self.__song_frames:
            cropped_image = image[top:bottom, left:right]
            self.__cropped_frames.append(cropped_image)

    def __get_song(self, s):
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

# get text from images
    def __get_text(self):
        for image in self.__cropped_frames:
            text = tess.image_to_string(image)
            song = self.__get_song(text)
            self.__songs.append(song)
