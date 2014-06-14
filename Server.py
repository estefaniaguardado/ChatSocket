#!/usr/bin/python
# -*- coding: utf-8 -*-

import SocketServer
import json
from ActionHandler import ActionHandler

actionHandler = ActionHandler()

class MyTCPServer(SocketServer.ThreadingTCPServer):
    allow_reuse_address = True

class MyTCPServerHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        try:
            data = json.loads(self.request.recv(1024).strip())
            response = actionHandler.procesaAccion(data)
            self.request.sendall(json.dumps(response))
        except Exception, e:
            print "Exception while receiving message: ", e

server = None
def main(serverIP, serverPort):
    server = MyTCPServer((serverIP, serverPort), MyTCPServerHandler)
    server.serve_forever()


if __name__ == "__main__":
    main('127.0.0.1', 13373);