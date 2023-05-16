import cv2 
import numpy as np

frame_binary=cv2.imread("HSV_inRange.jpg",flags=1)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))  # 创建膨胀腐蚀核并进行膨胀腐蚀
frame_binary_DE = cv2.dilate(frame_binary, kernel, iterations=1)
roi_edges = cv2.erode(frame_binary_DE, kernel,iterations=2)
cv2.imshow("roi_edges.jpg",roi_edges)
cv2.imwrite("roi_edges.jpg",roi_edges)
cv2.waitKey(0)
cv2.destroyAllWindows()  # 释放所有窗口