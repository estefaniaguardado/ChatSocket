#!/usr/bin/python

import Client

if __name__ == "__main__":
    comando = {"accion": "listar"}
    print Client.sendData(comando)
