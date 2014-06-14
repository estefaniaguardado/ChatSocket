#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import json

def sendData(data, serverIP='127.0.0.1', serverPort=13373):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((serverIP, serverPort))
    s.send(json.dumps(data))
    result = json.loads(s.recv(1024))
    s.close()
    return result