import cv2
capture = cv2.VideoCapture(1)
#capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 48)
#capture.set(cv2.CAP_PROP_FRAME_WIDTH, 64)
while(True):
    # 获取一帧
    ret, frame = capture.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break