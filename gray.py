import cv2 
import numpy
# 1.1 图像的读取
imgFile = "Lenna.png"  # 读取文件的路径
img1 = cv2.imread(imgFile, flags=1)  # flags=1 读取彩色图像(BGR)
img2 = cv2.imread(imgFile, flags=0)  # flags=0 读取为灰度图像

# 1.10 图像显示(plt.imshow)
imgRGB = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)  # 图片格式转换：BGR(OpenCV) -> RGB(PyQt5)
imGray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)  # 图片格式转换：BGR(OpenCV) -> Gray    
cv2.imshow("imGray_2", imGray)  # 在窗口 "Demo1" 显示图像 img1
cv2.imshow("imGray_1", img2)  # 在窗口 "Demo2" 显示图像 img2
cv2.imshow("RGB", img1)
key = cv2.waitKey(0)  # 等待按键命令, 1000ms 后自动关闭