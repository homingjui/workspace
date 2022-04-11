#!/usr/bin/env python3

import rospy
from project.msg import arduino_msg
import socket
import numpy as np
import time
from datetime import datetime
from tf2_msgs.msg import TFMessage
from scipy.spatial.transform import Rotation
from sensor_msgs.msg import Imu
import json


tf=0

def update_tf(data):
    global tf
    tf = data

def update_gps(data):


def update_imu(data):


def update_arduino(data):


host = "192.168.8.101"
port = 3401

rospy.init_node('tcp_sender')
rospy.Subscriber('/tf',TFMessage,update_pos)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(10)
conn, addr = server.accept()

#rospy.Subscriber('/camera/accel/sample',IMU,update_)
rate = rospy.Rate(1)
while not rospy.is_shutdown():
    
    rospy.loginfo(xyz)
    now = datetime.now()

    sending_format = {
        "messageType": "normal",
        "CarID": 0,
        "Location": "12.12345, 123.45678",
        "speed": 0,
        "power": 0,
        "water": 0,
        "direction":{
            "x_angle":tf.pitch,
            "x_gyro":tf.gyroX,
            "x_acc":tf.accX,
            "y_angle":tf.yaw,
            "y_gyro":tf.gyroY,
            "y_acc":tf.accY,
            "z_angle":tf.roll,
            "z_gyro":tf.gyroZ,
            "z_acc":tf.accZ,
        },
        "time": now.strftime("%m/%d/%Y, %H:%M:%S"),
    }
    rospy.loginfo(sending_format)
    data = json.dumps(sending_format)
    conn.sendall(data.encode('utf-8')) 
    rate.sleep()

rospy.loginfo("tcp close")
conn.close()
server.close()
