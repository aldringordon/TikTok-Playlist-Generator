import cv2

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
#        writeFrames(image, "frames/image"+str(count)+".jpg")
        saveFrames(image) # append to list
    return hasFrames

sec = 0
frameRate = 0.1 #//it will capture image in each 0.2 second
count=1
success = getFrame(sec)
print("converting mp4 to frames")
while success:
    count = count + 1
    sec = round(sec + frameRate, 2)
    success = getFrame(sec)

print("frames: "+str(len(frames)))
