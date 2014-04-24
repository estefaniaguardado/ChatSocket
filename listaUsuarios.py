#!/usr/bin/python

import Client

if __name__ == "__main__":
    comando = {"accion": "listar"}
    Client.sendData(comando)
