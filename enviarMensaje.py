#!/usr/bin/python
# -*- coding: utf-8 -*-

import Client
import sys
import datetime

def main(argumentos):
    mensaje = {
        "accion" : "enviar",
        "identificador" : argumentos[1],
        "informacionMsj" : {
            "horaFecha" : str(datetime.datetime.now()),
            "mensaje" : argumentos[2]
        }
    }
    return Client.sendData(mensaje)

if __name__ == "__main__":
    print main(sys.argv)