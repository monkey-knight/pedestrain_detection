# -*- coding: utf-8 -*-

import cv2
from image_grabber import ImageGrabber

if __name__ == '__main__':
    video_path = "rtsp://192.168.41.130:7000/test"
    image_grabber = ImageGrabber(video_path)
    while True:
        frame = image_grabber.grab()
        cv2.imshow('VIDEO', frame)
        cv2.waitKey(1)
