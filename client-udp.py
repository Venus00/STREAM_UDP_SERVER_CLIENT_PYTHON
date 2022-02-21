import socket
import cv2 
import base64
import sys
serverAddressPort = ("localhost", 2222)


while True : 
    vid = cv2.VideoCapture(0)
    while True : 

        ret, frame = vid.read()
        retval, buffer_img= cv2.imencode('.jpg', frame)
        #data = base64.b64encode(buffer_img)
        
        # encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
        # result, encimg = cv2.imencode('.jpg', frame, encode_param)
        #print(len(encimg))
        #bytesToSend = str.encode()
        # Create a UDP socket at client side
        frame = cv2.resize(frame, (320, 240), interpolation=cv2.INTER_AREA)
        print(sys.getsizeof(frame))
        retval, buffer_img= cv2.imencode('.jpg', frame)
        data = base64.encodestring(buffer_img)
        UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        # Send to server using created UDP socket
        UDPClientSocket.sendto(data, serverAddressPort)
        #msgFromServer = UDPClientSocket.recvfrom(bufferSize)
        #msg = "Message from Server {}".format(msgFromServer[0])
        #print(msg)
