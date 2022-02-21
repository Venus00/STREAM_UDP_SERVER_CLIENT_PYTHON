import socket
import cv2
import base64
import codecs
import numpy as np
import sys
localIP     = "localhost"
localPort   = 2222
bufferSize  = 1000000

serverAddressPort = ("192.168.10.81", 2222)

face_cascade = cv2.CascadeClassifier('file.xml')

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")
# Listen for incoming datagrams
while(True):

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientIP  = "Client IP Address:{}".format(address)
    #print(message)
    #frame = base64.decodebytes(message)

    nparr = np.frombuffer(base64.b64decode(message), np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    # print(clientIP)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    ##send to server
    #retval, buffer_img= cv2.imencode('.png', frame)
    ret , image  = cv2.imencode('.jpg', frame)
    data = base64.b64encode( image)
    print(sys.getsizeof(data))

    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    # Send to server using created UDP socket
    UDPClientSocket.sendto(data, serverAddressPort)
    # Sending a reply to client
    #UDPServerSocket.sendto(bytesToSend, address)