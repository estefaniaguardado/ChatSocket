#!/usr/bin/python
# -*- coding: utf-8 -*-

import SocketServer
import json
from ActionHandler import ActionHandler

class MyTCPServer(SocketServer.ThreadingTCPServer):
    allow_reuse_address = True

class MyTCPServerHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        try:
            data = ""
            while True:
                request_recv = self.request.recv(1)
                if request_recv == "\0":
                    break
                else:
                    data += request_recv
            data = json.loads(data)
            response = self.server.actionHandler.procesaAccion(data)
            self.request.sendall(json.dumps(response) + "\0")
        except Exception, e:
            print "Exception while receiving message: ", e

def main(serverIP, serverPort, handler = ActionHandler):
    newServer = MyTCPServer((serverIP, serverPort), MyTCPServerHandler)
    newServer.actionHandler = handler()
    return newServer

server = None
if __name__ == "__main__":
    server = main('127.0.0.1', 13373);
    server.serve_forever()