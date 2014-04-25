#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime

class ActionHandler(object):

    def __init__(self):
        super(ActionHandler, self).__init__()
        self.usuarios = {}
        self.mensajesPorUsuario = {}

    def procesaAccion(self, modelDeDatos):
        if modelDeDatos["accion"] == "actualizar":
            identificador = modelDeDatos["identificador"]
            informacion = modelDeDatos["informacion"]
            self.usuarios[identificador] = informacion
            return {"status" : "ok"}

        if modelDeDatos["accion"] == "enviar":
            return self.mandarMensaje(modelDeDatos)

        if modelDeDatos["accion"] == "listarMensajes":
            return {"status" : "ok",
                    "enviadoMsj" : self.mensajesPorUsuario}

        if modelDeDatos["accion"] == "recibir":
            return self.recibirMensajes(modelDeDatos)

        else:
            return {"status" : "ok",
                    "informacion" : self.usuarios}

    def mandarMensaje(self, modelDeDatos):
        usuario = modelDeDatos["usuario"]
        mensaje = modelDeDatos["informacionMsj"]["mensaje"]
        horaFecha = modelDeDatos["informacionMsj"]["horaFecha"]
        mensajeAGuardar = {"mensaje" : mensaje, "horaFecha": horaFecha}

        if usuario in self.mensajesPorUsuario:
            contenedor = self.mensajesPorUsuario[usuario]
        else:
            contenedor = []
            self.mensajesPorUsuario[usuario] = contenedor

        contenedor.append(mensajeAGuardar)

        return {"status" : "ok"}

    def recibirMensajes(self, modelDeDatos):
        mensajesAlmacenados = []
        usuario = modelDeDatos["usuario"]
        if usuario in self.mensajesPorUsuario:
            mensajesAlmacenados = self.mensajesPorUsuario[usuario]
        return {"status" : "ok", "recibidoMsj" : mensajesAlmacenados}

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
        "usuario" : "Fanny",
        "informacionMsj" : {
            "horaFecha" : datetime.datetime.now(),
            "mensaje" : "hola, como estas"
        }
    }

    enviarMensajeL = {
        "accion" : "enviar",
        "usuario" : "Luis",
        "informacionMsj" : {
            "horaFecha" : datetime.datetime.now(),
            "mensaje" : "muy bien y tu?"
        }
    }

    mensajesLista = {
        "accion" : "listarMensajes"
    }

    mensajesObtenerLuis = {
        "accion" : "recibir",
        "usuario" : "Luis"
    }

    mensajesObtenerFanny = {
        "accion" : "recibir",
        "usuario" : "Fanny"
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
        raise Exception("Incorrecto almacenamiento")

    # Ejemplo Listar con un elemento
    respuesta_listado = actionHandler.procesaAccion(modelDeDatosListar)
    if respuesta_listado["status"] == "ok":
        informacion_listado = respuesta_listado["informacion"]
        print informacion_listado
        if len(informacion_listado) == 2:
            if informacion_listado["1"]["usuario"] == "Fanny":
                print "Correcto listado Fanny"
            else:
                raise Exception("Incorrecto listado Fanny")
            if informacion_listado["2"]["usuario"] == "Luis":
                print "Correcto listado Luis"
            else:
                raise Exception("Incorrecto listado Luis")
        else:
            raise Exception("Incorrecto usuarios almacenados")
    else:
        raise Exception("Incorrecto listado")

    #Ejemplo Enviado
    enviado_Fanny = actionHandler.procesaAccion(enviarMensajeF)
    if enviado_Fanny["status"] == "ok":
        print "Enviado correctamente"
    else:
        raise Exception("Fallo en el envio")

    #Ejemplo de lista de mensajes enviados
    lista_enviados = actionHandler.procesaAccion(mensajesLista)
    if lista_enviados["status"] == "ok" and len(lista_enviados["enviadoMsj"]) == 1:
        print lista_enviados["enviadoMsj"]
        print "Mensajes almacenados correctamente"
    else:
        raise Exception("Fallo listado de todos los mensajes")

    #Ejemplo Recibido de Luis
    respuesta_recibido = actionHandler.procesaAccion(mensajesObtenerLuis)
    if respuesta_recibido["status"] == "ok" and len(respuesta_recibido["recibidoMsj"]) == 0:
        print "Recibido para Luis"
        print respuesta_recibido
    else:
        raise Exception("Error mensajes recibidos para Luis")

    #Ejemplo Recibido de Fanny
    respuesta_recibido = actionHandler.procesaAccion(mensajesObtenerFanny)
    if respuesta_recibido["status"] == "ok" and len(respuesta_recibido["recibidoMsj"]) == 1:
        print "Recibido para Fanny"
        print respuesta_recibido
    else:
        raise Exception("Error mensajes recibidos para Fanny")

    #Ejemplo Recibido de Fanny sin mensajes
    respuesta_recibido = actionHandler.procesaAccion(mensajesObtenerFanny)
    if respuesta_recibido["status"] == "ok" and len(respuesta_recibido["recibidoMsj"]) == 0:
        print "Recibido para Fanny"
        print respuesta_recibido
    else:
        raise Exception("Error mensajes recibidos para Fanny sin mensajes")
