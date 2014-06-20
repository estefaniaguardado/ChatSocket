#!/usr/bin/python
# -*- coding: utf-8 -*-

import Client
import sys
import FileHandler

def main(argumentos):
    mensaje = {
        "accion" : "recibir",
        "identificador" : argumentos[1],
        "llavePrivada" : argumentos[2],
        "participante" : argumentos[3] if len(argumentos) > 2 else ""
    }
    return Client.sendData(mensaje)

def procesaMensajesDeArchivo(mensajes):
    if mensajes is not None and len(mensajes):
        for mensaje in mensajes:
            textoMensaje = mensaje["mensaje"]
            if "archivo" in mensaje:
                contenidoArchivo = mensaje["archivo"]
                FileHandler.stringAArchivo(textoMensaje, contenidoArchivo)

if __name__ == "__main__":
    result = main(sys.argv)
    mensajes = result["recibidoMsj"]
    procesaMensajesDeArchivo(mensajes)
    print mensajes
