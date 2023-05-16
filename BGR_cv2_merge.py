import cv2
import numpy as np
import matplotlib.pyplot as plt
# 1.21 图像通道的合并
bImg = cv2.imread(r'C:\Users\hxb971002\Pictures\merge\bImg.png',flags=0)
gImg = cv2.imread(r'C:\Users\hxb971002\Pictures\merge\gImg.png',flags=0)
rImg = cv2.imread(r'C:\Users\hxb971002\Pictures\merge\rImg.png',flags=0)
# cv2.merge 实现图像通道的合并
imgMerge = cv2.merge([bImg, gImg, rImg])
cv2.imshow("cv2_merge", imgMerge)

cv2.waitKey(0)
cv2.destroyAllWindows()  # 释放所有窗口
