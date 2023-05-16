import cv2
import numpy as np
import matplotlib.pyplot as plt
# 1.20 图像拆分通道 (Numpy切片)
img1 = cv2.imread("Lenna.png", flags=1)  # flags=1 读取彩色图像(BGR)
img_HSV = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
# 获取 H 通道
hImg = img_HSV.copy()  # 获取 HSV
hImg[:, :, 1] = 0  # G=0
hImg[:, :, 2] = 0  # R=0

# 获取 S 通道
sImg = img_HSV.copy()  # 获取 HSV
sImg[:, :, 0] = 0  # B=0
sImg[:, :, 2] = 0  # R=0

# 获取 V 通道
vImg = img_HSV.copy()  # 获取 HSV
vImg[:, :, 0] = 0  # B=0
vImg[:, :, 1] = 0  # G=0

plt.subplot(131), plt.title("1. H channel"), plt.axis('off')
plt.imshow(hImg)  # matplotlib 显示 channel H

plt.subplot(132), plt.title("2. S channel"), plt.axis('off')
plt.imshow(sImg)  # matplotlib 显示 channel S

plt.subplot(133), plt.title("3. V channel"), plt.axis('off')
plt.imshow(vImg)  # matplotlib 显示 channel V

plt.show()
