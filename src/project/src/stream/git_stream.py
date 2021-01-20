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

frame = None
bridge = CvBridge()
event = Event()

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


def on_image(data):
    global frame
    array = list(data.data)
    img = np.array(array,np.float32)
    img = img.reshape(data.height,data.width,3)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #rospy.loginfo(np.shape(img))
    frame = cv2.imencode(".jpg",img)[1].tobytes()
    event.set()

Thread(target=lambda: rospy.init_node('image_stream', disable_signals=True)).start()
rospy.Subscriber("/my_image_raw",Image, on_image)
rospy.Subscriber('/tf',TFMessage,update_pos)

app = Flask(__name__)

def get_frame():
    event.wait()
    event.clear()
    return frame

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/tf')
def send():
    rospy.loginfo(tf_str)
    return tf_str

def gen():
    while True:
        frame = get_frame()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

def signal_handler(signal, frame):
    rospy.signal_shutdown("end")
    sys.exit(0)

signal.signal(signal.SIGINT,signal_handler)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080 ,debug=False)
