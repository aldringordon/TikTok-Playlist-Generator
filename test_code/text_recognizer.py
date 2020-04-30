import os
import pytesseract as tess
from PIL import Image

# returns (str,str) : (name,artist)
def getSong(s):
    name = ""
    artist = ""

    i = 0
    while not s[i] == "\n":
        name += s[i]
        i += 1

    for x in range(i,len(s)):
        if not s[x] == "\n":
            artist += s[x]

    return name, artist

directory = "crop/"
import_folder = "cropped/"

path = directory+import_folder

files = []
# r=root, d=directories, f=files
for r, d, f in os.walk(path):
    for file in f:
        if ".jpg" in file:
            files.append(os.path.join(r, file))

songs = []
for f in files:
    img = Image.open(f)
    text = tess.image_to_string(img)
    song = getSong(text)
    songs.append(song)
    print("-------------------------")
    print("test image: " + f + ":")
    print("\tName: "+song[0])
    print("\tArtist: "+song[1])
