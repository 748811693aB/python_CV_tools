import cv2
import numpy as np
# 1.19 图像拆分通道
img1 = cv2.imread("Lenna.png", flags=1)  # flags=1 读取彩色图像(BGR)
cv2.imshow("BGR", img1)  # BGR 图像

# BGR 通道拆分
bImg, gImg, rImg = cv2.split(img1)  # 拆分为 BGR 独立通道
cv2.imshow("rImg", rImg)  # 直接显示红色分量 rImg 显示为灰度图像
cv2.imshow("gImg", gImg)
cv2.imshow("bImg", bImg)
# 将单通道扩展为三通道
img_red = np.zeros_like(img1)  # 创建与 img1 相同形状的黑色图像
img_red[:,:,2] = rImg  # 在黑色图像模板添加红色分量 rImg
cv2.imshow("channel R", img_red)  # 扩展为 BGR 通道

img_blue = np.zeros_like(img1)  
img_blue[:,:,0] = bImg  
cv2.imshow("channel B", img_blue)  

img_green = np.zeros_like(img1)  
img_green[:,:,1] = gImg  
cv2.imshow("channel G", img_green)  

print(img1.shape, rImg.shape, img_red.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()  # 释放所有窗口
