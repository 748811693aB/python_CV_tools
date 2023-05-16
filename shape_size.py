import cv2 
imgFile = "Lenna.png"  # 读取文件的路径
img1 = cv2.imread(imgFile, flags=1)  # flags=1 读取彩色图像(BGR)
img2 = cv2.imread(imgFile, flags=0)  # flags=0 读取为灰度图像

print("Ndim of img1(BGR): {}, img2(Gray): {}".format(img1.ndim, img2.ndim))  # number of rows, columns and channels
print("Shape of img1(BGR): {}, img2(Gray): {}".format(img1.shape, img2.shape))  # number of rows, columns and channels
print("Size of img1(BGR): {}, img2(Gray): {}".format(img1.size, img2.size))  # size = rows * columns * channels
print("Dtype of img1(BGR): {}, img2(Gray): {}".format(img1.dtype, img2.dtype))  # uint8
