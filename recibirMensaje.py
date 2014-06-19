#!/usr/bin/python
# -*- coding: utf-8 -*-

import Client
import sys
import FileHandler

def main(argumentos):
    mensaje = {
        "accion" : "recibir",
        "identificador" : argumentos[1],
        "llavePrivada" : argumentos[2]
    }
    result = Client.sendData(mensaje)
    mensajes = result["recibidoMsj"]
    if mensajes is not None and len(mensajes):
        for mensaje in mensajes:
            textoMensaje = mensaje["mensaje"]
            if "archivo" in mensaje:
                contenidoArchivo = mensaje["archivo"]
                FileHandler.stringAArchivo(textoMensaje, contenidoArchivo)
                return textoMensaje, True
            else:
                return textoMensaje, False

if __name__ == "__main__":
    mensaje, archivo = main(sys.argv)
    if archivo:
        print "Archivo: " + mensaje
    else:
        print "> " + mensaje