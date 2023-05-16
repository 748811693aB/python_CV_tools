import cv2
import numpy as np
import matplotlib.pyplot as plt
# 1.21 图像通道的合并
bImg = cv2.imread(r'C:\Users\hxb971002\Pictures\merge\bImg.png',flags=0)
gImg = cv2.imread(r'C:\Users\hxb971002\Pictures\merge\gImg.png',flags=0)
rImg = cv2.imread(r'C:\Users\hxb971002\Pictures\merge\rImg.png',flags=0)

# Numpy 拼接实现图像通道的合并
imgStack = np.stack((bImg, gImg, rImg), axis=2)
cv2.imshow("npStack", imgStack)



cv2.waitKey(0)
cv2.destroyAllWindows()  # 释放所有窗口
