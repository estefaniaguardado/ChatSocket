#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime

class ActionHandler(object):

    def __init__(self):
        super(ActionHandler, self).__init__()
        self.informacionPersistida = {}
        self.mensajeEnviado = {}
        self.mensajeRecibido = {}

    def procesaAccion(self, modelDeDatos):
        if modelDeDatos["accion"] == "actualizar":
            identificador = modelDeDatos["identificador"]
            informacion = modelDeDatos["informacion"]
            self.informacionPersistida[identificador] = informacion
            return {"status" : "ok"}
        else:
            return {"status" : "ok", "informacion" : self.informacionPersistida}

    def mandarMensaje(self, Mensaje):
        if Mensaje["accion"] == "enviar":
            destinatario = Mensaje["destinatario"]
            informacionMsj = Mensaje["informacionMsj"]
            self.mensajeEnviado["destinatario"] = informacionMsj
            return {"status" : "ok"}
        else:
            return {"status" : "ok", "informacionMsj" : self.mensajeEnviado}

    def recibirMensajes(self, detalle_Mensaje):
        if detalle_Mensaje["accion"] == "recibir":
            remitente = detalle_Mensaje["remitente"]
            detalleMsj = detalle_Mensaje["detalleMsj"]
            self.mensajeRecibido["remitente"] = detalleMsj
            return {"status" : "ok"}
        else:
            return {"status" : "ok"}

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

    enviarMensaje = {
        "accion" : "enviar",
        "destinatario" : "Luis",
        "informacionMsj" : {
            "horaFecha" : datetime.datetime.now(),
            "mensaje" : []
        }
    }

    detalleMensaje = {
        "accion" : "recibir",
        "remitente" : "Fanny",
        "detalleMsj" : {
            "horaFecha" : datetime.datetime.now(),
            "mensaje" : []
        }
    }

    actionHandler = ActionHandler()

    # Ejemplo Actualizar
    respuesta = actionHandler.procesaAccion(modelDeDatosActualizar)
    if respuesta["status"] == "ok":
        print "Correcto almacenamiento"
    else:
        print "Incorrecto almacenamiento"

    # Ejemplo Listar con un elemento
    respuesta_listado = actionHandler.procesaAccion(modelDeDatosListar)
    if respuesta_listado["status"] == "ok":
        informacion_listado = respuesta_listado["informacion"]
        if len(informacion_listado) == 1 and informacion_listado["1"]["usuario"] == "Fanny":
            print "Correcto listado"
        else:
            print "Incorrecto listado"
    else:
        print "Incorrecto listado"

    #Ejemplo Enviado
    respuesta_enviado = actionHandler.mandarMensaje(enviarMensaje)
    if respuesta_enviado["status"] == "ok":
        print "Enviado correctamente"
    else:
        print "Fallo en el envio"

    #Ejemplo Recibido
    respuesta_recibido = actionHandler.recibirMensajes(detalleMensaje)
    if respuesta_recibido["status"] == "ok":
        print "Recibido"
    else:
        print "None"
