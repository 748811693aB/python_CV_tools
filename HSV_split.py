import cv2
import numpy as np
# 1.19 图像拆分通道
img1 = cv2.imread("Lenna.png", flags=1)  # flags=1 读取彩色图像(BGR)
cv2.imshow("BGR", img1)  # BGR 图像

img_HSV = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
# HSV 通道拆分
hImg, sImg, vImg = cv2.split(img_HSV)  # 拆分为 HSV 独立通道
cv2.imwrite(r'C:\Users\hxb971002\Pictures\merge\hImg.png',hImg)
cv2.imwrite(r'C:\Users\hxb971002\Pictures\merge\sImg.png',sImg)
cv2.imwrite(r'C:\Users\hxb971002\Pictures\merge\vImg.png',vImg)
cv2.imshow("hImg", hImg)  
cv2.imshow("sImg", sImg)
cv2.imshow("vImg", vImg)

cv2.waitKey(0)
cv2.destroyAllWindows()  # 释放所有窗口
