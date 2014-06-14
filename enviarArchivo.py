#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import datetime

import Client
import FileHandler

def main(argumentos):
    fileName = argumentos[3]
    mensaje = {
        "accion" : "archivo",
        "usuario" : argumentos[1],
        "informacionMsj" : {
            "horaFecha" : str(datetime.datetime.now()),
            "mensaje" : fileName,
            "archivo": FileHandler.archivoAString(fileName)
        }
    }

    return Client.sendData(mensaje)

if __name__ == "__main__":
    print main(sys.argv)