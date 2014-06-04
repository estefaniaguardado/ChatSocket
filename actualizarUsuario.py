#!/usr/bin/python
# -*- coding: utf-8 -*-

import Client
import sys
import socket

def main(argumentos):
    comando = {
        "accion" : "actualizar",
        "identificador" : argumentos[1],
        "informacion" : {
            "status" : argumentos[2],
            "usuario" : argumentos[3],
            "identificador" : socket.gethostbyname(socket.gethostname()),
            "puerto" : argumentos[4]
        }
    }
    return Client.sendData(comando)

if __name__ == "__main__":
    print main(sys.argv)