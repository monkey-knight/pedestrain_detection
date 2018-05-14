# -*- coding: utf-8 -*-
import time
from base_camera3 import BaseCamera
import os
from kafka_commucation.consumer import TempConsumer


class Camera3(BaseCamera):
    consumer = TempConsumer("group_id", "localhost:9092", "camera3")

    @staticmethod
    def frames():
        while True:
            yield Camera3.consumer.getonemsg()
            time.sleep(0.1)
