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
            "horaFecha" : str(datetime.datetime.now()),
            "mensaje" : argumentos[2]
        }
    }
    print Client.sendData(mensaje)
