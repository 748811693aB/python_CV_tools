#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import cv2
import matplotlib.pyplot as plt
img = cv2.imread("Troad_small.png", flags=1)  # flags=1 读取为彩色图像    
cv2.imshow('origin',img)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('imgGray',imgGray)
hImg, wImg = imgGray.shape

# Canny 边缘检测， kSize 为高斯核大小，t1, t2为阈值大小
ratio, low = 3, 120
imgGauss = cv2.GaussianBlur(imgGray, (5, 5), 0)
cv2.imshow('imgGauss',imgGauss)
imgCanny = cv2.Canny(imgGauss, low, low*ratio)
cv2.imshow('Canny',imgCanny)
pEdge = np.where(imgCanny==255)  # 所有的边缘像素
print(hImg, wImg, imgCanny.max(), imgCanny.min(), len(pEdge[0]))

# # 霍夫线变换
# # cv.HoughLines(image, rho, theta, threshold[, lines[, srn[, stn[, min_theta[, max_theta]]]]])
# # rho 距离分辨率（以像素为单位）, theta 角度分辨率（弧度）
# # threshold 累加器阈值参数
# # 返回：列表，形状为 (n,1,2) 的 Numpy 数组，每个元素 (n,1,:) 表示直线参数 rho, theta
lines = cv2.HoughLines(imgCanny, 1, np.pi/180, threshold=20)  # lines: (n, 1, 2)
print(lines.shape, type(lines))  # (11,1,2)
imgEdge = img.copy()

mid_x=0
mid_y=0
mid_x_cnt = 0
mid_y_cnt = 0
for i in range(6):
  rho, theta = lines[i,0,:]  # lines: (n,1,2)
  if (theta < (np.pi/4)) or (theta > (3*np.pi/4)):  # 直线与图像上下相交
    pt1 = (int(rho/np.cos(theta)), 0)  # (x,0), 直线与顶侧的交点
    pt2 = (int((rho - hImg * np.sin(theta))/np.cos(theta)), hImg)  # (x,h), 直线与底侧的交点
    cv2.line(imgEdge, pt1, pt2, (255, 0, 0),5)  # 绘制直线
    mid_x_cnt= mid_x_cnt+ 1
    mid_x=mid_x+ pt1[0]
  else:  # 直线与图像左右相交
    pt1 = (0, int(rho/np.sin(theta)))  # (0,y), 直线与左侧的交点
    pt2 = (wImg, int((rho - wImg * np.cos(theta))/np.sin(theta)))  # (w,y), 直线与右侧的交点
    cv2.line(imgEdge, pt1, pt2, (255, 0, 0), 5)  # 绘制直线
    mid_y_cnt = mid_y_cnt+1
    mid_y  = mid_y+pt1[1]  
  print(rho, theta, pt1, pt2)
mid_x = mid_x/mid_x_cnt
mid_y = mid_y/mid_y_cnt 
print(mid_x,mid_y)
mid_x=int(mid_x)
mid_y=int(mid_y)
cv2.circle(imgEdge, (mid_x-10,mid_y+10), 10, (0, 255, 0),-1)
cv2.imshow('Hough',imgEdge)
# 累积概率霍夫变换
# # cv.HoughLinesP(image, rho, theta, threshold[, lines[, minLineLength[, maxLineGap]]])
# # rho 距离分辨率（以像素为单位）, theta 角度分辨率（弧度）
# # threshold 累加器阈值参数, minLineLength 最小直线长度, maxLineGap 最大允许间隔
# # 返回：列表，每个元素是一个 4 元组，表示直线端点坐标 (x1, y1, x2, y2)

minLineLength = 100  # 直线的最短长度
maxLineGap = 20  # 线段之间最大间隔
lines = cv2.HoughLinesP(imgCanny, 1, np.pi/180, 100, minLineLength, maxLineGap)  # lines: (n,1,4)
for line in lines:
  x1, y1, x2, y2 = line[0]
  cv2.line(imgEdge, (x1,y1), (x2,y2), (0, 255, 0), 5)  # 绘制直线

plt.figure(figsize=(9, 5))
plt.subplot(131), plt.title("Origin"), plt.imshow(imgGray, cmap='gray'), plt.axis('off')
plt.subplot(132), plt.title("Canny"), plt.imshow(imgCanny, cmap='gray'), plt.axis('off')
plt.subplot(133), plt.title("Hough"), plt.imshow(cv2.cvtColor(imgEdge, cv2.COLOR_RGB2BGR)), plt.axis('off')
plt.tight_layout()
plt.show()
