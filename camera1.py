# -*- coding: utf-8 -*-
import time
from base_camera1 import BaseCamera
import os


class Camera1(BaseCamera):
    input_path = '/home/monkeyknight/Pictures/pedestrian/camera1'
    images = []

    @staticmethod
    def frames():
        for file in os.listdir(Camera1.input_path):
            Camera1.images.append(open(os.path.join(Camera1.input_path, file), 'rb').read())

        length = len(Camera1.images)
        while True:
            time.sleep(0.1)
            yield Camera1.images[int(time.time()) % length]
