#!/usr/bin/python
# -*- coding: utf-8 -*-

import Client

def main():
    comando = {"accion": "listarMensajes"}
    print Client.sendData(comando)

if __name__ == "__main__":
    main()