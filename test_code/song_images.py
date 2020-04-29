import cv2

# for image compare
import numpy as np
from skimage.measure import compare_ssim as ssim

# ImageCompare: returns true if 2 images are the same
# uses: cv2, numpy, sckit

# references:
# https://gist.github.com/gonzalo123/df3e43477f8627ecd1494d138eae03ae
# https://www.pyimagesearch.com/2017/06/19/image-difference-with-opencv-and-python/
####################################################################################

#note: the two images must have the same dimension
def mse(imageA, imageB):
    error = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    error /= float(imageA.shape[0] * imageA.shape[1])
    return error

def diff_remove_bg(img0, img1, im2):
    d1 = diff(img0, img1)
    d2 = diff(img1, img2)
    return sv2.bitwise_and(d1, d2)

def writeDiff(x1, x2, frame):
    x1 = cv2.cvtColor(x1, cv2.COLOR_BGR2GRAY)
    x2 = cv2.cvtColor(x2, cv2.COLOR_BGR2GRAY)

    absdiff = cv2.absdiff(x1, x2)
    cv2.imwrite("diff/diff_"+str(frame)+".png", absdiff)

def writeSame(x1, x2, frame):
    x1 = cv2.cvtColor(x1, cv2.COLOR_BGR2GRAY)
    x2 = cv2.cvtColor(x2, cv2.COLOR_BGR2GRAY)

    absdiff = cv2.absdiff(x1, x2)
    cv2.imwrite("same/same_"+str(frame)+".png", absdiff)


def checkFrames(x1, x2, frame):
    x1 = cv2.cvtColor(x1, cv2.COLOR_BGR2GRAY)
    x2 = cv2.cvtColor(x2, cv2.COLOR_BGR2GRAY)

    m = mse(x1, x2) # mse
    s = ssim(x1, x2) # ssim
  
    print(str(frame) + " - (mse, ssim) -> ("+str(m)+", "+str(s)+")")
    return m

# Gets frames of song
# uses: cv2, ImageCompare
####################################################################################

vidcap = cv2.VideoCapture('../test_data/test.mp4')
frames = []

# save frames as JPG
def writeFrames(image, path):
    cv2.imwrite(path, image)

def saveFrames(image):
    frames.append(image)

def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        writeFrames(image, "frames/image"+str(count)+".jpg")
        saveFrames(image) # append to list
    return hasFrames

print(len(frames))

sec = 0
frameRate = 0.1 #//it will capture image in each 0.2 second
count=1
success = getFrame(sec)
while success:
    count = count + 1
    sec = round(sec + frameRate, 2)
    success = getFrame(sec)

songs = []

for i in range(1, len(frames)):
    if checkFrames(frames[i-1], frames[i], i) > 1000.0:
        writeDiff(frames[i-1], frames[i], i)
    else:
        writeSame(frames[i-1], frames[i], i)
        songs.append(frames[i])

print("same frames: "+str(len(frame)))
