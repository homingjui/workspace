import pyrealsense2 as rs
import numpy as np
import cv2

pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth,640,480,rs.format.z16,30)
config.enable_stream(rs.stream.color,640,480,rs.format.bgr8,30)

pipeline.start(config)

align_to = rs.stream.color
align = rs.align(align_to)

try:
	while True:
		frames = pipeline.wait_for_frames()
		aligend_frames = align.process(frames)
		depth_frame = aligend_frames.get_depth_frame()
		color_frame = aligend_frames.get_color_frame()
		if not depth_frame or not color_frame:
			continue

		depth_image = np.asanyarray(depth_frame.get_data())
		color_image = np.asanyarray(color_frame.get_data())
		depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image,alph=0.03),cv2.COLORMAP_JET)

		face_cascade = cv2.CascadeClassifier('/home/isp/Desktop/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml')
		gray = cv2.cvtColor(color_image,cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(gray,scaleFactor=1.2,minNeighbor=5,minsize=(50,50))

		for (x,y,w,h) in faces:
			cv2.rectangle(color_image,(x,y-5),(x+w,y+h),(255,0,0),2)
			text_depth = "depth is "+str(np.round(depth_frame.get_distance(int (x+(1/2)*w),int (y+(1/2)*h)),3)+"m")
			color_image=cv2.putText(color_image,text_depth,(x,y-5),cv2.FONT_HERSHEY_PLAIN,1,(0.0.255),1,cv2.LINE_AA)

		images = np.hstack((color_image,depthcolormap))

		cv2.nameWindow('Realsense',cv2.WINDOW_AUTOSIZE)
		cv2.imshow('Realsense',images)

		key = cv2.waitKey(1)

		if Key & 0xFF == ord('q') or Key == 27:
			cv2.destroyAllWindows()
			break
finally:
	pipeline.stop()
	

