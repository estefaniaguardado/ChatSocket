#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import datetime

import Client
import FileHandler

def main(argumentos):
    usuarioDestino = argumentos[1]
    nombreArchivo = argumentos[2]
    if os.path.isfile(nombreArchivo):
        mensaje = {
            "accion" : "archivo",
            "usuario" : usuarioDestino,
            "informacionMsj" : {
                "horaFecha" : str(datetime.datetime.now()),
                "mensaje" : os.path.basename(nombreArchivo),
                "archivo": FileHandler.archivoAString(nombreArchivo)
            }
        }

        return Client.sendData(mensaje)

    raise Exception("Archivo no existe o inválido: " + nombreArchivo)

if __name__ == "__main__":
    print main(sys.argv)