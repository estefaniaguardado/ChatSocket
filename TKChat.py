from Tkinter import *


class Dialog(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.elemento_actual = None
        scroll = Scrollbar(self, orient=VERTICAL)
        self.lista = Listbox(self, selectmode=EXTENDED, yscrollcommand=scroll.set)
        scroll.config(command=self.lista.yview)
        scroll.pack(side=RIGHT, fill=Y)
        self.lista.pack(side=LEFT, fill=BOTH, expand=1)

        self.revision_seleccion()

    def revision_seleccion(self):
        elemento_actual = self.lista.curselection()
        if elemento_actual != self.elemento_actual:
            self.elemento_seleccionado(elemento_actual)
            self.elemento_actual = elemento_actual
        self.after(250, self.revision_seleccion)

    def elemento_seleccionado(self, elemento):
        print "Seleccionado elemento", elemento


def main():
    master = Tk()
    return Dialog(master)

if __name__ == "__main__":
    dialog = main()
    for item in ["one", "two", "three", "four", "two", "three", "four", "two", "three", "four", "two", "three", "four", "two", "three", "four"]:
        dialog.lista.insert(END, item)
    dialog.pack()
    mainloop()