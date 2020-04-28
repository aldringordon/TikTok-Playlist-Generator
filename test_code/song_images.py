import cv2

vidcap = cv2.VideoCapture('../test_data/test.mp4')
frames = []

def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        frames.append(image)
#        cv2.imwrite("frames/image"+str(count)+".jpg", image)     # save frame as JPG file
    return hasFrames


sec = 0
frameRate = 0.1 #//it will capture image in each 0.2 second
count=1
success = getFrame(sec)
while success:
    count = count + 1
    sec = round(sec + frameRate, 2)
    success = getFrame(sec)

i = 1
while i < len(frames):
    if frames[i] == frames[i-1]:
        frames.pop(i)

count = 1
for image in frames:
    cv2.imwrite("frames/image"+str(count)+".jpg", image)
    count += 1

