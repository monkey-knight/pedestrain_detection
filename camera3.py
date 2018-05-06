# -*- coding: utf-8 -*-
import time
from base_camera3 import BaseCamera
import os


class Camera3(BaseCamera):
    input_path = '/home/monkeyknight/Pictures/pedestrian/camera3'
    images = []

    @staticmethod
    def frames():
        for file in os.listdir(Camera3.input_path):
            Camera3.images.append(open(os.path.join(Camera3.input_path, file), 'rb').read())

        length = len(Camera3.images)
        while True:
            time.sleep(0.1)
            yield Camera3.images[int(time.time()) % length]
