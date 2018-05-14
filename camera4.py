# -*- coding: utf-8 -*-
import time
from base_camera4 import BaseCamera
import os
from kafka_commucation.consumer import TempConsumer


class Camera4(BaseCamera):
    consumer = TempConsumer("group_id", "localhost:9092", "camera4")

    @staticmethod
    def frames():
        while True:
            yield Camera4.consumer.getonemsg()
            time.sleep(0.1)
