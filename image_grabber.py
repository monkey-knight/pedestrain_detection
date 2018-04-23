# -*- coding: utf-8 -*-

"""
The ImageGrabber class can grab frame in video from FFServer video stream.
"""
import cv2


class ImageGrabber:

    def __init__(self, video_path):
        self.__video_capture = cv2.VideoCapture(video_path)

    def grab(self):
        _, image = self.__video_capture.read()
        return image

