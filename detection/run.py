# -*- coding: utf-8 -*-

import threading
from detection.image_grabber import ImageGrabber
from detection.pedestrian_detection import PedestrianDetection
import os
import cv2

# 读取视频的间隔帧数
INTERVAL_FRAME = 12


class MyThread(threading.Thread):

    def __init__(self, video_path, output_path):
        threading.Thread.__init__(self)
        self.__image_grabber = ImageGrabber(video_path)
        self.__pedestrian_detection = PedestrianDetection()
        self.__output_path = output_path

    def run(self):
        val = True
        count = 0
        number = 0
        while val:
            val, frame = self.__image_grabber.grab()
            count += 1
            if count % INTERVAL_FRAME == 0:
                # 每间隔INTERVAL_FRAME帧图片做一次检测
                frame = self.__pedestrian_detection.detect(frame)
                count = 0
                number += 1
                file_path = os.path.join(self.__output_path, str(number) + ".jpg")
                """
                cv2.imwrite(file, image)的使用注意：
                file是一个字符串路径，不能是一个pathLib object
                """
                cv2.imwrite(file_path, frame)


if __name__ == '__main__':
    # rtsp (real time streaming protocol)
    camera1_video_path = "rtsp://localhost:7001/test"
    camera2_video_path = "rtsp://localhost:7002/test"
    camera3_video_path = "rtsp://localhost:7003/test"
    camera4_video_path = "rtsp://localhost:7004/test"

    camera1_output_path = "/home/monkeyknight/Pictures/pedestrian/camera1"
    camera2_output_path = "/home/monkeyknight/Pictures/pedestrian/camera2"
    camera3_output_path = "/home/monkeyknight/Pictures/pedestrian/camera3"
    camera4_output_path = "/home/monkeyknight/Pictures/pedestrian/camera4"

    camera1 = MyThread(camera1_video_path, camera1_output_path)
    camera2 = MyThread(camera2_video_path, camera2_output_path)
    camera3 = MyThread(camera3_video_path, camera3_output_path)
    camera4 = MyThread(camera4_video_path, camera4_output_path)

    camera1.start()
    camera2.start()
    camera3.start()
    camera4.start()
