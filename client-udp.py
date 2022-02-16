import socket
import cv2 
import base64
serverAddressPort = ("127.0.0.1", 20001)


while True : 
    vid = cv2.VideoCapture(0)
    while True : 

        ret, frame = vid.read()
        retval, buffer_img= cv2.imencode('.jpg', frame)
        data = base64.b64encode(buffer_img)


        #bytesToSend = str.encode()
        # Create a UDP socket at client side
        UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        # Send to server using created UDP socket
        UDPClientSocket.sendto(data, serverAddressPort)
        #msgFromServer = UDPClientSocket.recvfrom(bufferSize)
        #msg = "Message from Server {}".format(msgFromServer[0])
        #print(msg)
