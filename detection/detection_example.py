# -*- coding: utf-8 -*-

import cv2
from detection.pedestrian_detection import PedestrianDetection

if __name__ == '__main__':
    image_path = "/home/monkeyknight/Pictures/pedestrian/1.jpg"
    image = cv2.imread(image_path)
    pedestrian_detection = PedestrianDetection()
    image = pedestrian_detection.detect(image)
    cv2.imshow("pedestrian detection", image)
    cv2.waitKey(0)
