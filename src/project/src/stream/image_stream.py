#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import Header
import cv2
import numpy as np
from flask import Flask, render_template, Response
from camera import VideoCamera
from cv_bridge import CvBridge
import struct

app = Flask(__name__)

@app.route('/')
def index():
    # rendering webpage
    return render_template('index.html')
def gen():
    
    #get camera frame
    frame = get_frame()
    yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


def new_image(data):
    global img
    array = list(data.data)
    img = np.array(array)
    img = img.reshape(data.height,data.width,3)
    rospy.loginfo(np.shape(img))

def get_frame():
    ret, jpeg = cv2.imencode('.jpg', img)
    return jpeg.tobytes()


try:
    rospy.init_node('image_stream')
    rospy.Subscriber('my_image_raw', Image, new_image)
    app.run(host='0.0.0.0',port='5002', debug=True)
except rospy.ROSInterruptException:
        pass
