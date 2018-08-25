import cv2
import os
import numpy as np
import time

def webcam_feed():
    cap = cv2.VideoCapture(0)
    cap.open(0)

"""
    captures 300 images from webcam (please have single face in frame)
"""
    for x in range(300):
        ret, frame = cap.read()
        cv2.imwrite('data/temp/' + str(time.clock()) + '.png', frame)
        cv2.imshow("webcam", frame)

        #break loop early if you press q
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()

if __name__ == "__main__":
    webcam_feed()
