#!/usr/bin/env python3

import rospy
from project.msg import deg_msg,motor_msg
from nav_msgs.msg import OccupancyGrid
from sensor_msgs.msg import Image,LaserScan
from std_msgs.msg import Header
from tf2_msgs.msg import TFMessage
import cv2
import numpy as np
import math
from scipy.spatial.transform import Rotation




#rout = np.array([[0,0],[0,0.7],[1.1,0.7],[1.1,0]])
rout = np.array([[0,0],[0,5],[-0.5,5],[-0.5,0]], dtype='f')

for i in range(1,len(rout)):
    rout[i]=[rout[i,0]*np.cos(np.pi/2)-rout[i,1]*np.sin(np.pi/2),
             rout[i,0]*np.sin(np.pi/2)+rout[i,1]*np.cos(np.pi/2)]

setup=np.array([False,False,False])

def get_deg(vac1,vac2):
    #Lx=np.sqrt(vac1.dot(vac1))
    #Ly=np.sqrt(vac2.dot(vac2))        
    norm = np.linalg.norm(vac1)*np.linalg.norm(vac2)
    rho = np.arcsin(np.cross(vac1,vac2)/norm)
    cos_ang= vac1.dot(vac2) / norm
    #rospy.loginfo(math.atan2(vac2[0]-vac1[0], vac2[1]-vac1[1]))
    ang=np.arccos(cos_ang)
    if rho>0:
        return -ang
    #rospy.loginfo(ang)
    return ang

def publish_image(imgdata):
    image_temp=Image()
    header = Header(stamp=rospy.Time.now())
    header.frame_id = 'map'
    image_temp.height=np.shape(imgdata)[0]
    image_temp.width=np.shape(imgdata)[1]
    image_temp.encoding='rgb8'
    image_temp.data=np.array(imgdata).tostring()
    #print(imgdata)
    #image_temp.is_bigendian=True
    image_temp.header=header
    image_temp.step=np.shape(imgdata)[1]*3
    img_pub.publish(image_temp)

now_x,now_y=0,0
def update_pos(data):
    global now_x,now_y,xyz,last_x,last_y
    setup[0]=True
    last_x,last_y=now_x,now_y
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
    #draw()

def update_map(data):
    global slam_map,w,h,res,map_pos
    setup[1]=True
    slam_map = np.array(data.data).reshape(data.info.height, data.info.width, -1)
    w = data.info.width
    h = data.info.height
    res = data.info.resolution
    map_pos = data.info.origin.position

def update_scan(data):
    global len_per_ndeg,angle_min,angle_n,len_deg
    setup[2]=True
    header = data.header
    ranges = data.ranges
    #rospy.loginfo(header)
    #rospy.loginfo(len(ranges))
    len_deg = np.array(ranges[::4])
    #rospy.loginfo(len(len_per_deg))
    angle_n = 5
    len_per_ndeg = np.array(len_deg[::angle_n])
    #rospy.loginfo(len(len_per_45deg))
    angle_min = data.angle_min
    #rospy.loginfo(angle_min)
    #draw()

#angle_min: -3.1241390705108643
#angle_max: 3.1415927410125732
#angle_increment: 0.004354226402938366
#time_increment: 5.4129151976667345e-05
#scan_time: 0.07789184898138046
#range_min: 0.15000000596046448
#range_max: 25.0
#ranges:

def draw():
    global rout,now_dot
    #rospy.loginfo(np.shape(slam_map))
    
    map_x = -map_pos.x / res
    map_y = -map_pos.y / res

    x = (-map_pos.x+now_x) / res
    y = (-map_pos.y+now_y) / res

    dot_size = h/100
    img = np.zeros((h, w, 3), dtype=np.uint8)
    try:
        img[:,:,:]=slam_map[:,:,:]
    except ValueError:
        rospy.loginfo("ValueError")
    img[ (img[:,:,0]!=255) & (img[:,:,0]>=70)  ] = [255,0,0]
    
    rad_angle_n = angle_n*np.pi/180
    

