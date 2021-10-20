import cv2
import time


def get_frame():
    capture = cv2.VideoCapture(0)
    time.sleep(1)
    response, image = capture.read()
    if response:
        cv2.imwrite("images/test.jpg", image)
    capture.release()
    return image