import cv2
import mediapipe as mp

import numpy as np

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands( )
mpDraw = mp.solutions.drawing_utils



while True:
    success, img = cap.read( )
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)




    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break