#!/usr/bin/python
import numpy as np
import time
import cv2
import os
import sys

input_path = sys.argv[1]
filenames = os.listdir(input_path)
filenames.sort()

for filename in filenames:
	#filepath = os.sep.join([input_path, filename])
	#print filepath
	print filename
  shotname = os.path.splitext(filename)
	print shotname[0],shotname[1]
    	
	img = cv2.imread(filename)
  text = shotname[0]
	cv2.putText(img, text, (1100,50), 0, 1.5, (0,0,255),2)
	cv2.namedWindow("Image")
	cv2.imshow("Image",img)
	cv2.waitKey(1)




