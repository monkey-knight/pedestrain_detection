# -*- coding: utf-8 -*-
import time
from base_camera2 import BaseCamera
import os


class Camera2(BaseCamera):
    input_path = '/home/monkeyknight/Pictures/pedestrian/camera2'
    images = []

    @staticmethod
    def frames():
        for file in os.listdir(Camera2.input_path):
            Camera2.images.append(open(os.path.join(Camera2.input_path, file), 'rb').read())

        length = len(Camera2.images)
        while True:
            time.sleep(0.1)
            yield Camera2.images[int(time.time()) % length]
