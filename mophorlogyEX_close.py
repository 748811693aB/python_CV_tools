import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取原始图像
imgGray = cv2.imread("dilate.png", flags=0)  # flags=0 读取为灰度图像
mu, sigma = 0.0, 10.0
noiseGause = np.random.normal(mu, sigma, imgGray.shape)
imgNoisy = imgGray + noiseGause
imgNoisy = np.uint8(cv2.normalize(imgNoisy, None, 0, 255, cv2.NORM_MINMAX))  # 归一化为 [0,255]
ret, imgBin = cv2.threshold(imgNoisy, 125, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)  # 二值化处理
'''
# 图像的闭运算
kSize = (2, 2)  # 卷积核的尺寸
kernel = np.ones(kSize, dtype=np.uint8)  # 生成盒式卷积核
imgClose1 = cv2.morphologyEx(imgBin, cv2.MORPH_CLOSE, kernel)
'''
kSize = (5, 5)  # 卷积核的尺寸
kernel = np.ones(kSize, dtype=np.uint8)  # 生成盒式卷积核
imgClose2 = cv2.morphologyEx(imgBin, cv2.MORPH_CLOSE, kernel)
'''
kSize = (10, 10)  # 卷积核的尺寸
kernel = np.ones(kSize, dtype=np.uint8)  # 生成盒式卷积核
imgClose3 = cv2.morphologyEx(imgBin, cv2.MORPH_CLOSE, kernel)
'''
plt.figure(figsize=(10, 5))
plt.subplot(121), plt.axis('off'), plt.title("Origin")
plt.imshow(imgNoisy, cmap='gray', vmin=0, vmax=255)
plt.subplot(122), plt.title("Closed kSize=(5,5)"), plt.axis('off')
plt.imshow(imgClose2, cmap='gray', vmin=0, vmax=255)
'''plt.subplot(143), plt.title("Closed kSize=(5,5)"), plt.axis('off')
plt.imshow(imgClose2, cmap='gray', vmin=0, vmax=255)
plt.subplot(144), plt.title("Closed kSize=(10,10)"), plt.axis('off')
plt.imshow(imgClose3, cmap='gray', vmin=0, vmax=255)'''
plt.tight_layout()
plt.show()


