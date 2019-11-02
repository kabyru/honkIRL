"""
honkIRL, an extension to Untitled Goose Game that allows you to control the honks of the goose with your actual mouth. No honk sounds necessary but are encouraged.
Created on 11/2/2019.
Written by Kaleb Byrum, from Louisville with <3
"""

import os

#os.system("pip3 install opencv-python")
#os.system("pip3 install imutils")
#os.system("pip3 install dlib")

#import necessary packages
from imutils.video import VideoStream
from imutils import face_utils
import datetime
import argparse
import imutils
import time
import dlib
import cv2
import keystrokeHandler

font = cv2.FONT_HERSHEY_SIMPLEX

#Parse the input arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-r", "--picamera", type=int, default=-1, help = "Which camera should be used")
# args = vars(ap.parse_args())

#Shape Predictor should be the path to dlibs pre-trained facial landmark predictor...

#Initialize dlib's HOG-based face detector and load facial predictor
print("Loading facial landmark predictor...")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

#Initialize VideoStream
print("Initializing camera stream...")
vs = VideoStream().start()

resetMessage = ""
resetFlag = False
spacePressed = False
mouthThreshold = 20

#Loop over frames within video stream
while True:
    time.sleep(0.1)
    frame = vs.read()
    frame = imutils.resize(frame, width=800)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.putText(frame, "q to quit program, r to reset closed mouth position", (50,50), font, 0.5, (255,0,0), 1, cv2.LINE_AA)

    if (resetFlag == True):
        cv2.putText(frame, resetMessage, (50,70), font, 0.5, (0,0,255), 1, cv2.LINE_AA)

    rects = detector(gray, 0)
    #Loop over face detections
    for rect in rects:
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape) #REAL-TIME NUMPY ARRAY OF DECTECTED COORDS
        #print(shape)

        #loop over x,y coords and draw on image

        if "closedMouth" not in locals():
            closedMouth = shape[57,1]
            print("Closed Mouth position initialized as " + str(closedMouth))

        dotCount = 0
        for (x, y) in shape: #add text to each circle
            cv2.circle(frame, (x, y), 1, (0, 0, 255), -1)
            cv2.putText(frame, str(dotCount), (x, y), font, 0.5, (0,255,0), 2, cv2.LINE_AA)
            dotCount += 1
    cv2.imshow("Frame", frame)

    print(shape[57])

    key = cv2.waitKey(1) & 0xFF

    #time.sleep(1)

    #Q will exit program
    if key == ord("q"):
        break

    if key == ord("r"):
        closedMouth = shape[57,1]
        resetMessage = "Closed mouth position has been reset to " + str(closedMouth)
        print(resetMessage)
        resetFlag = True
        spacePressed == False
        keystrokeHandler.SpaceBarRelease()
        #cv2.putText(frame, "Closed mouth position has been reset", (400,400), font, 1, (0,0,0), 1, cv2.LINE_AA)

    if ((shape[57,1] >= closedMouth + 20) and (spacePressed == False)):
        spacePressed = True
        keystrokeHandler.SpaceBar()
    
    if ((shape[57,1] <= closedMouth + 20) and (spacePressed == True)):
        spacePressed = False
        keystrokeHandler.SpaceBarRelease()


#Cleanup and destroy windows
cv2.destroyAllWindows
vs.stop()