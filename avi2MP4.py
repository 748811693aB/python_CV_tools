# !/usr/bin/env python
# -*-coding:utf-8-*-
import time
import cv2


def Video2Mp4(videoPath, outVideoPath):
    capture = cv2.VideoCapture(videoPath)
    fps = capture.get(cv2.CAP_PROP_FPS)  # 获取帧率
    size = (int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    # fNUMS = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    suc = capture.isOpened()  # 是否成功打开

    allFrame = []
    while suc:
        suc, frame = capture.read()
        if suc:
            allFrame.append(frame)
    capture.release()

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    videoWriter = cv2.VideoWriter(outVideoPath, fourcc, fps, size)
    for aFrame in allFrame:
        videoWriter.write(aFrame)
    videoWriter.release()


if __name__ == '__main__':
    inputVideoPath = "lane_video.avi"  # 读取视频路径
    outVideoPath = f"out_{int(time.time())}.mp4"
    Video2Mp4(inputVideoPath, outVideoPath)

