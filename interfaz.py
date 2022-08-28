from tkinter import*
import requests

class Interfaz():
    
    def ejecutaInterfaz(): 
        raiz= Tk()
        cuadro=Frame(width=650, height= 500,bd=20,relief="groove",bg="gray")
        #bg es el grosor del borde del frame
        ciudadOrigenLabel=Label(cuadro, text='Inserte su ciudad de origen:', justify="center",bg="blue", fg='red', font=("Arial", 20))
        imagenNube= PhotoImage(file="nube.png")
        imagenNube=imagenNube.subsample(10)
        Label(cuadro, image=imagenNube).place(x=500, y=5)
        raiz.title("Clima")
        raiz.resizable(False,False)
        raiz.geometry("700x500")
        raiz.config(bg="gray")
        
        cuadro.pack()
        ciudadOrigenLabel.place(x=20, y=5) #permite colocar el label en una coordenada dada
        raiz.mainloop()

    ejecutaInterfaz()
