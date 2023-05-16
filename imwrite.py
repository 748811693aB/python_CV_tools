import cv2 
imgFile = "Lenna.png"  # 读取文件的路径
img3 = cv2.imread(imgFile, flags=1)  # flags=1 读取彩色图像(BGR)
saveFile = "./imgSave.png"  # 保存文件的路径
cv2.imwrite(saveFile, img3)  # 保存图像文件
