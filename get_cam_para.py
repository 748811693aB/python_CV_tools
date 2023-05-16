import cv2
capture = cv2.VideoCapture(0)
width, height = capture.get(3), capture.get(4)
print(width, height)