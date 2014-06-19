from Tkinter import *
from listaUsuarios import main as _listarUsuarios

class Dialog(Frame):

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
        if self.delegado is not None:
            self.delegado.elemento_seleccionado(elemento)


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


def main():
    master = Tk()
    return Dialog(master)

if __name__ == "__main__":
    dialog = main()
    for item in ["one", "two", "three", "four", "two", "three", "four", "two", "three", "four", "two", "three", "four", "two", "three", "four"]:
        dialog.lista.insert(END, item)
    dialog.proveedor = ProveedorDeUsuarios()
    dialog.pack()
    mainloop()