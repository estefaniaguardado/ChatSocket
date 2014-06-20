from Tkinter import *
from listaUsuarios import main as _listarUsuarios
from recibirMensaje import main as _recivirMensajes

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
        # TODO: Agregar Textfield para envio de mensaje e inyectarlo con el delegado

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
        if self.delegado is not None:
            self.delegado.elemento_seleccionado(int(elemento[0]))

class DialogoConversacion(DialogoContactos):
    def __init__(self, master):
        DialogoContactos.__init__(self, master)
        def enterKey(event):
            self.procesaMensaje()
        self.r = StringVar()
        self.messageEntry = Entry(master, textvariable=self.r)
        self.messageEntry.pack(fill=X, side=BOTTOM)
        self.messageEntry.bind('<Return>', enterKey)

    def procesaMensaje(self):
        message_entry_get = self.messageEntry.get()
        self.messageEntry.delete(0, END)
        if self.delegado is not None:
            self.delegado.procesa_texto(message_entry_get)


class ProveedorDeUsuarios(object):
    def __init__(self):
        self.llaves = None
        self.valores = None
        self.usuarios = None

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
        # TODO: Generar una nueva lista como proveedor "ProveedorDeMensajes"



class ProveedorDeMensajes(object):
    def elemento_seleccionado(self, indiceElemento, identificadorSeleccionado):
        _recivirMensajes(["ProveedorDeUsuarios", llavePublica, llavePrivada, identificadorSeleccionado])
        # TODO: obtener mensajes filtrados y cargarlos en el modelo para que al pedirlo la vista se muestre

    def procesa_texto(self, textoMensaje):
        # TODO: publicar mensaje en la conversacion
        pass


# TODO: Crear clase para envio de mensaje a usuario seleccionado
class GestorMensajes(object):
    pass

def main():
    master = Tk()
    dialog = DialogoContactos(master)
    proveedor_de_usuarios = ProveedorDeUsuarios()
    dialog.proveedor = proveedor_de_usuarios
    dialog.delegado = proveedor_de_usuarios
    return dialog

if __name__ == "__main__":
    dialog = main()
    dialog.pack()
    mainloop()