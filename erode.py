import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取原始图像
imgGray = cv2.imread("erode.png", flags=0)  # flags=0 读取为灰度图像
ret, imgBin = cv2.threshold(imgGray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)  # 二值化处理

# 图像腐蚀
kSize = (3, 3)  # 卷积核的尺寸
kernel = np.ones(kSize, dtype=np.uint8)  # 生成盒式卷积核
imgErode1 = cv2.erode(imgBin, kernel=kernel)  # 图像腐蚀

kSize = (6, 6)
kernel = np.ones(kSize, dtype=np.uint8)
imgErode2 = cv2.erode(imgBin, kernel=kernel)

kSize = (9, 9)
kernel = np.ones(kSize, dtype=np.uint8)
imgErode3 = cv2.erode(imgBin, kernel=kernel)

plt.figure(figsize=(10, 5))
plt.subplot(141), plt.axis('off'), plt.title("Origin")
plt.imshow(imgBin, cmap='gray', vmin=0, vmax=255)
plt.subplot(142), plt.title("eroded kSize=(3,3)"), plt.axis('off')
plt.imshow(imgErode1, cmap='gray', vmin=0, vmax=255)
plt.subplot(143), plt.title("eroded kSize=(6,6)"), plt.axis('off')
plt.imshow(imgErode2, cmap='gray', vmin=0, vmax=255)
plt.subplot(144), plt.title("eroded kSize=(9,9)"), plt.axis('off')
plt.imshow(imgErode3, cmap='gray', vmin=0, vmax=255)
plt.tight_layout()
plt.show()

