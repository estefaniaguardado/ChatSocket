#!/usr/bin/python

import Client
import sys
import socket

if __name__ == "__main__":
    argumentos = sys.argv
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
    Client.sendData(comando)
