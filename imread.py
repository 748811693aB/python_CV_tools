import cv2 
import numpy as np
import matplotlib.pyplot as plt
import random
import math
shear = 50
perspective = 0.002
degrees = 20
scale=.1
translate=.1
hgain=0.5
sgain=0.5
vgain=0.5
imgFile = r"C:\Users\hxb971002\Desktop\CODE\5-20.jpg"  # 读取文件的路径
img1 = cv2.imread(imgFile, flags=1)  # flags=1 读取彩色图像(BGR)
img2 = cv2.imread(imgFile, flags=0)  # flags=0 读取为灰度图像

height = img1.shape[0]  # shape(h,w,c)
width = img1.shape[1]
'''
# Center
C = np.eye(3)
C[0, 2] = -img1.shape[1] / 2  # x translation (pixels) 第一行第三列
C[1, 2] = -img1.shape[0] / 2  # y translation (pixels) 第二行第三列
'''
'''
# Perspective
P = np.eye(3)
P[2, 0] = random.uniform(-perspective, perspective)  # x perspective (about y)
P[2, 1] = random.uniform(-perspective, perspective)  # y perspective (about x)
'''

'''
# Rotation and Scale
R = np.eye(3)
a = random.uniform(-degrees, degrees)
# a += random.choice([-180, -90, 0, 90])  # add 90deg rotations to small rotations
s = random.uniform(1 - scale, 1 + scale)
# s = 2 ** random.uniform(-scale, scale)
R[:2] = cv2.getRotationMatrix2D(angle=a, center=(0, 0), scale=s)
'''
'''
# shear
S = np.eye(3)
S[0, 1] = math.tan(random.uniform(-shear, shear) * math.pi / 180)  # x shear (deg)
S[1, 0] = math.tan(random.uniform(-shear, shear) * math.pi / 180)  # y shear (deg)
'''
'''
# Translation
T = np.eye(3)
T[0, 2] = random.uniform(0.5 - translate, 0.5 + translate) * width  # x translation (pixels)
T[1, 2] = random.uniform(0.5 - translate, 0.5 + translate) * height  # y translation (pixels)

'''
'''
# HSV
r = np.random.uniform(-1, 1, 3) * [hgain, sgain, vgain] + 1  # random gains
hue, sat, val = cv2.split(cv2.cvtColor(img1, cv2.COLOR_BGR2HSV))
dtype = img1.dtype  # uint8

x = np.arange(0, 256, dtype=r.dtype)
lut_hue = ((x * r[0]) % 180).astype(dtype)
lut_sat = np.clip(x * r[1], 0, 255).astype(dtype)
lut_val = np.clip(x * r[2], 0, 255).astype(dtype)

im_hsv = cv2.merge((cv2.LUT(hue, lut_hue), cv2.LUT(sat, lut_sat), cv2.LUT(val, lut_val)))
cv2.cvtColor(im_hsv, cv2.COLOR_HSV2BGR, dst=img1)  # no return needed
'''

#img = np.fliplr(img1)
#im = cv2.warpPerspective(img1, T, dsize=(width, height), borderValue=(114, 114, 114))


cv2.imshow('imgFile',img)
k = cv2.waitKey(0)