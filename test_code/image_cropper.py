# take all the image files from the template matched folder
# crop each image so that it only has the song name-artist
# write each image

# Reference: https://www.geeksforgeeks.org/python-pil-image-crop-method/

# Python Image Library's Image Class
from PIL import Image

# Opens RGB Image
im = Image.open("crop/test.jpg")

# Points for Cropped Image
left = 0
top = 650
right = 600
bottom = 800

# Crop Image
cr = im.crop((left, top, right, bottom))

cr.show()
