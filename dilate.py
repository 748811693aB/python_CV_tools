import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取原始图像
imgGray = cv2.imread("dilate.png", flags=0)  # flags=0 读取为灰度图像
ret, imgBin = cv2.threshold(imgGray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)  # 二值化处理
# 10.2 图像的膨胀 (cv.dilate)
# cv.dilate(src, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]]) → dst

# 图像膨胀
kSize = (3, 3)  # 卷积核的尺寸
kernel = np.ones(kSize, dtype=np.uint8)  # 生成盒式卷积核
imgDilate1 = cv2.dilate(imgBin, kernel=kernel)  # 图像膨胀

kSize = (5, 5)
kernel = np.ones(kSize, dtype=np.uint8)
imgDilate2 = cv2.dilate(imgBin, kernel=kernel)  # 图像膨胀

kSize = (7, 7)
kernel = np.ones(kSize, dtype=np.uint8)
imgDilate3 = cv2.dilate(imgBin, kernel=kernel)  # 图像膨胀

plt.figure(figsize=(10, 5))
plt.subplot(141), plt.axis('off'), plt.title("Origin")
plt.imshow(imgBin, cmap='gray', vmin=0, vmax=255)
plt.subplot(142), plt.title("dilate kSize=(3,3)"), plt.axis('off')
plt.imshow(imgDilate1, cmap='gray', vmin=0, vmax=255)
plt.subplot(143), plt.title("dilate kSize=(5,5)"), plt.axis('off')
plt.imshow(imgDilate2, cmap='gray', vmin=0, vmax=255)
plt.subplot(144), plt.title("dilate kSize=(7,7)"), plt.axis('off')
plt.imshow(imgDilate3, cmap='gray', vmin=0, vmax=255)
plt.tight_layout()
plt.show()
