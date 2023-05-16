import cv2
import numpy as np
import matplotlib.pyplot as plt
#  投影变换 (Projective mapping)
img = cv2.imread("raw_road.png")  # 读取彩色图像(BGR)
h, w = img.shape[:2]  # 图片的高度和宽度
pointSrc = np.float32([[376,198], [557,198], [77,547], [843, 533]])  # 原始图像中 4点坐标
pointDst = np.float32([[77,198], [843,198], [77,547], [843, 533]])  # 变换图像中 4点坐标
MP = cv2.getPerspectiveTransform(pointSrc, pointDst)  # 计算投影变换矩阵 M
imgP = cv2.warpPerspective(img, MP, (w, h))  # 用变换矩阵 M 进行投影变换
plt.figure(figsize=(9,6))
plt.subplot(121), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title("Original")
plt.subplot(122), plt.imshow(cv2.cvtColor(imgP, cv2.COLOR_BGR2RGB)), plt.title("Projective")
plt.show()
