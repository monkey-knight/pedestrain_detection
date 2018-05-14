# -*- coding: utf-8 -*-

import threading
from detection.image_grabber import ImageGrabber
from detection.pedestrian_detection import PedestrianDetection
import os
import cv2
from kafka_commucation.producer import TempProducer

# 读取视频的间隔帧数
INTERVAL_FRAME = 12


class MyThread(threading.Thread):

    def __init__(self, video_path, kafka_bootstrap_server, kafka_topic):
        threading.Thread.__init__(self)
        self.__image_grabber = ImageGrabber(video_path)
        self.__pedestrian_detection = PedestrianDetection()
        self.__producer = TempProducer(kafka_bootstrap_server, kafka_topic)

    def run(self):
        val = True
        number = 0
        count = 0
        while val:
            val, frame = self.__image_grabber.grab()
            count += 1
            if count % INTERVAL_FRAME == 0:
                # 每间隔INTERVAL_FRAME帧图片做一次检测
                frame = self.__pedestrian_detection.detect(frame)
                print(type(frame))
                count = 0
                number += 1
                self.__producer.p_cpmsg(frame, str(number)+".jpg")


if __name__ == '__main__':
    # rtsp (real time streaming protocol)
    camera1_video_path = "rtsp://localhost:7001/test"
    camera2_video_path = "rtsp://localhost:7002/test"
    camera3_video_path = "rtsp://localhost:7003/test"
    camera4_video_path = "rtsp://localhost:7004/test"

    kafka_bootstrap_server = "localhost:9092"
    camera1_topic = "camera1"
    camera2_topic = "camera2"
    camera3_topic = "camera3"
    camera4_topic = "camera4"

    camera1 = MyThread(camera1_video_path, kafka_bootstrap_server, camera1_topic)
    camera2 = MyThread(camera2_video_path, kafka_bootstrap_server, camera2_topic)
    camera3 = MyThread(camera3_video_path, kafka_bootstrap_server, camera3_topic)
    camera4 = MyThread(camera4_video_path, kafka_bootstrap_server, camera4_topic)

    camera1.start()
    camera2.start()
    camera3.start()
    camera4.start()
