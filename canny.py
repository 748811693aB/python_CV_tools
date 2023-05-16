import cv2
import numpy as np
import matplotlib.pyplot as plt
# 11.8 Canny 边缘检测算子
img = cv2.imread("Lenna.png", flags=0)  # flags=0 读取为灰度图像
# 高斯核低通滤波器，sigmaY 缺省时 sigmaY=sigmaX
kSize = (5, 5)
imgGauss1 = cv2.GaussianBlur(img, kSize, sigmaX=1.0)  # sigma=1.0
# Canny 边缘检测， kSize 为高斯核大小，t1,t2为阈值大小
t1, t2 = 50, 150
imgCanny = cv2.Canny(imgGauss1, t1, t2)
plt.figure(figsize=(10, 6))
plt.subplot(121), plt.title("Origin"), plt.imshow(img, cmap='gray'), plt.axis('off')
plt.subplot(122), plt.title("Canny"), plt.imshow(imgCanny, cmap='gray'), plt.axis('off')
plt.tight_layout()
plt.show()
