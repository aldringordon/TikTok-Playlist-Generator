# take all the image files from the template matched folder
# crop each image so that it only has the song name-artist
# write each image

# References:
    # https://www.geeksforgeeks.org/python-pil-image-crop-method/
    # https://mkyong.com/python/python-how-to-list-all-files-in-a-directory/

import os

import cv2
import numpy as np

# Python Image Library's Image Class
from PIL import Image

directory = "crop/"
import_folder = "to_crop/"
export_folder = "cropped/"

path = directory+import_folder

files = []
# r=root, d=directories, f=files
for r, d, f in os.walk(path):
    for file in f:
        if ".jpg" in file:
            files.append(os.path.join(r, file))

for f in files:
    # Opens RGB Image
    im = Image.open(f)

    # Points for Cropped Image
    left = 0
    top = 650
    right = 600
    bottom = 800

    # Crop Image
    cr = im.crop((left, top, right, bottom))

    #cr.show()
    cr.save(f.replace(import_folder, export_folder))


# opencv implementation
export_folder = "cv/"

for f in files:
    im = cv2.imread(f)

    # [y:y+h, x:x+w]
    cr = im[650:800, 0:600]

    cv2.imwrite(f.replace(import_folder, export_folder), cr)
