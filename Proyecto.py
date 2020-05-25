from tkinter import *
#Creacion de la ventana
ventana = Tk()
ventana.geometry("500x400+300+200")
ventana.config(bg="white")
ventana.title("Calculadora de Integrales")

#Caja de texto
txt = Entry(ventana).place(x=80,y=50)

#Boton para calcular
boton1 = Button(ventana, text = "Calcular").place(x=220,y=50)

#Carga de imagenes
imagenL = PhotoImage(file = "Integral.gif")
labelImagen = Label(ventana, image= imagenL).place (x=0, y=0)

ventana.mainloop()