###############    draw 360 scanline   ####################
    if rospy.get_param("/draw_scan_line"):
    #if True:
        for i in range(len(len_per_ndeg)):
            if len_per_ndeg[i]==float("inf"):
                continue
            #rospy.loginfo(len_per_ndeg[i])
            try:
                cv2.line(img, (int(x),int(y)), 
                     (int(x+(len_per_ndeg[i]*np.cos(xyz[2]+angle_min+(rad_angle_n*i)))/res),
                      int(y+(len_per_ndeg[i]*np.sin(xyz[2]+angle_min+(rad_angle_n*i)))/res)),
                      (0, 255, 0), int(1+(dot_size)/5))
            except OverflowError:
                rospy.loginfo("get inf")
                rospy.loginfo(len_per_ndeg[i])

####################    draw now scanning dot    ####################
    #if rospy.get_param("/draw_scan_adge"):
    if True:
        #rospy.loginfo(np.shape(len_deg))
        for i in range(len(len_deg)):
            if len_deg[i]==float("inf"):
                continue
            try:
                cv2.circle(img, (int(x+(len_deg[i]*np.cos(xyz[2]+angle_min+i*(np.pi/180)))/res),
                int(y+(len_deg[i]*np.sin(xyz[2]+angle_min+i*(np.pi/180)))/res)),1, (52, 207, 235), -1 )
            except OverflowError:
                rospy.loginfo("get inf")
                rospy.loginfo(len_deg[i])

####################    draw crashing line   ####################
    crash_range = 0.6
    car_w = 0.48
    check_r = ((np.arctan((car_w/2)/crash_range)/np.pi)*180)*0.8
    #rospy.loginfo(check_r)
    #if rospy.get_param("/draw_scan_adge"):
    if True:
        #rospy.loginfo(angle_min)
        for i in range(int(check_r)):
            if len_deg[i]==float("inf"):
                continue
            try:
                check_col = (0, 255, 0)
                if len_deg[i]<crash_range:
                    check_col = (235, 52, 232)
                cv2.line(img, (int(x),int(y)),
                            (int(x+(len_deg[i]*np.cos(xyz[2]+angle_min+i*(np.pi/180)))/res),
                            int(y+(len_deg[i]*np.sin(xyz[2]+angle_min+i*(np.pi/180)))/res)),
                            check_col, int(1+(dot_size)/5))
            except OverflowError:
                rospy.loginfo("get inf")
                rospy.loginfo(len_deg[i])

            if len_deg[i*-1-1]==float("inf"):
                continue
            try:
                check_col = (0, 255, 0)
                if len_deg[i*-1]<crash_range:
                    check_col = (235, 52, 232)
                cv2.line(img, (int(x),int(y)),                                                      
                            (int(x+(len_deg[i*-1-1]*np.cos(xyz[2]+angle_min+(i*-1-1)*(np.pi/180)))/res),
                            int(y+(len_deg[i*-1-1]*np.sin(xyz[2]+angle_min+(i*-1-1)*(np.pi/180)))/res)),
                            check_col, int(1+(dot_size)/5))
            except OverflowError:
                rospy.loginfo("get inf")
                rospy.loginfo(len_deg[i*-1-1])
    

    if not rospy.get_param("/turning"):
        if len_deg[:int(check_r)].min() < crash_range or len_deg[int(-check_r):].min() < crash_range :
            rospy.loginfo("crash!!")
            ok_len = (car_w*1.2)/np.sin( ( (3*check_r) /180) *np.pi)
            for deg_p in range(int(check_r*0.1),int(check_r)+45):
                if len_deg[int(deg_p):int(check_r+deg_p)].min() > ok_len :
                    find_deg = ((check_r*1.3+deg_p)/180)*np.pi
                    finded = [now_x-ok_len*np.cos(find_deg+xyz[2]),now_y-ok_len*np.sin(find_deg+xyz[2])]
                    rospy.loginfo(finded)
                    rospy.loginfo(deg_p)
                    rout = np.insert(rout,now_dot+1,[now_x,now_y],0)
                    rout = np.insert(rout,now_dot+2,finded,0)
                    break
                if len_deg[int(-(check_r*1.3+deg_p)):int(-deg_p)].min() > ok_len :
                    find_deg = -((check_r*1.3+deg_p)/180)*np.pi
                    finded = [now_x-ok_len*np.cos(find_deg+xyz[2]),now_y-ok_len*np.sin(find_deg+xyz[2])]
                    rospy.loginfo(finded)
                    rospy.loginfo(-deg_p)
                    rout = np.insert(rout,now_dot+1,[now_x,now_y],0)
                    rout = np.insert(rout,now_dot+2,finded,0)
                    break
                if rospy.is_shutdown():
                    break


    if rospy.get_param("/draw_map_o"):
        cv2.circle(img, (int(map_x),int(map_y)), int(1+dot_size),(0, 255, 255), -1)
    
    if rospy.get_param("/draw_car_o"):
        cv2.circle(img, (int(x),int(y)),int(1+dot_size),(0, 0, 255), -1)

    if rospy.get_param("/draw_car_way"):
        cv2.line(img, (int(x),int(y)), (int(x-5*dot_size*np.cos(xyz[2])),
                                        int(y-5*dot_size*np.sin(xyz[2]))),
                 (0, 0, 255), int(1+(dot_size*2)/3) )

    if rospy.get_param("/draw_car_way"):
        cv2.line(img, (int(x),int(y)), (int(x-5*dot_size*np.cos(xyz[2]-deg)),
                                        int(y-5*dot_size*np.sin(xyz[2]-deg))),
                 (200, 0, 200), int(1+(dot_size)/5) )

    #print(now_dot)
    cv2.circle(img, (int(map_x+rout[now_dot+1,0]/res),int(map_y+rout[now_dot+1,1]/res)),int(1+dot_size),(100, 100, 255), -1)
