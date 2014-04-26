#!/usr/bin/python
# -*- coding: utf-8 -*-

import base64
import datetime
import

def archivoAString(file):
    '''fin = open(file, "rb")
    bynary_data = fin.read()
    fin.close()
    return base64.b64encode(bynary_data)'''
    return "XXX"

def stringAArchivo(nombreArchivo, contenidoArchivo):
    b64_fname = nombreArchivo + "_b64.txt"
    fout = open(b64_fname, "w")
    fout.write(contenidoArchivo)
    fout.close()
    fin = open(b64_fname, 'r')
    b64_str = fin.read()
    fin.close()
    return base64.b64decode(b64_str)

if __name__ == "__main__":

    mensajeSencillo = {
        "accion" : "enviar",
        "usuario" : "Fanny",
        "informacionMsj" : {
            "horaFecha" : str(datetime.datetime.now()),
            "mensaje" : "hola"
        }
    }

    fileName = hola.tx
    mensajeArchivo = {
        "accion" : "archivo",
        "usuario" : "Fanny",
        "informacionMsj" : {
            "horaFecha" : str(datetime.datetime.now()),
            "mensaje" : "te envio un archivo",
            "archivo": archivoAString(hola.tx)
        }
    }