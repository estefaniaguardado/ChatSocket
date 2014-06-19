#!/usr/bin/python
# -*- coding: utf-8 -*-

from Server import main as ClientServer

clientServer = ClientServer("127.0.0.1", 0)
IP, PORT = clientServer.server_address

if __name__ == "__main__":
    print "IP:", IP, " PORT: ", PORT
    clientServer.serve_forever()