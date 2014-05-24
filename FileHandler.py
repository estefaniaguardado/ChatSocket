#!/usr/bin/python
# -*- coding: utf-8 -*-

import base64
import datetime


def archivoAString(file):
    fin = open(file, "rb")
    bynary_data = fin.read()
    fin.close()
    return base64.b64encode(bynary_data)

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
    archivo = "FileHandler.py"
    stringDeArchivo = archivoAString(archivo)
    stringAArchivo("Prueba.py",  stringDeArchivo)
    stringDeArchivoResultado = archivoAString("Prueba.py")
    if stringDeArchivo == stringDeArchivoResultado:
        print "Lectura correcta de archivos"
    else:
        raise Exception("Archivos no guardados correctamente")



