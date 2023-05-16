import cv2
capture = cv2.VideoCapture(1)
while(True):
    # 获取一帧
    #ret, frame = capture.read()
    frame = cv2.imread('raw_road.png')
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break
