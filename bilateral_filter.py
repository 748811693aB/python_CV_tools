import cv2
import numpy as np
import matplotlib.pyplot as plt
# 1.74：图像的非线性滤波—双边滤波器
img = cv2.imread("Lenna.png", flags=1)

imgBiFilter = cv2.bilateralFilter(img, d=0, sigmaColor=100, sigmaSpace=10)

plt.figure(figsize=(9, 6))
plt.subplot(121), plt.axis('off'), plt.title("Original")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.subplot(122), plt.axis('off'), plt.title("cv2.bilateralFilter")
plt.imshow(cv2.cvtColor(imgBiFilter, cv2.COLOR_BGR2RGB))
plt.tight_layout()
plt.show()
