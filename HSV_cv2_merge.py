import cv2
import numpy as np
import matplotlib.pyplot as plt
# 1.21 图像通道的合并
hImg = cv2.imread(r'C:\Users\hxb971002\Pictures\merge\hImg.png',flags=0)
sImg = cv2.imread(r'C:\Users\hxb971002\Pictures\merge\sImg.png',flags=0)
vImg = cv2.imread(r'C:\Users\hxb971002\Pictures\merge\vImg.png',flags=0)
# cv2.merge 实现图像通道的合并
imgMerge = cv2.merge([hImg, sImg, vImg])
cv2.imshow("cv2Merge", imgMerge)

cv2.waitKey(0)
cv2.destroyAllWindows()  # 释放所有窗口
