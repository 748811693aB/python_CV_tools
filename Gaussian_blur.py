import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("deep-learn.jpg", flags=1)

kSize = (5, 5)
imgGaussBlur1 = cv2.GaussianBlur(img, (3,3), sigmaX=0)
imgGaussBlur2 = cv2.GaussianBlur(img, (11,11), sigmaX=0)

plt.figure(figsize=(9, 6))
plt.subplot(131), plt.axis('off'), plt.title("Original")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.subplot(132), plt.axis('off'), plt.title("ksize=3, sigma=0")
plt.imshow(cv2.cvtColor(imgGaussBlur1, cv2.COLOR_BGR2RGB))
plt.subplot(133), plt.axis('off'), plt.title("ksize=11, sigma=20")
plt.imshow(cv2.cvtColor(imgGaussBlur2, cv2.COLOR_BGR2RGB))
plt.tight_layout()
plt.show()
