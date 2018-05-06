# -*- coding: utf-8 -*-

"""
The ImageGrabber class can grab frame in video from FFServer video stream.
"""
import cv2


class ImageGrabber:

    def __init__(self, video_path):
        """
        从指定的FFServer读取视频帧
        :param video_path: 视频路劲
        """
        self.__video_capture = cv2.VideoCapture(video_path)
        if not self.__video_capture.isOpened():
            raise RuntimeError("{} can not be opened".format(video_path))

    def grab(self):
        val, frame = self.__video_capture.read()
        return val, frame

