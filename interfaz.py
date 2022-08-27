from tkinter import*

raiz= Tk()
raiz.title("Clima")
raiz.resizable(False,False)
raiz.geometry("700x500")
raiz.config(bg="gray")
cuadro=Frame()
cuadro.pack()
cuadro.config(bg="blue")
cuadro.config(width=650, height= 500)
cuadro.config(bd=20)
cuadro.config(relief="groove")
raiz.mainloop()
