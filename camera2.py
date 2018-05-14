# -*- coding: utf-8 -*-
import time
from base_camera2 import BaseCamera
import os
from kafka_commucation.consumer import TempConsumer


class Camera2(BaseCamera):
    consumer = TempConsumer("group_id", "localhost:9092", "camera2")

    @staticmethod
    def frames():
        while True:
            yield Camera2.consumer.getonemsg()
            time.sleep(0.1)
