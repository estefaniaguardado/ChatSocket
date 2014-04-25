#!/usr/bin/python

import Client
import sys
import datetime

if __name__ == "__main__":
    argumentos = sys.argv
    mensaje = {
        "accion" : "recibir",
        "usuario" : argumentos[1]
    }
    Client.sendData(mensaje)
