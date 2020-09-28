#!/usr/bin/env python

import rospy
from project.msg import arduino_msg
import socket
import numpy as np
import time

host = "134.208.1.101"
port = 3400

the_time = time.time()

def send(data):
    global the_time,s
    if time.time()-the_time > 1:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((host, port))
            rospy.loginfo(data)
            s.sendall(b'Hello, world')
            s.close()
        except:
            rospy.loginfo("server connect error")
        the_time = time.time()

rospy.init_node('tcp_sender')
rospy.Subscriber('arduino', arduino_msg, send)
rospy.spin()

rospy.loginfo("tcp close")
s.close()
