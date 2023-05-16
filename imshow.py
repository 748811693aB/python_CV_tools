import cv2 
imgFile = "511.png"  # 读取文件的路径
img1 = cv2.imread(imgFile, flags=1)  # flags=1 读取彩色图像(BGR)
img2 = cv2.imread(imgFile, flags=0)  # flags=0 读取为灰度图像
cv2.imshow("T_road", img1)  # 在窗口 "Demo1" 显示图像 img1
cv2.imshow("Lenna_Gray", img2)  # 在窗口 "Demo2" 显示图像 img2
key = cv2.waitKey(0)  # 等待按键命令, 1000ms 后自动关闭
