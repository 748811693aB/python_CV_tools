import cv2 
import numpy as np
H_min = 22  # HSV提取
H_max = 100#74
S_min = 100
S_max = 255
V_min = 0
V_max = 255

colorLow = np.array([H_min, S_min, V_min])
colorHigh = np.array([H_max, S_max, V_max])
hsv_image = cv2.imread("turn.jpg", flags=1)  # flags=1 读取彩色图像(BGR)
frame_binary = cv2.inRange(hsv_image, colorLow, colorHigh)  # 图像二值化

cv2.imshow("cv2Merge", frame_binary)
cv2.imwrite("turn-HSV_inRange.jpg", frame_binary)
cv2.waitKey(0)
cv2.destroyAllWindows()  # 释放所有窗口
