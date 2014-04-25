#!/usr/bin/python
# -*- coding: utf-8 -*-

import Client
import sys
import FileHandler

if __name__ == "__main__":
    argumentos = sys.argv
    mensaje = {
        "accion" : "recibir",
        "usuario" : argumentos[1]
    }
    result = Client.sendData(mensaje)
    for mensaje in result["recibidoMsj"]:
        textoMensaje = mensaje["mensaje"]
        if "archivo" in mensaje:
            print "Guardado archivo:", textoMensaje
            contenidoArchivo = mensaje["archivo"]
            FileHandler.stringAArchivo(textoMensaje, contenidoArchivo)
        else:
            print textoMensaje