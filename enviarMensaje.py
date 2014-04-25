#!/usr/bin/python

import Client
import sys
import datetime

if __name__ == "__main__":
    argumentos = sys.argv
    mensaje = {
        "accion" : "enviar",
        "usuario" : argumentos[1],
        "informacionMsj" : {
            "horaFecha" : datetime.datetime.now(),
            "mensaje" : argumentos[2]
        }
    }
    Client.sendData(mensaje)
