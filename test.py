from re import A
import numpy as np
import cv2
img=cv2.imread('Lenna.png',cv2.IMREAD_UNCHANGED,) #此处输入图片文件名
cv2.namedWindow('img',cv2.WINDOW_AUTOSIZE)
cv2.imshow('img',img)
GRAY = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('GRAY',GRAY)
cv2.waitKey(0)
