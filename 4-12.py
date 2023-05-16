# -*- coding: UTF-8 -*-
#!/usr/bin/env python3
 
from __future__ import division
import cv2
import numpy as np
import matplotlib.pyplot as plt
#from matplotlib import pyplot as plt

image = cv2.imread('/home/zc/Desktop/lenna.jpg')
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)#cv2.COLOR_BGR2HSV
cv2.imshow('hsv',hsv)
cv2.waitKey(0)

#cv2.imwrite('/home/zc/Desktop/lenna2.jpg', image, [cv2.IMWRITE_JPEG_QUALITY, 50])






def image_hist(image):
    """绘制hsv的直方图（二个通道）"""
   
    hist_H = cv2.calcHist([hsv], [0], None, [256], [0, 256])
    hist_S = cv2.calcHist([hsv], [1], None, [256], [0, 256])
    #量纲12,582,912
    i = 0
    while i < 256:
       hist_H[i] = (hist_H[i]/12582912)*2550
       i+=1
    j = 0
    while j < 256:
       hist_S[j] = (hist_S[j]/12582912)*2550
       j+=1
    i = 0
    while i < 10:     #去掉H<10的像素点
      hist_H[i] = 0
      i+=1
    print(hist_H)
    j = 0
    while j < 10:     #去掉S<10的像素点
      hist_S[j] = 0
      j+=1
    print(hist_S)
    #plt.scatter(hist_H,hist_S)
    #plt.xlim([0, 25500])  # 设置坐标轴刻度取值范围
    #plt.ylim([0, 25500])
    plt.plot(hist_H, color='blue')  #  绘制函数曲线
    plt.plot(hist_S, color='red')
    plt.xlim([0, 255])  # 设置坐标轴刻度取值范围
    plt.ylim([0, 255])
    plt.show()
    cv2.waitKey(2000)
   

image_hist(hsv)
   
