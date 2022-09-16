# iam using python version Python 3.10.7
# install module opencv python3 -m pip install -U opencv-contrib-python
# install module Pillow python3 -m pip install -U Pillow
# sourcode face detection https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml

import cv2
camera = cv2.VideoCapture(0)
# setting width and height camera
camera.set(3, 640)
camera.set(4, 480)

faceDecetor = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
  retV, frame = camera.read()
  greyColor = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  
  faceDetection = faceDecetor.detectMultiScale(frame, 1.3, 5) #(frame, scale factor, minNightFirst)

  for (x, y, w, h) in faceDetection:
    frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    greyColor = cv2.rectangle(greyColor,(x,y),(x+w,y+h),(255,0,0),2)

  # showing frame
  cv2.imshow('Frame 1', frame)
  cv2.imshow('Frame 2', greyColor)
  
  pressKeyBoard =  cv2.waitKey(1) & 0xFF
  # when keyboard press button esc or q
  if pressKeyBoard == 27 or pressKeyBoard == ord('q'): 
    break

camera.release()
cv2.destroyAllWindows()