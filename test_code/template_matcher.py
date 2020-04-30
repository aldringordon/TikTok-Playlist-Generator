# Template Matching - OpenCV with Python for Image and Video Analysis 11 - @sentdex

import cv2
import numpy as np

#img_bgr = cv2.imread("../test_data/test5.png")
img_bgr = cv2.imread("frames/image87.jpg")

img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

template = cv2.imread("../test_data/templates/template2.png", 0)
w, h = template.shape[::1]

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
thresh = 0.8
loc = np.where(res >= thresh)

print(loc)
print()
print(loc[0].size)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_bgr, pt, (pt[0]+w, pt[1]+h), (0,255,0), 2)



cv2.imwrite("detected.png", img_bgr)
