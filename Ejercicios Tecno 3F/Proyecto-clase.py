from tkinter import Tk, Entry, Button

ventana = Tk()

ventana.configure(background="Light Blue")
ventana.title("Calculadora Basica")
ventana.geometry("350x350")
ventana.resizable(False,False)

datos = Entry(ventana)
datos.grid(columnspan=10, ipadx = 150, ipady=10)

boton1 = Button(ventana, text="1", fg="black", bg="white", height=2, width= 10)
boton1.grid(columnspan=1, row=1, column= 0)

boton2 = Button(ventana, text="2", fg="black", bg="white", height=2, width= 10)
boton2.grid(columnspan=2, row=1, column=1)

ventana.mainloop()