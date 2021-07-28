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

arduino = arduino_msg()
'''def publish_temp(timer_event):
    temp_msg = Temperature()
    temp_msg.header.frame_id = IMU_FRAME
    temp_msg.temperature = read_word_2c(TEMP_H)/340.0 + 36.53
    temp_msg.header.stamp = rospy.Time.now()
    temp_pub.publish(temp_msg)'''


def publish_imu(timer_event):
    imu_msg = Imu()
    imu_msg.header.frame_id = IMU_FRAME

    # Read the acceleration vals
    accel_x = arduino.accX /32768.0*16.0
    accel_y = arduino.accY /32768.0*16.0
    accel_z = arduino.accZ /32768.0*16.0
    
    # Calculate a quaternion representing the orientation
    '''accel = accel_x, accel_y, accel_z
    ref = np.array([0, 0, 1])
    acceln = accel / np.linalg.norm(accel)
    axis = np.cross(acceln, ref)
    angle = np.arccos(np.dot(acceln, ref))
    orientation = quaternion_about_axis(angle, axis)'''

    # Read the gyro vals
    gyro_x = arduino.gyroX/32768 *2000 *pi/180
    gyro_y = arduino.gyroY/32768 *2000 *pi/180
    gyro_z = arduino.gyroZ/32768 *2000 *pi/180
    
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

    rospy.Subscriber('arduino', arduino_msg , get_data)
    rospy.init_node('imu_node')


    IMU_FRAME = rospy.get_param('~imu_frame', 'imu_link')

    #temp_pub = rospy.Publisher('temperature', Temperature)
    imu_pub = rospy.Publisher('imu/data', Imu)
    imu_timer = rospy.Timer(rospy.Duration(0.02), publish_imu)
    #temp_timer = rospy.Timer(rospy.Duration(10), publish_temp)
    rospy.spin()
