from tkinter import*
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

class Interfaz(ttk.Frame):

    def __init__(self, raiz, lista):
        """Metodo para construir la interfaz.

        raiz = tt.Tk() - la ventana principal

        lista = list - una lista de paises.

        TODO: implementar muestraClima()
        """
        try:
            super().__init__(raiz)
            self.lista=lista
            #configurando la ventana
            raiz.title("Clima")
            raiz.resizable(False,False)
            raiz.geometry("700x500")
            raiz.config(bg="light blue")
            #configurando Frame
            cuadro=Frame(width=650, height= 500,bd=10,relief="groove",bg="light blue")
            cuadro.pack()
            #Label de Ciudad de destino
            ciudadOrigenLabel=Label(cuadro, text='Seleccione la ciudad para consultar su clima:',
                         justify="center",bg="light blue", fg='blue', font=("Purisa", 18))
            ciudadOrigenLabel.place(x=15, y=5)
            #Creando un menú desplegable
            self.desplegable = ttk.Combobox(state="readonly", values=lista)
            self.desplegable.bind("<<ComboboxSelected>>",self.muestraEscogido)
            self.desplegable.place(x=50,y=70)

            boton = ttk.Button(text="mostrar clima", command=self.muestraClima)
            boton.place(x=280,y=65)
        except TypeError: 
            print("raiz no es un tt.Tk() o lista no es una lista")


    def muestraEscogido(self,event):
            escogido = self.desplegable.get()
            messagebox.showinfo(title="Selección",message="Ha seleccionado: "+escogido)

    def muestraClima(self):
        print("Work in progress")    


raiz=tk.Tk()
lista=["Mexico", "Canada", "Estados Unidos"]
objeto = Interfaz(raiz, lista)
objeto.mainloop()

