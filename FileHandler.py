#!/usr/bin/python
# -*- coding: utf-8 -*-

import base64
import os

def archivoAString(file, toBase64 = True):
    fin = open(file, "rb")
    bynary_data = fin.read()
    fin.close()
    return base64.b64encode(bynary_data) if toBase64 else bynary_data

def stringAArchivo(nombreArchivo, contenidoArchivo, toBase64 = True):
    directorio = os.path.dirname(nombreArchivo)
    if len(directorio) > 0 and os.path.exists(directorio) == False:
        os.makedirs(directorio)
    fout = open(nombreArchivo, "wb")
    fout.write(base64.b64decode(contenidoArchivo) if toBase64 else contenidoArchivo)
    fout.close()

if __name__ == "__main__":
    archivo = "FileHandler.py"
    stringDeArchivo = archivoAString(archivo)
    stringAArchivo("Prueba.py",  stringDeArchivo)
    stringDeArchivoResultado = archivoAString("Prueba.py")
    if stringDeArchivo == stringDeArchivoResultado:
        print "Lectura correcta de archivos"
    else:
        raise Exception("Archivos no guardados correctamente")


def existeArchivo(archivo):
    return os.path.exists(archivo)