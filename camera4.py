# -*- coding: utf-8 -*-
import time
from base_camera4 import BaseCamera
import os


class Camera4(BaseCamera):
    input_path = '/home/monkeyknight/Pictures/pedestrian/camera4'
    images = []

    @staticmethod
    def frames():
        for file in os.listdir(Camera4.input_path):
            Camera4.images.append(open(os.path.join(Camera4.input_path, file), 'rb').read())

        length = len(Camera4.images)
        while True:
            time.sleep(0.1)
            yield Camera4.images[int(time.time()) % length]
