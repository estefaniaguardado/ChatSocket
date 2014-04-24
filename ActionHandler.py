#!/usr/bin/python
# -*- coding: utf-8 -*-

class ActionHandler(object):

    def __init__(self):
        super(ActionHandler, self).__init__()
        self.informacionPersistida = []

    def procesaAccion(self, modelDeDatos):
        if modelDeDatos["accion"] == "actualizar":
            self.informacionPersistida.append(modelDeDatos)
            return {"status" : "ok"}
        else:
            return {"status" : "ok", "informacion" : self.informacionPersistida}


if __name__ == "__main__":

    modelDeDatosActualizar = {
        "accion" : "actualizar",
        "identificador" : "1",
        "informacion" : {
            "status" : "online",
            "usuario" : "Fanny",
            "identificador" : "192.168.1.65",
            "puerto" : 13375
        }
    }

    modelDeDatosListar = {
        "accion" : "listar"
    }

    actionHandler = ActionHandler()

    # Ejemplo Actualizar
    respuesta = actionHandler.procesaAccion(modelDeDatosActualizar)
    if respuesta["status"] == "ok":
        print "Correcto"
    else:
        print "Incorrecto"

    # Ejemplo Listar con un elemento
    respuesta_listado = actionHandler.procesaAccion(modelDeDatosListar)
    if respuesta_listado["status"] == "ok":
        informacion_listado = respuesta_listado["informacion"]
        if len(informacion_listado) == 1 and informacion_listado[0]["identificador"] == "1":
            print "Correcto listado"
        else:
            print "Incorrecto listado"
    else:
        print "Incorrecto listado"
