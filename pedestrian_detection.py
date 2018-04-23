# -*- coding: utf-8 -*-

"""
PedestrianDetection class can detect pedestrian in image that
we want to detect pedestrians in.
"""
import cv2
import numpy as np
from imutils.object_detection import non_max_suppression


class PedestrianDetection:

    def __init__(self):
        # initialize the HOG (Histogram of Oriented Gradient) Descriptor.
        self.__hog = cv2.HOGDescriptor()
        # sets the SVM (Support Vector Machine) detector to be the default pedestrian
        # detector included with OpenCV.
        self.__hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    def detect(self, image, win_stride=(4, 4), padding=(8, 8), scale=1.05,
               overlap_threshold=0.65, line_color=(0, 255, 0), line_width=2):
        """
        detect pedestrian in image
        :param image:
        :param win_stride: the step size in the x and y direction of our sliding window
        :param padding: the amount of pixels the ROI is padded with prior to HOG feature vector extraction
        and SVM classification
        :param scale: the scale of the image pyramid (allowing us to detect people in images at multiple scales)
        :param overlap_threshold:
        :param line_color: the color of line to draw the rectangle containing person in image
        :param line_width: the width of line to draw the rectangle containing person in image
        :return:
        """
        (rectangles, weights) = self.__hog.detectMultiScale(image, winStride=win_stride, padding=padding, scale=scale)
        rectangles = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rectangles])
        pick = non_max_suppression(rectangles, probs=None, overlapThresh=overlap_threshold)
        for (x_min, y_min, x_max, y_max) in pick:
            cv2.rectangle(image, (x_min, y_min), (x_max, y_max), line_color, line_width)
        return image
