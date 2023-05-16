import cv2
import numpy as np
import matplotlib.pyplot as plt
# 1.21 图像通道的合并
hImg = cv2.imread(r'C:\Users\hxb971002\Pictures\merge\HSV\hImg.png',flags=0)
sImg = cv2.imread(r'C:\Users\hxb971002\Pictures\merge\HSV\sImg.png',flags=0)
vImg = cv2.imread(r'C:\Users\hxb971002\Pictures\merge\HSV\vImg.png',flags=0)

# Numpy 拼接实现图像通道的合并
imgStack = np.stack((hImg, sImg, vImg), axis=2)
cv2.imshow("npStack", imgStack)

cv2.waitKey(0)
cv2.destroyAllWindows()  # 释放所有窗口
