from os import kill
import socketio
import cv2
import base64
import threading 
import time

sio = socketio.Client()
killThread = False

@sio.event
def connect():
    print('connected to server')
    t1 = threading.Thread(target=send_frame, args=(0,))
    t1.start()


@sio.event
def disconnect():
    global killThread
    killThread = True
    print('disconnected from server')

def send_frame(index) : 
    global killThread
    vid = cv2.VideoCapture(index)
    vid.set(cv2.CAP_PROP_FPS, 15)
    while True : 
        if killThread == True : 
            return 
        ret, frame = vid.read()
        
        retval, buffer_img= cv2.imencode('.jpg', frame)
        data = base64.b64encode(buffer_img)
        sio.emit('StreamEvent',data)
        
        print("another frame has been sent")
        time.sleep(0.09)

if __name__ == '__main__':
    sio.connect('https://socket.nextronic.ddns.me')
    

