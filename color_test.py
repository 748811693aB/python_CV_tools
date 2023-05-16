#!/usr/bin/env python3
 
"""
File: opencv-open-file-color-test.py
 
This Python 3 code is published in relation to the article below:
https://www.bluetin.io/opencv/opencv-color-detection-filtering-python/
 
Website:    www.bluetin.io
Author:     Mark Heywood
Date:	    8/12/2017
Version     0.1.0
License:    MIT
"""
 
from __future__ import division
import cv2
import numpy as np
 
def nothing(*arg):
        pass

# Initial HSV GUI slider values to load on program start.
#icol = (36, 202, 59, 71, 255, 255)    # Green
icol = (18, 0, 196, 36, 255, 255)  # Yellow
#icol = (89, 0, 0, 125, 255, 255)  # Blue
#icol = (0, 100, 80, 10, 255, 255)   # Red
cv2.namedWindow('colorTest')
# Lower range colour sliders.
cv2.createTrackbar('lowHue', 'colorTest', icol[0], 255, nothing)
cv2.createTrackbar('lowSat', 'colorTest', icol[1], 255, nothing)
cv2.createTrackbar('lowVal', 'colorTest', icol[2], 255, nothing)
# Higher range colour sliders.
cv2.createTrackbar('highHue', 'colorTest', icol[3], 255, nothing)
cv2.createTrackbar('highSat', 'colorTest', icol[4], 255, nothing)
cv2.createTrackbar('highVal', 'colorTest', icol[5], 255, nothing)
 
# Raspberry pi file path example.
frame = cv2.imread('/home/zc/catkin_wss/src/visions/scripts/road.jpg')
# Windows file path example.
#frame = cv2.imread('road.jpg')

#HXB imag_size middle_lane
height, width, channels = frame.shape
print(height, width, channels)
cx, cy = height/2, width/2
print(cx,cy)

while True:
    # Get HSV values from the GUI sliders.
    lowHue = cv2.getTrackbarPos('lowHue', 'colorTest')
    lowSat = cv2.getTrackbarPos('lowSat', 'colorTest')
    lowVal = cv2.getTrackbarPos('lowVal', 'colorTest')
    highHue = cv2.getTrackbarPos('highHue', 'colorTest')
    highSat = cv2.getTrackbarPos('highSat', 'colorTest')
    highVal = cv2.getTrackbarPos('highVal', 'colorTest')
 
    # Show the original image.
    cv2.imshow('frame', frame)
    
    # Blur methods available, comment or uncomment to try different blur methods.
    frameBGR = cv2.GaussianBlur(frame, (7, 7), 0)
    #frameBGR = cv2.medianBlur(frameBGR, 7)
    #frameBGR = cv2.bilateralFilter(frameBGR, 15 ,75, 75)
    """kernal = np.ones((15, 15), np.float32)/255
    frameBGR = cv2.filter2D(frameBGR, -1, kernal)"""
	
    # Show blurred image.
    #cv2.imshow('blurred', frameBGR)
	
    # HSV (Hue, Saturation, Value).
    # Convert the frame to HSV colour model.
    hsv = cv2.cvtColor(frameBGR, cv2.COLOR_BGR2HSV)
    
    # HSV values to define a colour range.
    colorLow = np.array([lowHue,lowSat,lowVal])
    colorHigh = np.array([highHue,highSat,highVal])
    mask = cv2.inRange(hsv, colorLow, colorHigh)
    # Show the first mask
    #cv2.imshow('mask-plain', mask)
 
    kernal = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)
 
    # Show morphological transformation mask
    #cv2.imshow('mask', mask)
    
    # Put mask over top of the original image.
    result = cv2.bitwise_and(frame, frame, mask = mask)
 
    
    # Show final output image
    #cv2.imshow('colorTest', result)
    #cv2.imwrite(r"/home/zc/Desktop/lenna.jpg",result)

    #cut_image height width
    cut_result=result[900:1270,2:300].copy()
    cv2.imwrite(r"/home/zc/Desktop/lenna2.jpg",cut_result)
    

   # 
    cvImg = cv2.cvtColor(cut_result, 6)  # cv2.COLOR_BGR2GRAY
    npImg = np.asarray(cvImg)
    thresh = cv2.threshold(npImg, 1, 255, cv2.THRESH_BINARY)[1]
    # 
    thre,cnts, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

    # 
    for c in cnts:

	    # 
	    if c.shape[0] < 150:
		continue

	    # 
	    M = cv2.moments(c)

	    if int(M["m00"]) not in range(500, 22500):
		continue

	    cX = int(M["m10"] / M["m00"])
	    cY = int(M["m01"] / M["m00"])

	    print("x: {}, y: {}, size: {}".format(cX, cY, M["m00"]))

	    # 
	    cv2.drawContours(cut_result, [c], -1, (0, 0, 255), 5)
	    draw_line = cv2.circle(cut_result, (cX, cY), 1, (0, 0, 255), -1)
    cv2.imshow('draw_line', draw_line)    







    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    
cv2.destroyAllWindows()
