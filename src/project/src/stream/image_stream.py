#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import Header
import cv2
import numpy as np
from flask import Flask, render_template, Response,request
from camera import VideoCamera
from cv_bridge import CvBridge
import struct
import os
import socket



app = Flask(__name__)
stop = False

def shutdown_server():
    print("shut here")
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/')
def index():
    # rendering webpage
    print("/")
    return render_template('index.html')

def gen():
    
        print("gen")
        if stop:
            print("!!!shutdown!!!")
            shutdown_server()
        #get camera frame
        frame = get_frame()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    print("feed")
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

def new_image(data):
    global img,stop
    array = list(data.data)
    img = np.array(array)
    img = img.reshape(data.height,data.width,3)
    rospy.loginfo(np.shape(img))
    if rospy.is_shutdown():
        print("shutdown")
        stop = True

def get_frame():
    ret, jpeg = cv2.imencode('.jpg', img)
    return jpeg.tobytes()


try:
    #rospy.init_node('image_stream')
    #rospy.loginfo("start here")
    #rospy.Subscriber('my_image_raw', Image, new_image)
    #rospy.spin()
    if __name__ == '__main__':
        print("strat flask")
        app.run(host='0.0.0.0',port='5033', debug=False)
    print("A")
except rospy.ROSInterruptException:
        pass
