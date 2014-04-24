import socket
import json

def sendData(data):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 13373))
    s.send(json.dumps(data))
    result = json.loads(s.recv(1024))
    print result
    s.close()

