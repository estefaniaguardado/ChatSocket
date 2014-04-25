#!/usr/bin/python
# -*- coding: utf-8 -*-

import Client

if __name__ == "__main__":
    comando = {"accion": "listar"}
    print Client.sendData(comando)
