import imp
from Peticion import Peticion
from functools import partial
from tkinter import*
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

from Climas import Climas


class Interfaz(ttk.Frame):

    def __init__(self, raiz, lista):
        """Metodo para construir la interfaz.

        raiz = tt.Tk() - la ventana principal

        lista = list - una lista de paises.

        TODO: recibir las ciudades con sus coordenadas del CSV
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
            self.cuadro = cuadro
            #Label de Ciudad de destino
            ciudadOrigenLabel=Label(cuadro, text='Seleccione la ciudad para consultar su clima:',
                         justify="center",bg="light blue", fg='blue', font=("Purisa", 18))
            ciudadOrigenLabel.place(x=15, y=5)
            #Creando un menú desplegable
            self.desplegable = ttk.Combobox(state="readonly", values=lista)
            self.desplegable.bind("<<ComboboxSelected>>",self.muestraEscogido)
            self.desplegable.place(x=50,y=70)
            #un boton para crear un label con la información solicitada
        except TypeError:
            print("raiz no es un tt.Tk() o lista no es una lista")


    def muestraEscogido(self,event):
            """
            Muestra el elemento escogido en una ventanita, además, crea un botón.
            """
            #el elemento escogido por el usuario.
            escogido = self.desplegable.get()
            #mensaje para saber cual es el elemento escogido por el usuario
            messagebox.showinfo(title="Selección",message="Ha seleccionado: "+escogido)
            climas =Climas()
            ciudad = climas.buscaCiudad(escogido)
            boton = ttk.Button(text="mostrar clima", command=partial(self.muestraClima,
                                         self, self.cuadro, ciudad.latitud,ciudad.altitud, escogido))
            boton.place(x=280,y=65)

    def muestraClima(self, event, cuadro : Frame, lat:float,lon:float, nombre):
        """
        Despliega un label con el clima de la ciudad solicitada
        """
        try:
            solicitud = Peticion(lat,lon,nombre)
            climaLabel = Label()
            climaLabel.place(x=15,y=150)
        except ConnectionError:
            print("conexión fallida")




raiz=tk.Tk()
ciudades = Climas()
lista = ciudades.arregloNombres()
objeto = Interfaz(raiz, lista)
objeto.mainloop()
