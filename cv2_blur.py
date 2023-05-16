import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("Lenna.png", flags=0)

kSize = (5, 5)
imgConv2 = cv2.blur(img, kSize)  # cv2.blur 方法
kSize = (11, 11)
imgConv11 = cv2.blur(img, kSize)  # cv2.blur 方法

plt.figure(figsize=(9, 6))
plt.subplot(131), plt.axis('off'), plt.title("Original")
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.subplot(132), plt.axis('off'), plt.title("cv2.blur (kSize=[5,5])")
plt.imshow(imgConv2, cmap='gray', vmin=0, vmax=255)
plt.subplot(133), plt.axis('off'), plt.title("cv2.blur (kSize=[11,11])")
plt.imshow(imgConv11, cmap='gray', vmin=0, vmax=255)
plt.tight_layout()
plt.show()


