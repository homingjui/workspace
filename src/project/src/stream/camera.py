#camera.py
# import the necessary packages
import cv2
import numpy as np

class VideoCamera(object):
    def __init__(self):
       #capturing video
       self.video = cv2.VideoCapture(0)
    
    def __del__(self):
        #releasing camera
        self.video.release()

def get_frame(self):
        fram = np.zeros((300,400))
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()
