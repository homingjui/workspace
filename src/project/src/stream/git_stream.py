#!/usr/bin/env python3
import rospy
import cv2
from threading import Thread, Event
from flask import Flask, render_template, Response
import signal, sys
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import numpy as np
from tf2_msgs.msg import TFMessage
from scipy.spatial.transform import Rotation
import time
from PIL import Image as PIL_image
import simplejpeg

frame = None
bridge = CvBridge()
event = Event()
show_img = 'slam'

def update_pos(data):
    global now_x,now_y,xyz,tf_str
    tf = data.transforms[0]
    now_x = tf.transform.translation.x
    now_y = tf.transform.translation.y
    tfx = tf.transform.rotation.x
    tfy = tf.transform.rotation.y
    tfz = tf.transform.rotation.z
    tfw = tf.transform.rotation.w
    #rospy.loginfo(tf)
    rot = Rotation.from_quat([tfx, tfy, tfz, tfw])
    xyz = rot.as_euler('xyz')
    #rospy.loginfo(xyz)
    tf_str = str(now_x)+","+str(now_y)+","+str(xyz)

def yolo_image(data):
    global fram
    if show_img == 'yolo':
        img = np.ndarray(buffer=data.data,dtype=np.uint8,shape=(data.height,data.width,3))
        fram = simplejpeg.encode_jpeg(img)
        event.set()

def getRGBD(data):
    global RGBD
    
    depth_img = np.frombuffer(data.data, dtype=np.uint8).reshape(data.height, data.width, -1)
    depth = np.zeros((data.height, data.width), dtype=np.float32)
    depth[:,:] = depth_img[:,:,1]
    depth *= 255
    depth += depth_img[:,:,0]
    depth /= depth.max()
    depth *= 255
    depth = depth.astype(np.uint8) 
    depth=cv2.cvtColor(depth, cv2.COLOR_GRAY2RGB)
    RGBD = simplejpeg.encode_jpeg(depth)
    event.set()

def on_image(data):
    global fram
    img = np.ndarray(buffer=data.data,dtype=np.uint8,shape=(data.height,data.width,3))
    fram = simplejpeg.encode_jpeg(img)
    event.set()

def getRGB(data):
    global RGB
    img = np.ndarray(buffer=data.data,dtype=np.uint8,shape=(data.height,data.width,3))
    RGB = simplejpeg.encode_jpeg(img)
    event.set()

Thread(target=lambda: rospy.init_node('image_stream', disable_signals=True)).start()
rospy.Subscriber('/camera/color/image_raw',Image,getRGB)
rospy.Subscriber('/camera/aligned_depth_to_color/image_raw',Image,getRGBD)
rospy.Subscriber("/my_image_raw",Image, on_image)
#rospy.Subscriber("/yolo_image_raw",Image, yolo_image)
#rospy.Subscriber('/tf',TFMessage,update_pos)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/slam')
def index_slam():
    global show_img
    show_img = 'slam'
    return render_template('index.html')


def gen(t='slam'):
    while True:
        if t=='slam' and  'fram'in globals():
            event.wait()
            event.clear()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + fram + b'\r\n')
        elif t=='rgb' and 'RGB'in globals():
            event.wait()
            event.clear()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + RGB + b'\r\n')
        elif t=='rgbd' and 'RGBD'in globals():
            event.wait()
            event.clear()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + RGBD + b'\r\n')



        else:
            img = np.zeros((500,500,3),dtype=np.uint8)
            cv2.putText(img, 'no img QQ', (50, 300), cv2.FONT_HERSHEY_PLAIN,
                      5, (0, 255, 255), 5, cv2.LINE_AA)
            framx = simplejpeg.encode_jpeg(img)
            yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + framx + b'\r\n')
            

@app.route('/camera_depth')
def rgbd_graph():
        return Response(gen('rgbd'),
                        mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/slam_graph')
def slam_graph():
        return Response(gen('slam'),
                        mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/camera')
def camera():
        return Response(gen('rgb'),
                        mimetype='multipart/x-mixed-replace; boundary=frame')


def signal_handler(signal, frame):
    rospy.signal_shutdown("end")
    sys.exit(0)

signal.signal(signal.SIGINT,signal_handler)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3400 ,debug=False)
