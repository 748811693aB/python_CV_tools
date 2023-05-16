import cv2 
imgFile = "deep-learn.jpg"  # 读取文件的路径
img_BGR = cv2.imread(imgFile, flags=1)  # flags=1 读取彩色图像(BGR)
img_HSV = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2HSV)
cv2.imshow("img_BGR", img_BGR)  # 在窗口 "Demo1" 显示图像 img1
cv2.imshow("img_HSV", img_HSV)  # 在窗口 "Demo2" 显示图像 img2
cv2.imwrite("deep-learn-img_HSV.jpg", img_HSV)  
key = cv2.waitKey(0)  # 等待按键命令, 1000ms 后自动关闭
