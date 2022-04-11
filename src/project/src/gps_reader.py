#!/usr/bin/python

import rospy
from project.msg import gps_msg
import serial
import numpy as np

COM_PORT = '/dev/ttyACM0'
BAUD_RATES = 9600
ser = serial.Serial(COM_PORT, BAUD_RATES)

pub = rospy.Publisher('gps', gps_msg, queue_size=10)
rospy.init_node('gps_reader')
try:
    while not rospy.is_shutdown():
        gps = gps_msg()
        while ser.in_waiting:
            data = ser.readline()
            status = data.split(",")[0]
            rospy.loginfo(data)
            gps.latitude=0
            gps.longitude=0
            gps.fix_code=0
            if not status == "$GNGGA":
                #pub.publish(gps)
                continue
            if not data.split(",")[2]:
                pub.publish(gps)
                rospy.loginfo("no gps data")
                continue
            
            latitudedm = data.split(",")[2]
            longitudedm = data.split(",")[4]

            #latitudedm = "2353.92083"
            #longitudedm = "12132.60397"
            
            fix_code = int(data.split(",")[6])
            #rospy.loginfo(np.float64(latitudedm[0:2])+np.float64(latitudedm[2:])/60)
            latitude = np.float64(latitudedm[0:2])+np.float64(latitudedm[2:])/60
            longitude = np.float64(longitudedm[0:3])+np.float64(longitudedm[3:])/60
            
            gps.latitude=latitude
            gps.longitude=longitude
            gps.fix_code=fix_code
            pub.publish(gps)
            rospy.loginfo(gps)

except rospy.ROSInterruptException:
    ser.close()
