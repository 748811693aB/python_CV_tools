import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread("Lenna.png", flags=1)  # flags=1 读取彩色图像(BGR)
cv2.imshow("BGR", img1)  # BGR 图像

# BGR 通道拆分
bImg, gImg, rImg = cv2.split(img1)  # 拆分为 BGR 独立通道
cv2.imshow("rImg", rImg)  # 直接显示红色分量 rImg 显示为灰度图像
cv2.imshow("gImg", gImg)
cv2.imshow("bImg", bImg)

img_new = np.zeros(img1.shape, np.uint8)

img_new[:, :, 0] = bImg 
img_new[:, :, 1] = gImg
img_new[:, :, 2] = rImg -60


cv2.imshow('img_new',img_new)
cv2.waitKey(0)
cv2.destroyAllWindows()  # 释放所有窗口