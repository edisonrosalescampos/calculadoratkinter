from tkinter import *

class Calculadora:
  def __init__(self):
    self.ventana = Tk()
    self.ventana.title("Calculadora Básica")
    #self.ventana.geometry("392x600")
    
    # CONFIGURAMOS LA PANTALLA
    self.pantalla = Entry(self.ventana, font=("Helvetica", 15))
    self.pantalla.grid(row=0, column=0, columnspan=4, sticky="WE", ipady=20)

    # CREAMOS UNA VARIABLE OPERACIÓN VACÍA
    self.operacion = "" 

    # CREAMOS LA BOTONERA DE LA CALCULADORA
    botonera = []
    botonera.append(self.crearBoton("C"))
    botonera.append(self.crearBoton("CE"))
    botonera.append(self.crearBoton("R"))
    botonera.append(self.crearBoton(u"\u232B"))
    botonera.append(self.crearBoton("7"))
    botonera.append(self.crearBoton("8"))
    botonera.append(self.crearBoton("9"))
    botonera.append(self.crearBoton("/"))
    botonera.append(self.crearBoton("4"))
    botonera.append(self.crearBoton("5"))
    botonera.append(self.crearBoton("6"))
    botonera.append(self.crearBoton("x"))
    botonera.append(self.crearBoton("1"))
    botonera.append(self.crearBoton("2"))
    botonera.append(self.crearBoton("3"))
    botonera.append(self.crearBoton("-"))
    botonera.append(self.crearBoton("."))
    botonera.append(self.crearBoton("0"))
    botonera.append(self.crearBoton("="))
    botonera.append(self.crearBoton("+"))
    #  botonera.append(self.crearBoton("=", 40))

    fila = 1
    columna = 0    
    for indice, boton in enumerate(botonera):
      if indice != 0 and indice % 4 == 0:
        fila = fila + 1
        columna = 0

      boton.grid(row=fila, column=columna)
      
      columna = columna + 1

    # BUCLE INFINITO
    self.ventana.mainloop()

  def crearBoton(self, texto, ancho=8, alto=4):
    return Button(self.ventana, text=texto, width=ancho, height=alto, font=("Helvetica", 10))

calculadora = Calculadora()