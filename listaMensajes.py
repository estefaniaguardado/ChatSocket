#!/usr/bin/python
# -*- coding: utf-8 -*-

import Client

def main():
    comando = {"accion": "listarMensajes"}
    return Client.sendData(comando)

if __name__ == "__main__":
    print main()