from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit, send
from flask_cors import CORS
import cv2
import base64
import time
app = Flask(__name__)
app.config['SECRET_KEY'] = 'justasecretkeythatishouldputhere'

socketio = SocketIO(app, cors_allowed_origins="http://localhost:3000", logger=True, engineio_logger=True)
CORS(app)

@socketio.on('connect')
def on_connect(auth):
    print("CONNECTED")

@socketio.on("live")
def live(test):
    cap = cv2.VideoCapture(0)
    counter  = 0
    for _ in range(30):
        counter += 1
        ret,frame = cap.read()
        retval, buffer = cv2.imencode('.jpg', frame)
        send(f"Hi, {counter}")
        time.sleep(1)


if __name__ == '__main__':
    socketio.run(app)