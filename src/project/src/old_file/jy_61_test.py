#!/usr/bin/env python3

from project.msg import arduino_msg

import time
import smbus2
import struct
import rospy
import numpy as np
from math import pi
from sensor_msgs.msg import Temperature, Imu
#from tf.transformations import quaternion_about_axis

accel_x,accel_y,accel_z=0,0,1
gyro_x,gyro_y,gyro_z = 0,0,0


'''def publish_temp(timer_event):
    temp_msg = Temperature()
    temp_msg.header.frame_id = IMU_FRAME
    temp_msg.temperature = read_word_2c(TEMP_H)/340.0 + 36.53
    temp_msg.header.stamp = rospy.Time.now()
    temp_pub.publish(temp_msg)'''
def get_data(what):
    #arduino = what.arduino_msg()
    #print(arduino)
    # Read the acceleration vals
    global accel_x, accel_y,accel_z
    accel_x = what.accX /32768.0*16.0
    if(accel_x >= 16):
        accel_x -= 2*16.0
    accel_y = what.accY /32768.0*16.0
    if(accel_y >= 16):
        accel_y -= 2*16.0
    accel_z = what.accZ /32768.0*16.0
    if(accel_z >= 16):
        accel_z -= 2*16.0
    print(accel_x,accel_y,accel_z)


    # Read the gyro vals
    global gyro_x,gyro_y,gyro_z
    gyro_x = what.gyroX/32768.0 *2000 *pi/180.0
    if(gyro_x >= 2000):
        gyro_x -= 2*2000
    gyro_y = what.gyroY/32768.0 *2000 *pi/180.0
    if(gyro_y >= 2000):
        gyro_y -= 2*2000
    gyro_z = what.gyroZ/32768.0 *2000 *pi/180.0
    if(gyro_z >= 2000):
        gyro_z -= 2*2000
    #print(arduino.accX)

def publish_imu(timer_event):
    imu_msg = Imu()
    imu_msg.header.frame_id = IMU_FRAME

    # Calculate a quaternion representing the orientation
    '''accel = accel_x, accel_y, accel_z
    ref = np.array([0, 0, 1])
    acceln = accel / np.linalg.norm(accel)
    axis = np.cross(acceln, ref)
    angle = np.arccos(np.dot(acceln, ref))
    orientation = quaternion_about_axis(angle, axis)'''
    global accel_x, accel_y,accel_z
    global gyro_x,gyro_y,gyro_z

    
    # Load up the IMU message
    #o = imu_msg.orientation
    #o.x, o.y, o.z, o.w = orientation

    imu_msg.linear_acceleration.x = accel_x
    imu_msg.linear_acceleration.y = accel_y
    imu_msg.linear_acceleration.z = accel_z

    imu_msg.angular_velocity.x = gyro_x
    imu_msg.angular_velocity.y = gyro_y
    imu_msg.angular_velocity.z = gyro_z

    imu_msg.header.stamp = rospy.Time.now()

    imu_pub.publish(imu_msg)
    

temp_pub = None
imu_pub = None

if __name__ == '__main__':
    rospy.init_node('imu_node')
    rospy.Subscriber('arduino', arduino_msg , get_data)
    



    IMU_FRAME = rospy.get_param('~imu_frame', 'imu_link')

    #temp_pub = rospy.Publisher('temperature', Temperature)
    imu_pub = rospy.Publisher('imu/data', Imu)
    imu_timer = rospy.Timer(rospy.Duration(0.02), publish_imu)
    #temp_timer = rospy.Timer(rospy.Duration(10), publish_temp)
    rospy.spin()