####################    draw rout   ####################
    if rospy.get_param("/draw_rout"):
        for i in range(len(rout)-1):
            cv2.line(img, (int(map_x+rout[i,0]/res),int(map_y+rout[i,1]/res)),
                          (int(map_x+rout[i+1,0]/res),int(map_y+rout[i+1,1]/res)),
                          (144, 144, 0), int(1+(dot_size)/5))

    if rospy.get_param("/img_flip"):
        img = cv2.flip(img, 1)
    
    publish_image(img)

last_x,last_y = 0,0
try:
    rospy.init_node('slam_control')
    rospy.Subscriber('/scan',LaserScan,update_scan)
    rospy.Subscriber('/tf',TFMessage,update_pos)
    rospy.Subscriber('/map',OccupancyGrid,update_map)
    img_pub = rospy.Publisher('my_image_raw',Image,queue_size=1)
    pub_deg = rospy.Publisher('revise_deg', deg_msg, queue_size=10)
    pub_mot = rospy.Publisher('auto_motion', motor_msg, queue_size=10)

    deg = deg_msg()
    #rate = rospy.wallRate(1) # 10hz
    rospy.loginfo("wait to start")
    while setup.all() != True:
        if rospy.is_shutdown():
            break
        continue
    rospy.loginfo(setup)
    rospy.loginfo("done")
    rospy.set_param("/turning",False)    
    deg = get_deg(np.array([-1,0]),rout[1]-rout[0])
    if deg > np.pi/18:
        rospy.set_param("/turning",True)
        pub_deg.publish(deg)
    
    rate = rospy.Rate(10)
    now_dot = 0
    while not rospy.is_shutdown():
        if rospy.get_param("/turning"):
            rospy.loginfo("turning")
            draw()
            rate.sleep()
            continue
        #rospy.loginfo(rout[1])
        #rospy.loginfo((now_x,now_y))
        #rospy.loginfo(np.linalg.norm([rout[1,0]-now_x,rout[1,1]-now_y]))
        deg = get_deg(np.array([-np.cos(xyz[2]),-np.sin(xyz[2])]),rout[now_dot+1]-[now_x,now_y])
        d_to_next_dot = np.linalg.norm([rout[now_dot+1,0]-now_x,rout[now_dot+1,1]-now_y])
        d_running = np.linalg.norm([last_x-now_x,last_y-now_y])
        if d_to_next_dot < d_running :
            now_dot += 1
            if now_dot==len(rout)-1:
                mymotor = motor_msg()
                mymotor.way = 'stop'
                pub_mot.publish(mymotor)
                while not rospy.is_shutdown():
                    rospy.loginfo("finish!!")
                    rospy.sleep(2)
            rospy.set_param("/turning",True)
            deg = get_deg(np.array([-np.cos(xyz[2]),-np.sin(xyz[2])]),rout[now_dot+1]-[now_x,now_y])
            pub_deg.publish(deg)
        else:
            print((d_to_next_dot,d_running))
        pub_deg.publish(deg)
        draw()
        rate.sleep()
    rospy.spin()
except rospy.ROSInterruptException:
        pass
