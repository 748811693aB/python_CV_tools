import cv2
img = cv2.imread("Lenna.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blocksize=11
C=-30
binary = cv2.adaptiveThreshold(gray, 150, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, blocksize, C)
cv2.imshow('thresh_adaptive', binary)
cv2.waitKey(0)
