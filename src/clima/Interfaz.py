import json
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

        """
        try:
            super().__init__(raiz)
            raiz.title("Clima")
            raiz.resizable(False,False)
            raiz.geometry("700x500")
            raiz.config(bg="light blue")
            cuadro=Frame(width=650, height= 500,bd=10,relief="groove",bg="light blue")
            cuadro.pack()
            self.cuadro = cuadro
            aeropuertoOrigenLabel=Label(cuadro, text='Seleccione la ciudad para consultar su clima:',
                         justify="center",bg="light blue", fg='blue', font=("Purisa", 18))
            aeropuertoOrigenLabel.place(x=15, y=5)
            self.__desplegable = ttk.Combobox(state="readonly", values=lista)
            self.__desplegable.bind("<<ComboboxSelected>>",self.__muestraEscogido)
            self.__desplegable.place(x=50,y=70)
        except TypeError:
            print("raiz no es un tt.Tk() o lista no es una lista")


    def __muestraEscogido(self,event):
            """
            Muestra el elemento escogido en una ventanita, además, crea un botón.
            """
            escogido = self.__desplegable.get()
            messagebox.showinfo(title="Selección",message="Ha seleccionado: "+escogido)
            climas =Climas()
            ciudad = climas.buscaCiudad(escogido)
            boton = ttk.Button(text="mostrar clima", command=partial(self.__muestraClima,
                                         self, self.cuadro, ciudad.latitud,ciudad.altitud, escogido))
            boton.place(x=280,y=65)

    def __muestraClima(self,event, cuadro : Frame, lat:float,lon:float, nombre):
        """
        Despliega un label con el clima de la ciudad solicitada
        """
        try:
            solicitud = Peticion(lat,lon,nombre)
            ruta = "../caché/peticiones/"+nombre+".json"
            with open(ruta, 'r') as j:
                info = json.load(j)
                climainfo = info['weather']
                descripcion = climainfo[0]["description"] 
                climaLabel = Label(self.cuadro,
                     text="Temperatura :  "+ str(info['main']['temp'] )+"°C"
                     +"\n"+"Máxima de  "+ str(info["main"]["temp_max"])+ "°C"
                     +"\n"+"Mínima de  " + str(info["main"]["temp_min"])+ "°C"
                     +"\n"+ descripcion+ "\n"+ "Percepción térmica: "
                     + str(info["main"]["feels_like"])+ "°C",
                     justify= "center",bg="pink" ,
                     fg="blue", font=("Purisa",18))
                climaLabel.place(x=15,y=140)      
        except FileNotFoundError:
             print("Archivo json no encontrado")




raiz=tk.Tk()
aeropuertos = Climas()
lista = aeropuertos.arregloNombres()
objeto = Interfaz(raiz, lista)
objeto.mainloop()
