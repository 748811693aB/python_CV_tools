import cv2
import numpy as np
import matplotlib.pyplot as plt

rho = 1  # 霍夫变换参数
theta = np.pi / 180
threshold = 15

min_line_len = 20  # 线的最小长度
max_line_gap = 40  # 线段之间最大允许间隙
slope_threshold_min = 0.2  # 斜率检测参数
slope_threshold_max = 10
distance_threshold = 5  # 间距参数
exc_time = [-1.0, -1.0]

H_min = 22  # HSV提取
H_max = 74
S_min = 100
S_max = 255
V_min = 0
V_max = 255

input_cv_img = cv2.imread("deep-learn.jpg", flags=1)
gs_frame = cv2.GaussianBlur(input_cv_img, (3, 3), 0)  # 高斯模糊
hsv_image = cv2.cvtColor(gs_frame, cv2.COLOR_BGR2HSV)

colorLow = np.array([H_min, S_min, V_min])
colorHigh = np.array([H_max, S_max, V_max])
frame_binary = cv2.inRange(hsv_image, colorLow, colorHigh)  # 图像二值化

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))  # 创建膨胀腐蚀核并进行膨胀腐蚀
frame_binary_DE = cv2.dilate(frame_binary, kernel, iterations=1) #膨胀操作
roi_edges = cv2.erode(frame_binary_DE, kernel,iterations=2) #腐蚀操作
lines = cv2.HoughLinesP(roi_edges, rho, theta, threshold, minLineLength=min_line_len, maxLineGap=max_line_gap)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(roi_edges, (x1,y1), (x2,y2), (100,0,0), 1)  # 绘制直线
    
cv2.imshow('imgEdge',roi_edges)
cv2.waitKey(0)
cv2.destroyAllWindows()  # 释放所有窗口