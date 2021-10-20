import numpy as np
import cv2
import sys


def get_frame():
    capture = cv2.VideoCapture(0)
    time.sleep(1)
    response, image = capture.read()
    if response:
        cv2.imwrite("images/test.jpg", image)
    capture.release()