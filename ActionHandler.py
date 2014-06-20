#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import uuid
import FileHandler
import json

class ActionHandler(object):

    def __init__(self):
        super(ActionHandler, self).__init__()
        self.usuarios = {}
        self.mensajesPorUsuario = {}
        self.usuarios["0"] = {"status" : "online", "usuario" : "ROOT"}

    def procesaAccion(self, modelDeDatos):
        if modelDeDatos["accion"] == "actualizar":
            identificador = str(modelDeDatos["identificador"])
            if identificador == "0" or identificador in self.usuarios:
                informacion = modelDeDatos["informacion"]
                retorno = {"status" : "ok"}
                if identificador == "0":
                    identificador = str(uuid.uuid4())
                    llavePrivada = str(uuid.uuid4())

                    informacion["llavePrivada"] = llavePrivada

                    retorno["identificador"] = identificador
                    retorno["llavePrivada"] = llavePrivada

                self.usuarios[identificador] = informacion
                return retorno

            return {"status" : "error", "mensaje" : "Identificador destinatario no valido"}

        if modelDeDatos["accion"] == "enviar":
            return self.mandarMensaje(modelDeDatos)

        if modelDeDatos["accion"] == "listarMensajes":
            return {"status" : "ok",
                    "enviadoMsj" : self.mensajesPorUsuario}

        if modelDeDatos["accion"] == "recibir":
            return self.recibirMensajes(modelDeDatos)

        if modelDeDatos["accion"] == "backup":
            return self.hazRespaldo()

        if modelDeDatos["accion"] == "restaurar":
            return self.restauraRespaldo()

        if modelDeDatos["accion"] == "listar":
            return self.listaUsuarios()

        else:
            return {"status" : "ok",
                    "informacion" : self.usuarios}

    def agregaMensajeAContenedorDeUsuario(self, usuarioInteres, mensajeInteres):
        if usuarioInteres in self.mensajesPorUsuario:
            contenedor = self.mensajesPorUsuario[usuarioInteres]
        else:
            contenedor = []
            self.mensajesPorUsuario[usuarioInteres] = contenedor
        contenedor.append(mensajeInteres)

    def mandarMensaje(self, modelDeDatos):
        usuarioDestinatario = modelDeDatos["identificador"]
        if usuarioDestinatario in self.usuarios:
            mensaje = modelDeDatos["informacionMsj"]
            mensaje["destinatario"] = usuarioDestinatario
            self.agregaMensajeAContenedorDeUsuario(usuarioDestinatario, mensaje)
            if "remitente" in mensaje and mensaje["remitente"] in self.usuarios:
                self.agregaMensajeAContenedorDeUsuario(mensaje["remitente"], mensaje)

            return {"status" : "ok"}
        else:
            return {"status" : "error", "mensaje" : "Identificador destinatario no valido"}

    def recibirMensajes(self, modelDeDatos):
        usuario = str(modelDeDatos["identificador"])
        hayMensajes = usuario in self.mensajesPorUsuario
        usuarioValido = self.usuarios[usuario]["llavePrivada"] == modelDeDatos["llavePrivada"]
        participante = modelDeDatos["participante"] if "participante" in modelDeDatos else ""
        mensajesAlmacenados = []
        if usuario == "0" or (hayMensajes and usuarioValido):
            mensajesAlmacenados = self.mensajesPorUsuario[usuario]
            mensajesAlmacenados = [mensaje for mensaje in mensajesAlmacenados if self.filtraMensajes(mensaje, participante)]

        return {"status" : "ok", "recibidoMsj" : mensajesAlmacenados}

    def hazRespaldo(self):
        FileHandler.stringAArchivo("Backup/usuarios", json.dumps(self.usuarios), toBase64=False)
        FileHandler.stringAArchivo("Backup/mensajesPorUsuario", json.dumps(self.mensajesPorUsuario), toBase64=False)
        return {"status" : "ok"}

    def restauraRespaldo(self):
        if FileHandler.existeArchivo("Backup/usuarios") and FileHandler.existeArchivo("Backup/mensajesPorUsuario"):
            self.usuarios = json.loads(FileHandler.archivoAString("Backup/usuarios", toBase64=False))
            self.mensajesPorUsuario = json.loads(FileHandler.archivoAString("Backup/mensajesPorUsuario", toBase64=False))
            return {"status" : "ok"}
        return {"status" : "error", "mensaje" : "No hay respaldo existente"}

    def listaUsuarios(self):
        usuarios = self.usuarios
        salida = {}
        for identificador in usuarios:
            infoPrivada = dict(usuarios[identificador])
            if "llavePrivada" in infoPrivada:
                infoPrivada.pop("llavePrivada")
            if identificador == "0" or infoPrivada["status"] == "online":
                salida[identificador] = infoPrivada

        return {"status" : "ok", "informacion" : salida}

    def filtraMensajes(self, mensaje, usuario):
        remitente = mensaje["remitente"] if "remitente" in mensaje else ""
        destinatario = mensaje["destinatario"] if "destinatario" in mensaje else ""
        return remitente == usuario or destinatario == usuario


if __name__ == "__main__":

    modelDeDatosActualizar = {
        "accion" : "actualizar",
        "identificador" : "1",
        "informacion" : {
            "status" : "online",
            "usuario" : "Fanny",
            "IP" : "192.168.1.65",
            "puerto" : 13375
        }
    }

    modelDeDatosActualizar1 = {
        "accion" : "actualizar",
        "identificador" : "2",
        "informacion" : {
            "status" : "online",
            "usuario" : "Luis",
            "IP" : "192.168.1.65",
            "puerto" : 13378
        }
    }

    modelDeDatosListar = {
        "accion" : "listar"
    }

    enviarMensajeF = {
        "accion" : "enviar",
        "identificador" : "1",
        "informacionMsj" : {
            "horaFecha" : datetime.datetime.now(),
            "mensaje" : "hola, como estas"
        }
    }

    enviarMensajeL = {
        "accion" : "enviar",
        "identificador" : "2",
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
        "identificador" : "2"
    }

    mensajesObtenerFanny = {
        "accion" : "recibir",
        "identificador" : "1"
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
