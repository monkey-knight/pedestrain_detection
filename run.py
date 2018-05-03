# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, url_for
import cv2
import os

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/video")
def video():
    images = []
    img_dir = "./static/images"
    for file in os.listdir(img_dir):
        image = img_dir + "/" + file
        images.append(image)
    return render_template("video.html", images=images)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
