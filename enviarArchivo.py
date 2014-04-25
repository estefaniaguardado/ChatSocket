

import sys
import datetime

import Client
import FileHandler

if __name__ == "__main__":
    argumentos = sys.argv
    fileName = argumentos[3]
    mensaje = {
        "accion" : "archivo",
        "usuario" : argumentos[1],
        "informacionMsj" : {
            "horaFecha" : str(datetime.datetime.now()),
            "mensaje" : fileName,
            "archivo": FileHandler.archivoAString(fileName)
        }
    }

    print Client.sendData(mensaje)