import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Troad.png")  # 读取彩色图像(BGR)

height, width = img.shape[:2]  # 图片的高度和宽度
imgZoom1 = cv2.resize(img, (int(0.4*width), int(0.4*height)))
cv2.imwrite('Troad_small.png',imgZoom1)
#imgZoom2 = cv2.resize(img, None, fx=0.75, fy=1.0, interpolation=cv2.INTER_AREA)

plt.figure(figsize=(8,6))
plt.subplot(111), plt.axis('off'), plt.title("Zoom: 0.1*W,0.1*H")
plt.imshow(cv2.cvtColor(imgZoom1, cv2.COLOR_BGR2RGB))
plt.show()
