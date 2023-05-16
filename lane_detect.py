#!/usr/bin/env python3
from __future__ import division
import cv2
import numpy as np
import matplotlib.pyplot as plt

capture = cv2.VideoCapture(1)

def nothing(*arg):
        pass
def process_an_image(img):
    # 2. 标记四个坐标点用于ROI截取
    points = np.array([[(0, 628), (331, 187), (557, 187), (953, 630)]])
    roi_edges = roi_mask(img, points)
    return  roi_edges
def roi_mask(img, corner_points):
    # 创建掩膜
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, corner_points, (255,255,255))
    masked_img = cv2.bitwise_and(img, mask)
    return masked_img
frame = cv2.imread('raw_road.png')
#frame = process_an_image(frame)
cv2.imshow("MaskROI", frame)  # 显示从 img1 提取的 ROI
frameGray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
hImg,wImg = frameGray.shape

# Initial HSV GUI slider values to load on program start.
#icol = (36, 202, 59, 71, 255, 255)  # Green
#icol = (18, 0, 196, 36, 255, 255)  # Yellow
#icol = (89, 0, 0, 125, 255, 255)  # Blue
icol = (0, 100, 80, 10, 255, 255)   # Red
cv2.namedWindow('colorTest')
# Lower range colour sliders.
cv2.createTrackbar('lowHue', 'colorTest', icol[0], 255, nothing)
cv2.createTrackbar('lowSat', 'colorTest', icol[1], 255, nothing)
cv2.createTrackbar('lowVal', 'colorTest', icol[2], 255, nothing)
# Higher range colour sliders.
cv2.createTrackbar('highHue', 'colorTest', icol[3], 255, nothing)
cv2.createTrackbar('highSat', 'colorTest', icol[4], 255, nothing)
cv2.createTrackbar('highVal', 'colorTest', icol[5], 255, nothing)
top = 0
bottom = 0
while True:
    # Get HSV values from the GUI sliders.
    lowHue = cv2.getTrackbarPos('lowHue', 'colorTest')
    lowSat = cv2.getTrackbarPos('lowSat', 'colorTest')
    lowVal = cv2.getTrackbarPos('lowVal', 'colorTest')
    highHue = cv2.getTrackbarPos('highHue', 'colorTest')
    highSat = cv2.getTrackbarPos('highSat', 'colorTest')
    highVal = cv2.getTrackbarPos('highVal', 'colorTest')
 
    # Show the original image.
    
    #ret, frame = capture.read()
    cv2.imshow('frame', frame)
    # Blur methods available, comment or uncomment to try different blur methods.
    frameBGR = cv2.GaussianBlur(frame, (7, 7), 0)
    #frameBGR = cv2.medianBlur(frameBGR, 7)
    #frameBGR = cv2.bilateralFilter(frameBGR, 15 ,75, 75)
    """kernal = np.ones((15, 15), np.float32)/255
    frameBGR = cv2.filter2D(frameBGR, -1, kernal)"""
	
    # Show blurred image.
    cv2.imshow('blurred', frameBGR)
	
    # HSV (Hue, Saturation, Value).
    # Convert the frame to HSV colour model.
    hsv = cv2.cvtColor(frameBGR, cv2.COLOR_BGR2HSV)
    cv2.imshow('hsv', hsv)
    # HSV values to define a colour range.
    colorLow = np.array([lowHue,lowSat,lowVal])
    colorHigh = np.array([highHue,highSat,highVal])
    mask = cv2.inRange(hsv, colorLow, colorHigh)
    # Show the first mask
    cv2.imshow('mask-plain', mask)
 
    kernal = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
    print('kernal =',kernal)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)
 
    # Show morphological transformation mask
    cv2.imshow('mask', mask)
    
    # Put mask over top of the original image.
    result = cv2.bitwise_and(frame, frame, mask = mask)
 
    # Show final output image
    #cv2.imshow('colorTest', result)
    #result = mask
    #Canny
    t1, t2 = 50, 150
    imgCanny = cv2.Canny(result, t1, t2)
    cv2.imshow('imgCanny', imgCanny)
    #Hough
    lines = cv2.HoughLines(imgCanny, 1, np.pi/180, threshold=120)  # lines: (n, 1, 2)
    print('lines =',lines.shape, type(lines))  # (11,1,2)
    imgEdge = result.copy()

    top_num =0 
    bottom_num = 0
    for i in range(8):
        rho, theta = lines[i,0,:]  # lines: (n,1,2)
        if (theta < (np.pi/4)) or (theta > (3*np.pi/4)):  # 直线与图像上下相交
            pt1 = (int(rho/np.cos(theta)), 0)  # (x,0), 直线与顶侧的交点
            pt2 = (int((rho - hImg * np.sin(theta))/np.cos(theta)), hImg)  # (x,h), 直线与底侧的交点
            cv2.line(imgEdge, pt1, pt2, (255, 0, 0),5)  # 绘制直线
            top += pt1[0]
            bottom += pt2[0]
            top_num += 1
        else:  # 直线与图像左右相交
            pt1 = (0, int(rho/np.sin(theta)))  # (0,y), 直线与左侧的交点
            pt2 = (wImg, int((rho - wImg * np.cos(theta))/np.sin(theta)))  # (w,y), 直线与右侧的交点
            #cv2.line(imgEdge, pt1, pt2, (255, 0, 255), 5)  # 绘制直线
        print(rho, theta, pt1, pt2)
    top_mid = top/top_num
    bottom_mid = bottom/top_num
    #cv2.line(imgEdge, (int(top_mid),0), (int(bottom_mid),hImg), (0, 255,0),5)  # 绘制中线
    minLineLength = 100  # 直线的最短长度
    maxLineGap = 20  # 线段之间最大间隔
    lines = cv2.HoughLinesP(imgCanny, 1, np.pi/180, 100, minLineLength, maxLineGap)  # lines: (n,1,4)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        #cv2.line(imgEdge, (x1,y1), (x2,y2), (255, 215, 0), 5)  # 绘制直线

    plt.figure(figsize=(9, 5))
    ret1, imgEdge = cv2.threshold(imgEdge, 10, 255, cv2.THRESH_BINARY)
    plt.subplot(111), plt.title("Hough"), plt.imshow(cv2.cvtColor(imgEdge, cv2.COLOR_RGB2BGR)), plt.axis('off')
    plt.tight_layout()
    plt.show()
   
   
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    
cv2.destroyAllWindows()