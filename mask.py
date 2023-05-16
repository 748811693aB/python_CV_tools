import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1.27 图像的加法 (掩模 mask)
img1 = cv2.imread("lenna.png")  # 读取彩色图像(BGR)
img2 = cv2.imread("opencv.png")  # 读取彩色图像(BGR)

Mask = np.zeros((img1.shape[0], img1.shape[1]), dtype=np.uint8)  # 返回与图像 img1 尺寸相同的全零数组
xmin, ymin, w, h = 180, 190, 200, 200  # 矩形裁剪区域 (ymin:ymin+h, xmin:xmin+w) 的位置参数
Mask[ymin:ymin+h, xmin:xmin+w] = 255  # 掩模图像，ROI 为白色，其它区域为黑色
print(img1.shape, img2.shape, Mask.shape)

imgAddMask1 = cv2.add(img1, img2, mask=Mask)  # 带有掩模 mask 的加法
imgAddMask2 = cv2.add(img1, np.zeros(np.shape(img1), dtype=np.uint8), mask=Mask)  # 提取 ROI

cv2.imshow("MaskImage", Mask)  # 显示掩模图像 Mask
cv2.imshow("MaskAdd", imgAddMask1)  # 显示掩模加法结果 imgAddMask1
cv2.imshow("MaskROI", imgAddMask2)  # 显示从 img1 提取的 ROI
key = cv2.waitKey(0)  # 等待按键命令

