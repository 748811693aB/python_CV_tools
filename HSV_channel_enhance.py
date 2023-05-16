import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread("Lenna.png", flags=1)  # flags=1 读取彩色图像(HSV)
img_HSV = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", img_HSV)  # HSV 图像

# HSV 通道拆分
hImg, sImg, vImg = cv2.split(img_HSV)  # 拆分为 HSV 独立通道

img_new = np.zeros(img_HSV.shape, np.uint8)

img_new[:, :, 0] = hImg + 100
img_new[:, :, 1] = sImg
img_new[:, :, 2] = vImg 


cv2.imshow('img_new',img_new)
cv2.waitKey(0)
cv2.destroyAllWindows()  # 释放所有窗口