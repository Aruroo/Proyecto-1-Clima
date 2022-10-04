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
            #Label de aeropuerto de destino
            aeropuertoOrigenLabel=Label(cuadro, text='Seleccione la aeropuerto para consultar su clima:',
                         justify="center",bg="light blue", fg='blue', font=("Purisa", 18))
            aeropuertoOrigenLabel.place(x=15, y=5)
            #Creando un menú desplegable
            self.desplegable = ttk.Combobox(state="readonly", values=lista)
            self.desplegable.bind("<<ComboboxSelected>>",self.__muestraEscogido)
            self.desplegable.place(x=50,y=70)
            #un boton para crear un label con la información solicitada
        except TypeError:
            print("raiz no es un tt.Tk() o lista no es una lista")


    def __muestraEscogido(self,event):
        """
        Muestra el elemento escogido en una ventanita, además, crea un botón.
        """
        #el elemento escogido por el usuario.
        escogido = self.desplegable.get()
        #mensaje para saber cual es el elemento escogido por el usuario
        messagebox.showinfo(title="Selección",message="Ha seleccionado: "+escogido)
        climas =Climas()
        aeropuerto = climas.buscaAeropuerto(escogido)
        #Creando un botón que al presionarse, ejecuta el método "muestra clima"
        boton = ttk.Button(text="mostrar clima", command=partial(self.__muestraClima,
                                     self, self.cuadro, aeropuerto.latitud,aeropuerto.altitud, escogido))
        boton.place(x=280,y=65)

    def __muestraClima(self,event, cuadro : Frame, lat:float,lon:float, nombre):
        """
        Despliega un label con el clima del aeropuerto solicitado
        """
        try:
            solicitud = Peticion(lat,lon,nombre)
            ruta = "../caché/peticiones/"+nombre+".json"
            with open(ruta, 'r') as j:
                info = json.load(j)
                #weather devuelve una lista cuyo unico elemento es un diccionario
                climainfo = info['weather']
                descripcion = climainfo[0]["description"]
                #un label muy extenso
                climaLabel = Label(self.cuadro,
                     text="Temperatura:  "+ str(info['main']['temp'])
                     +"\n"+"Máxima de  "+ str(info["main"]["temp_max"])
                     +"\n"+"Mínima de  " + str(info["main"]["temp_min"])
                     +"\n"+ descripcion+ "\n"+ "Percepción térmica: "
                     + str(info["main"]["feels_like"]),
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
