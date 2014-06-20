#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import json

targetIP = ""
targetPort = 0

def sendData(data, serverIP='127.0.0.1', serverPort=13373):
    if targetPort > 0:
        serverPort = targetPort
    if targetIP != "":
        serverIP = targetIP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((serverIP, serverPort))
    str_unicode = json.dumps(data) + "\0"
    s.sendall(str_unicode)
    data = ""
    while True:
        request_recv = s.recv(1)
        if request_recv == "\0":
            break
        else:
            data += request_recv
    result = json.loads(data)
    s.close()
    return result