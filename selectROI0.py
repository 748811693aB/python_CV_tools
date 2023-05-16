import cv2
i = 0
img1 = cv2.imread(r"E:\209laboratory\6-6\model\badmintondatasets\images2\0.png", flags=1)  # flags=1 读取彩色图像(BGR)

xmin, ymin, w, h = 0, 0, 200, 200  # 矩形裁剪区域 (ymin:ymin+h, xmin:xmin+w) 的位置参数
imgCrop = img1[ymin:ymin+h, xmin:xmin+w].copy()  # 切片获得裁剪后保留的图像区域

cv2.imshow("DemoCrop", imgCrop)  # 在窗口显示 彩色随机图像
key = cv2.waitKey(0)  # 等待按键命令
