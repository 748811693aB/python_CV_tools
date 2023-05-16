import cv2

im=cv2.imread("20160222_115224_mask.jpg")
size=im.shape
for i in range (size[0]):
    for j in range (size[1]):
        im[i,j]=im[i,j]*255

cv2.imwrite("saved.png",im)