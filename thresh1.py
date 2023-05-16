import cv2 
import matplotlib.pyplot as plt
# 1.47 固定阈值二值变换
img = cv2.imread("Lenna.png")  # 读取彩色图像(BGR)
imgGray = cv2.imread("Lenna.png", flags=0)  # flags=0 读取为灰度图像
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 颜色转换：BGR(OpenCV) -> Gray

# cv2.threshold(src, thresh, maxval, type[, dst]) → retval, dst
ret1, img1 = cv2.threshold(imgGray, 64, 255, cv2.THRESH_BINARY)  # 转换为二值图像, thresh=64
ret2, img2 = cv2.threshold(imgGray, 128, 255, cv2.THRESH_BINARY)  # 转换为二值图像, thresh=128
ret3, img3 = cv2.threshold(imgGray, 192, 255, cv2.THRESH_BINARY)  # 转换为二值图像, thresh=192


plt.figure(figsize=(9, 6))
titleList = ["1. BINARY(thresh=64)", "2. BINARY(thresh=128)", "3. BINARY(thresh=192)"]
imageList = [img1, img2, img3]
for i in range(3):
    plt.subplot(1, 3, i+1), plt.title(titleList[i]), plt.axis('off')
    plt.imshow(imageList[i], 'gray')  # 灰度图像 ndim=2
plt.show()
