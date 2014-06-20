#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import time
import Client
import tkFileDialog

from Tkinter import *
from listaUsuarios import main as _listarUsuarios
from recibirMensaje import main as _recivirMensajes
from enviarMensaje import main as _enviarMensaje
from actualizarUsuario import  main as _actualizarUsuario
from enviarArchivo import main as _enviarArchivo
from recibirMensaje import procesaMensajesDeArchivo as _procesaMensajesDeArchivo

llavePublica = ""
llavePrivada = ""

class DialogoContactos(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.elemento_actual = None
        scroll = Scrollbar(self, orient=VERTICAL)
        self.lista = Listbox(self, selectmode=EXTENDED, yscrollcommand=scroll.set)
        scroll.config(command=self.lista.yview)
        scroll.pack(side=RIGHT, fill=Y)
        self.lista.pack(side=LEFT, fill=BOTH, expand=1)
        self.delegado = None
        self.proveedor = None

        self.revision_seleccion()
        self.cargaInformacion()

    def cargaInformacion(self):
        if self.proveedor is not None:
            listado = self.proveedor.obtenListado()
            if listado is not None:
                self.lista.delete(0, END)
                for item in listado:
                    self.lista.insert(END, item)
        self.after(500, self.cargaInformacion)


    def revision_seleccion(self):
        elemento_actual = self.lista.curselection()
        if elemento_actual != self.elemento_actual:
            self.elemento_seleccionado(elemento_actual)
            self.elemento_actual = elemento_actual
        self.after(250, self.revision_seleccion)

    def elemento_seleccionado(self, elemento):
        if self.delegado is not None and len(elemento) > 0:
            self.delegado.elemento_seleccionado(int(elemento[0]))

class DialogoConversacion(DialogoContactos):
    def __init__(self, master):
        DialogoContactos.__init__(self, master)
        def enterKey(evento):
            self.procesaMensaje()
        def clicKey(evento):
            self.procesaClic(evento)
        self.r = StringVar()
        self.messageEntry = Entry(master, textvariable=self.r)
        self.messageEntry.pack(fill=X, side=BOTTOM)
        self.messageEntry.bind('<Return>', enterKey)
        self.messageEntry.bind("<Double-Button-1>", clicKey)

    def procesaMensaje(self):
        message_entry_get = self.messageEntry.get()
        self.messageEntry.delete(0, END)
        if self.delegado is not None:
            self.delegado.procesa_texto(message_entry_get)

    def procesaClic(self, evento):
        f = tkFileDialog.askopenfilename()
        if self.delegado is not None:
            self.delegado.procesa_archivo(f)



class ProveedorDeUsuarios(object):
    def __init__(self):
        self.llaves = None
        self.valores = None
        self.usuarios = None
        self.gestorMensajes = None
        self.proveedorDeMensajes = None

    def obtenListado(self):
        informacion = _listarUsuarios()
        if informacion["status"] == "ok":
            nuevasLlaves = sorted(informacion["informacion"].keys())
            if self.llaves != nuevasLlaves:
                self.usuarios = informacion["informacion"]
                self.llaves = nuevasLlaves
                self.valores = [ self.usuarios[llave]["usuario"] for llave in self.llaves ]

                return self.valores
        return None

    def elemento_seleccionado(self, indiceElemento):
        identificadorSeleccionado = self.llaves[indiceElemento]
        usuarioSeleccionado = self.usuarios[identificadorSeleccionado]
        if self.gestorMensajes is not None:
            self.gestorMensajes.identificadorUsuario = identificadorSeleccionado
            self.gestorMensajes.estableceUsuarioSeleccionado(usuarioSeleccionado)


class ProveedorDeMensajes(object):
    def __init__(self):
        self.identificadorUsuario = None
        self.usuarioSeleccionado = None
        self.mensajes = []
        self.mensajesPlanos = []

    def cargaInformacion(self):
        if self.identificadorUsuario is not None:
            respuestaRecibirMensajes = _recivirMensajes(["ProveedorDeUsuarios", llavePublica, llavePrivada, self.identificadorUsuario])
            self.mensajes = respuestaRecibirMensajes["recibidoMsj"]
            self.mensajesPlanos = [ ( "> " + infoMensaje["mensaje"] if "remitente" in infoMensaje and infoMensaje["remitente"] == llavePublica else "-> " + infoMensaje["mensaje"] ) for infoMensaje in self.mensajes ]

    def obtenListado(self):
        self.cargaInformacion()
        return self.mensajesPlanos

    def elemento_seleccionado(self, indiceElemento):
        mensajeSeleccionado = self.mensajes[indiceElemento]
        _procesaMensajesDeArchivo([mensajeSeleccionado])


    def estableceUsuarioSeleccionado(self, usuarioSeleccionado):
        self.usuarioSeleccionado = usuarioSeleccionado
        self.cargaInformacion()

    def procesa_texto(self, textoMensaje):
        if self.identificadorUsuario is not None:
            _enviarMensaje(["ProveedorDeMensajes", self.identificadorUsuario, textoMensaje, llavePublica])

    def procesa_archivo(self, nombreArchivo):
        if self.identificadorUsuario is not None and len(nombreArchivo):
            _enviarArchivo(["ProveedorDeMensajes", self.identificadorUsuario, nombreArchivo, llavePublica])

def main():
    masterContactos = Tk()
    dialogoContactos = DialogoContactos(masterContactos)
    proveedor_de_usuarios = ProveedorDeUsuarios()
    dialogoContactos.proveedor = proveedor_de_usuarios
    dialogoContactos.delegado = proveedor_de_usuarios

    masterConversacion = Tk()
    dialogo_conversacion = DialogoConversacion(masterConversacion)
    proveedor_de_mensajes = ProveedorDeMensajes()
    dialogo_conversacion.proveedor = proveedor_de_mensajes
    dialogo_conversacion.delegado = proveedor_de_mensajes

    proveedor_de_usuarios.gestorMensajes = proveedor_de_mensajes

    return dialogoContactos, dialogo_conversacion

if __name__ == "__main__":
    serverIP = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
    serverPort = sys.argv[2] if len(sys.argv) > 2 else "13373"
    userName = sys.argv[3] if len(sys.argv) > 3 else time.strftime("%d %m %Y %H:%M:%S", time.gmtime())

    Client.targetPort = int(serverPort)
    Client.targetIP = str(serverIP)

    resultadoInicializacion = _actualizarUsuario(["TKChat", "0", "online", userName, serverIP, serverPort])
    llavePublica = resultadoInicializacion["identificador"]
    llavePrivada = resultadoInicializacion["llavePrivada"]

    dialogoContactos, dialogoConversacion = main()
    dialogoContactos.pack()
    dialogoConversacion.pack()
    mainloop()

    resultadoInicializacion = _actualizarUsuario(["TKChat", llavePublica, "offline", userName, serverIP, serverPort])