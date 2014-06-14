#!/usr/bin/python
# -*- coding: utf-8 -*-

import Client
import sys
import FileHandler

def main(argumentos):
    mensaje = {
        "accion" : "recibir",
        "usuario" : argumentos[1]
    }
    result = Client.sendData(mensaje)
    for mensaje in result["recibidoMsj"]:
        textoMensaje = mensaje["mensaje"]
        if "archivo" in mensaje:
            contenidoArchivo = mensaje["archivo"]
            FileHandler.stringAArchivo(textoMensaje, contenidoArchivo)
            return textoMensaje, True
        else:
            return textoMensaje, False

if __name__ == "__main__":
    argumentos = sys.argv
    mensaje, archivo = main(argumentos)
    if archivo:
        print "Archivo: " + mensaje
    else:
        print "> " + mensaje