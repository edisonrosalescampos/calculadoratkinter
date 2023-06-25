from tkinter import *
from tkinter import messagebox

class Calculadora:
  def __init__(self):
    self.ventana = Tk()    
    self.ventana.title("Calculadora Básica")
    self.ventana.iconbitmap("calculadora.ico")
    #self.ventana.geometry("392x600")
    
    # CONFIGURAMOS LA PANTALLA
    self.pantalla = Text(self.ventana, width=0, height=3, font=("Helvetica", 15))
    self.pantalla.grid(row=0, column=0, columnspan=4, sticky="ew")

    # CREAMOS UNA VARIABLE OPERACIÓN VACÍA
    self.operacion = "" 

    # CREAMOS LA BOTONERA DE LA CALCULADORA
    botonera = []
    botonera.append(self.crearBoton("BORRAR"))
    botonera.append(self.crearBoton(u"\u232B"))
    botonera.append(self.crearBoton("7"))
    botonera.append(self.crearBoton("8"))
    botonera.append(self.crearBoton("9"))
    botonera.append(self.crearBoton("/"))
    botonera.append(self.crearBoton("4"))
    botonera.append(self.crearBoton("5"))
    botonera.append(self.crearBoton("6"))
    botonera.append(self.crearBoton("*"))
    botonera.append(self.crearBoton("1"))
    botonera.append(self.crearBoton("2"))
    botonera.append(self.crearBoton("3"))
    botonera.append(self.crearBoton("-"))
    botonera.append(self.crearBoton("."))
    botonera.append(self.crearBoton("0"))
    botonera.append(self.crearBoton("="))
    botonera.append(self.crearBoton("+"))

    botonera[0].grid(row=1, column=0, columnspan=2, sticky="ew")
    botonera[1].grid(row=1, column=2, columnspan=2, sticky="ew")

    contador = 2  
    for fila in range(2, 6):
      for columna in range(4):
        botonera[contador].grid(row=fila, column=columna)

        contador += 1

    # BUCLE INFINITO
    self.ventana.mainloop()

  def crearBoton(self, valor, ancho=8, alto=4):
    return Button(self.ventana, text=valor, width=ancho, height=alto, font=("Helvetica", 10), command=lambda:self.capturarClic(valor))
  
  def capturarClic(self, tecla):
    # OPCIÓN IGUAL
    if tecla == "=" and self.operacion != "":
      try:
        resultado = str(eval(self.operacion))
        self.operacion = resultado
        self.limpiarPantalla()
        self.mostrarPantalla(resultado)
      except ZeroDivisionError:
        messagebox.showwarning(title="Notificación", message="No es posible la división entre cero.")
      except SyntaxError:
        messagebox.showwarning(title="Notificación", message="El formato usado no es válido.")

    # OPCIÓN LIMPIAR PANTALLA
    elif tecla == "BORRAR":
      self.limpiarPantalla()

    # OPCIÓN BORRAR ÚLTIMO CARACTER
    elif tecla == u"\u232B":
      self.borrarPantalla()

    # TODAS LAS DEMÁS TECLAS
    else:
      self.operacion += tecla
      self.mostrarPantalla(tecla)

  def habilitarPantalla(self):
    self.pantalla.configure(state="normal")

  def deshabilitarPantalla(self):
    self.pantalla.configure(state="disabled")

  def borrarPantalla(self):
    texto = self.pantalla.get(1.0, END)
    texto = texto[:-2]
    self.operacion = texto
    self.habilitarPantalla()
    self.pantalla.delete(1.0, END)
    self.pantalla.insert(END, texto)
    self.deshabilitarPantalla()

  def limpiarPantalla(self):
    self.habilitarPantalla()    
    self.pantalla.delete(1.0, END)
    self.deshabilitarPantalla()

  def mostrarPantalla(self, texto):
    self.habilitarPantalla()
    self.pantalla.insert(END, texto)
    self.deshabilitarPantalla()


calculadora = Calculadora()