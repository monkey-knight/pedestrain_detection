# -*- coding: utf-8 -*-
import time
from base_camera1 import BaseCamera
import os
from kafka_commucation.consumer import TempConsumer


class Camera1(BaseCamera):
    consumer = TempConsumer("group_id", "localhost:9092", "camera1")

    @staticmethod
    def frames():
        while True:
            yield Camera1.consumer.getonemsg()
            time.sleep(0.1)
