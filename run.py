# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, url_for, Response
from camera1 import Camera1
from camera2 import Camera2
from camera3 import Camera3
from camera4 import Camera4

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/cameras")
def cameras():
    return render_template("cameras.html")


def generate_camera1(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/camera1')
def camera1():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(generate_camera1(Camera1()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


def generate_camera2(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/camera2')
def camera2():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(generate_camera2(Camera2()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


def generate_camera3(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/camera3')
def camera3():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(generate_camera3(Camera3()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


def generate_camera4(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/camera4')
def camera4():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(generate_camera4(Camera4()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, threaded=True)
