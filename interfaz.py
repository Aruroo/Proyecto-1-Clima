from tkinter import*

class Interfaz():
    
    def ejecutaInterfaz(): 
        raiz= Tk()
        raiz.title("Clima")
        raiz.resizable(False,False)
        raiz.geometry("700x500")
        raiz.config(bg="gray")

        cuadro=Frame(width=650, height= 500,bd=10,relief="groove",bg="gray")
        cuadro.pack()

        ciudadOrigenLabel=Label(cuadro, text='Inserte su ciudad de origen:', justify="center",bg="grey", fg='pink', font=("Comic Sans MS", 30))
        ciudadOrigenLabel.place(x=20, y=5)

        imagenNube= PhotoImage(file="nube.png")
        imagenNube=imagenNube.subsample(5)
        Label(cuadro, image=imagenNube).place(x=480, y=5)


        raiz.mainloop()

    ejecutaInterfaz()
