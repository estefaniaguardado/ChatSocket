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

        if modelDeDatos["accion"] == "listarMensajes":
            return {"status" : "ok",
                    "enviadoMsj" : self.mensajeEnviado}
                    #"obtenidoMsj" : self.mensajeRecibido}

        if modelDeDatos["accion"] == "recibir":
            return self.recibirMensaje(modelDeDatos)

        else:
            return {"status" : "ok",
                    "informacion" : self.informacionPersistida}




    def mandarMensaje(self, modelDeDatos):
        remitente = modelDeDatos["remitente"]
        mensaje = modelDeDatos["informacionMsj"]["mensaje"]
        horaFecha = modelDeDatos["informacionMsj"]["horaFecha"]
        informacionEnviada = {"mensaje" : mensaje, "horaFecha": horaFecha}
        self.mensajeEnviado[remitente] = informacionEnviada
        return {"status" : "ok", "enviadoMsj": self.mensajeEnviado}

    def recibirMensaje(self, modelDeDatos):
        destinatario = modelDeDatos["destinatario"]
        mensaje = modelDeDatos["obtenidoMsj"]["mensaje"]
        horaFecha = modelDeDatos["obtenidoMsj"]["mensaje"]
        informacionRecibida = {"mensaje" : mensaje, "horaFecha" : horaFecha}
        self.mensajeRecibido[destinatario] = informacionRecibida
        return {"status" : "ok", "recibidoMsj" : self.mensajeRecibido}

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

    modelDeDatosActualizar1 = {
        "accion" : "actualizar",
        "identificador" : "2",
        "informacion" : {
            "status" : "online",
            "usuario" : "Luis",
            "identificador" : "192.168.1.65",
            "puerto" : 13378
        }
    }

    modelDeDatosListar = {
        "accion" : "listar"
    }

    enviarMensajeF = {
        "accion" : "enviar",
        "remitente" : "Fanny",
        "informacionMsj" : {
            "horaFecha" : datetime.datetime.now(),
            "mensaje" : "hola, como estas"
        }
    }

    enviarMensajeL = {
        "accion" : "enviar",
        "remitente" : "Luis",
        "informacionMsj" : {
            "horaFecha" : datetime.datetime.now(),
            "mensaje" : "muy bien y tu?"
        }
    }

    mensajesLista = {
        "accion" : "listarMensajes"
    }

    mensajeObtenidoL = {
        "accion" : "recibir",
        "destinatario" : "Luis",
        "obtenidoMsj" : {
            "horaFecha" : datetime.datetime.now(),
            "mensaje" : "xxx"
        }
    }

    mensajeObtenidoF = {
        "accion" : "recibir",
        "destinatario" : "Fanny",
        "obtenidoMsj" : {
            "horaFecha" : datetime.datetime.now(),
            "mensaje" : "xxx"
        }
    }


    actionHandler = ActionHandler()

    # Ejemplo Actualizar
    respuesta = actionHandler.procesaAccion(modelDeDatosActualizar)
    print respuesta
    respuesta1 = actionHandler.procesaAccion(modelDeDatosActualizar1)
    print respuesta1
    if respuesta["status"] == "ok":
        print "Correcto almacenamiento"
    else:
        print "Incorrecto almacenamiento"

    # Ejemplo Listar con un elemento
    respuesta_listado = actionHandler.procesaAccion(modelDeDatosListar)
    if respuesta_listado["status"] == "ok":
        informacion_listado = respuesta_listado["informacion"]
        print informacion_listado
        if len(informacion_listado) == 1 and informacion_listado["1"]["usuario"] == "Fanny":
            print "Correcto listado Fanny"
        else:
            print "Incorrecto listado Fanny"
        if len(informacion_listado) == 2 and informacion_listado["2"]["usuario"] == "Luis":
            print "Correcto listado Luis"
        else:
            print "Incorrecto listado Luis"
    else:
        print "Incorrecto listado"

    #Ejemplo Enviado
    enviado_Fanny = actionHandler.mandarMensaje(enviarMensajeF)
    enviado_Luis = actionHandler.mandarMensaje(enviarMensajeL)
    if enviado_Fanny["status"] == "ok" and enviado_Luis["status"] == "ok":
        print "Enviado correctamente"
    else:
        print "Fallo en el envio"


    #Ejemplo de lista de mensajes enviados
    lista_enviados = actionHandler.procesaAccion(mensajesLista)
    if lista_enviados["status"] == "ok":
        print lista_enviados["enviadoMsj"]
    else:
        print "Fallo mensaje"

    #Ejemplo Recibido
    respuesta_recibido = actionHandler.recibirMensaje(mensajeObtenidoF)
    if respuesta_recibido["status"] == "ok":
        print "Recibido"
    else:
        print "None"
