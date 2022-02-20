#!/usr/bin/env python

import math
import rospy
import time
import tf
from sensor_msgs.msg import Imu
from scipy.spatial.transform import Rotation


def callback(data):
    tfx = data.orientation.x
    tfy = data.orientation.y
    tfz = data.orientation.z
    tfw = data.orientation.w
    rot = Rotation.from_quat([tfx, tfy, tfz, tfw])
    xyz = rot.as_euler('xyz')
    xyz = (xyz/math.pi)*180
    data.orientation.x=xyz[0]
    data.orientation.y=xyz[1]
    data.orientation.z=xyz[2]
    data.orientation.w=1
    #print(xyz)
    pub.publish(data)
rospy.init_node('listener', anonymous=True)
rospy.Subscriber("/imu", Imu, callback)
pub = rospy.Publisher('/myimu', Imu, queue_size=10)
rospy.spin()
