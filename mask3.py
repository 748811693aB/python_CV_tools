import cv2
import numpy as np
import matplotlib.pyplot as plt
def process_an_image(img):
    # 2. 标记四个坐标点用于ROI截取
    points = np.array([[(0, 550), (331, 187), (557, 187), (921, 550)]])
    roi_edges = roi_mask(img, points)
    return  roi_edges
def roi_mask(img, corner_points):
    # 创建掩膜
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, corner_points, (255,255,255))
    masked_img = cv2.bitwise_and(img, mask)
    return masked_img
#  图像的加法 (掩模 mask)
img1 = cv2.imread("raw_road.png")  # 读取彩色图像(BGR)
cv2.imshow("raw_road.png", img1)  # 显示从 img1 提取的 ROI
img2 = process_an_image(img1)
cv2.imshow("MaskROI", img2)  # 显示从 img1 提取的 ROI
key = cv2.waitKey(0)  # 等待按键命令



