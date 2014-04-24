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
        if modelDeDatos["accion"] == "enviar":
            return self.mandarMensaje(modelDeDatos)
        if modelDeDatos["accion"] == "recibir":
            return self.recibirMensaje(modelDeDatos)
        else:
            return {"status" : "ok",
                    "informacion" : self.informacionPersistida,
                    "informacionMsj" : self.mensajeEnviado,
                    "obtenidoMsj" : self.mensajeRecibido}

    def mandarMensaje(self, modelDeDatos):
        destinatario = modelDeDatos["destinatario"]
        mensaje = modelDeDatos["informacionMsj"]["mensaje"]
        horaFecha = modelDeDatos["informacionMsj"]["horaFecha"]
        self.mensajeEnviado["destinatario"] = destinatario + mensaje + horaFecha
        return {"status" : "ok"}

    def recibirMensaje(self, modelDeDatos):
        remitente = modelDeDatos["remitente"]
        mensaje = modelDeDatos["obtenidoMsj"]["mensaje"]
        horaFecha = modelDeDatos["obtenidoMsj"]["mensaje"]
        self.mensajeRecibido["remitente"] = remitente + mensaje + horaFecha
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
            "mensaje" : "xxx"
        }
    }

    mensajeObtenido = {
        "accion" : "recibir",
        "remitente" : "Fanny",
        "obtenidoMsj" : {
            "horaFecha" : datetime.datetime.now(),
            "mensaje" : "xxx"
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
