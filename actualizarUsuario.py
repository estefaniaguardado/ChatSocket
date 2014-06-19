#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

import Client

def main(argumentos):
    comando = {
        "accion" : "actualizar",
        "identificador" : argumentos[1],
        "informacion" : {
            "status" : argumentos[2],
            "usuario" : argumentos[3],
            "IP" : argumentos[4],
            "puerto" : argumentos[5]
        }
    }
    return Client.sendData(comando)

if __name__ == "__main__":
    print main(sys.argv)