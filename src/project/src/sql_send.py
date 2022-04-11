#!/usr/bin/env python3
import rospy
import mysql.connector
from mysql.connector import Error
from project.msg import gps_msg
from std_msgs.msg import UInt32


setting=[False,False]

def update_gps(data):
    global lat,lng
    lat = data.latitude
    lng = data.longitude
    if lat != 0:
        setting[0]=True

def update_arduino(data):
    global voltage,speed
    setting[1]=True
    voltage = int(data.data/10000)
    speed = data.data%10000

rospy.init_node('sql_send')
rospy.Subscriber('/gps',gps_msg,update_gps)
rospy.Subscriber('/arduino_send',UInt32,update_arduino)
r = rospy.Rate(0.1)

while not rospy.is_shutdown():
    if all(setting):
        try:
            connection = mysql.connector.connect(
                host='134.208.2.168',
                database='pcdm3401',
                user='pcdm3401',
                password='pcdm3401isp')

            if connection.is_connected():
                print(lat,lng,voltage,speed)
                db_Info = connection.get_server_info()
                #print("version:",db_Info)

                cursor = connection.cursor()
                send_str = "INSERT INTO car2 (lat,lng,power,water,speed) values(%s, %s, %s, %s, %s)"
                new_data = (lat, lng, voltage, 0, speed)
                cursor.execute(send_str, new_data)
                connection.commit()
                r.sleep()
                #cursor.execute("SELECT * FROM car2;")
                #record = cursor.fetchone()
                #print("data:", record)

        except Error as e:
            print("error", e)
    else:
        rospy.loginfo("wait data")
        r.sleep()

if (connection.is_connected()):
    cursor.close()
    connection.close()
    print("closed")
