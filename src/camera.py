import cv2
import time


def get_frame():
    capture = cv2.VideoCapture(0)
    time.sleep(1)
    response, image = capture.read()
    if response:
        cv2.imwrite("images/test.png", image)
    capture.release()
    return image

def crop_face():
    image = face_recognition.load_image_file("images/test.png")
    face_locations = face_recognition.face_locations(image)
    top, right, bottom, left = face_locations[0]
    area = img.crop((left,top,right,bottom))