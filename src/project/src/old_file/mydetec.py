#!/usr/bin/python3


import jetson.inference
import jetson.utils

import argparse
import sys

import numpy as np
import cv2



parser = argparse.ArgumentParser()

parser.add_argument("input_URI", type=str, default="", nargs='?')
parser.add_argument("output_URI", type=str, default="", nargs='?')
parser.add_argument("--overlay", type=str, default="box,labels,conf")
parser.add_argument("--threshold", type=float, default=0.5)
parser.add_argument("--network", type=str, default="facenet-120")
parser.add_argument("--camera", type=str, default="/dev/video2")


is_headless = ["--headless"] if sys.argv[0].find('console.py') != -1 else [""]

try:
	opt = parser.parse_known_args()[0]
except:
	print("")
	parser.print_help()
	sys.exit(0)
print(opt)
print(sys.argv)
sys.argv += ['--camera=/dev/video2']
sys.argv += ['--network=facenet-120']
sys.argv += ['--threshold=0.1']

# load the object detection network
net = jetson.inference.detectNet(opt.network, sys.argv, opt.threshold)

# create video sources & outputs
input = jetson.utils.videoSource(opt.input_URI, argv=sys.argv)
#output = jetson.utils.videoOutput(opt.output_URI, argv=sys.argv+is_headless)


while True:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2RGBA).astype(np.float32)
    img = jetson.utils.cudaFromNumpy(img)
    detections = net.Detect(img, overlay=opt.overlay)
    img2 = jetson.utils.cudaToNumpy(img, 1280, 720, 4)
    img2 = cv2.cvtColor(np.array(img2), cv2.COLOR_RGBA2RGB).astype(np.uint8)
    img2 = cv2.cvtColor(img2, cv2.COLOR_RGB2BGR)
    for detection in detections:
        print(detection)
    cv2.imshow('img',img2)
    cv2.waitKey(0)


# process frames until the user exits
#while True:
	# capture the next image
#	img = input.Capture()

	# detect objects in the image (with overlay)
#	detections = net.Detect(img, overlay=opt.overlay)

	# print the detections
#	print("detected {:d} objects in image".format(len(detections)))

#	for detection in detections:
#		print(detection)

	# render the image
#	output.Render(img)

	# update the title bar
#	output.SetStatus("{:s} | Network {:.0f} FPS".format(opt.network, net.GetNetworkFPS()))

	# print out performance info
#	net.PrintProfilerTimes()
        
	# exit on input/output EOS
#	if not input.IsStreaming() or not output.IsStreaming():
#		break
