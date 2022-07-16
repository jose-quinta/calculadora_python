import tkinter as tk
from tkinter.messagebox import askquestion

class Interface(tk.Frame):
  def __init__(self, master):
    super().__init__(master)
    self.master = master
    self.master.title('Calculadora')
    # self.master.geometry('100x150') # no se puede usar si usas grid
    self.first_number = tk.StringVar(self.master)
    self.second_number = tk.StringVar(self.master)
    self.operator = tk.StringVar(self.master)
    self.result = tk.StringVar(self.master)
    self.display_text = tk.StringVar(self.master)
    # self.pack() # No se puede usar pack cuando estas usando grid
    self.mostrar_campos()

  def salir_aplicacion(self): # No se esta usando
    request = askquestion(title='Salir de la aplicación', message='Desea salir de la aplicación realmente')
    if request == 'yes':
      self.master.destroy()

  def clear_first_number(self):
    self.first_number.set('')

  def clear_second_number(self):
    self.second_number.set('')

  def clear_operator(self):
    self.operator.set('')

  def clear_result(self):
    self.result.set('')

  def clear_display_text(self):
    self.display_text.set('')

  def eraser_all(self):
    self.clear_first_number()
    self.clear_second_number()
    self.clear_operator()
    self.clear_result()
    self.clear_display_text()

  def eraser_previous(self):
    string = self.display_text.get()
    self.display_text.set(string[:-1])

  def press_key(self, key):
    result = self.display_text.get() + key
    self.display_text.set(result)

  def sum_numbers(self, number):
    self.first_number.set(number)
    self.operator.set('+')
    self.display_text.set('')

  def subtract_numbers(self, number):
    self.first_number.set(number)
    self.operator.set('-')
    self.display_text.set('')

  def multiply_numbers(self, number):
    self.first_number.set(number)
    self.operator.set('*')
    self.display_text.set('')

  def split_numbers(self, number):
    self.first_number.set(number)
    self.operator.set('/')
    self.display_text.set('')

  def result_operation(self):
    self.second_number.set(self.display_text.get())
    if self.operator.get() == '+':
      self.result.set(float(self.first_number.get()) + float(self.second_number.get()))
      self.display_text.set(self.result.get())
      self.operator.set('')
    if self.operator.get() == '-':
      self.result.set(float(self.first_number.get()) - float(self.second_number.get()))
      self.display_text.set(self.result.get())
      self.operator.set('')
    if self.operator.get() == '*':
      self.result.set(float(self.first_number.get()) * float(self.second_number.get()))
      self.display_text.set(self.result.get())
      self.operator.set('')
    if self.operator.get() == '/':
      self.result.set(float(self.first_number.get()) / float(self.second_number.get()))
      self.display_text.set(self.result.get())
      self.operator.set('')

  def mostrar_campos(self):
    #------------------------------- el display  -------------------------------------------------------
    display = tk.Label(self.master, textvariable=self.display_text, width=37, height=4, foreground='green', background='black')
    display.grid(row= 0, column= 0, columnspan= 5)
    #------------------------- Botones para empezar -----------------------------------------------------
    boton_eraser_all = tk.Button(self.master, text='X', width=5, height=2, command=self.eraser_all)
    boton_eraser_all.grid(row= 1, column= 4)

    boton_eraser_one = tk.Button(self.master, text='C', width=5, height=2, command=self.eraser_previous)
    boton_eraser_one.grid(row=1, column=3)

    boton_number_nine = tk.Button(self.master, text='9', width=5, height=2, command=lambda:self.press_key('9'))
    boton_number_nine.grid(row= 1, column= 2)

    boton_number_eigth = tk.Button(self.master, text='8', width=5, height=2, command=lambda:self.press_key('8'))
    boton_number_eigth.grid(row= 1, column =1)

    boton_number_seven = tk.Button(self.master, text='7', width=5, height=2, command=lambda:self.press_key('7'))
    boton_number_seven.grid(row= 1, column= 0)

    boton_split = tk.Button(self.master, text='/', width=5, height=2, command=lambda:self.split_numbers(self.display_text.get()))
    boton_split.grid(row= 2, column= 4)

    boton_multiply = tk.Button(self.master, text='*', width=5, height=2, command=lambda:self.multiply_numbers(self.display_text.get()))
    boton_multiply.grid(row= 2, column= 3)

    boton_number_six = tk.Button(self.master, text='6', width=5, height=2, command=lambda:self.press_key('6'))
    boton_number_six.grid(row= 2, column= 2)

    boton_number_five = tk.Button(self.master, text='5', width=5, height=2, command=lambda:self.press_key('5'))
    boton_number_five.grid(row= 2, column= 1)

    boton_number_fourt = tk.Button(self.master, text='4', width=5, height=2, command=lambda:self.press_key('4'))
    boton_number_fourt.grid(row= 2, column= 0)

    boton_subtract = tk.Button(self.master, text='-', width=5, height=2, command=lambda:self.subtract_numbers(self.display_text.get()))
    boton_subtract.grid(row= 3, column= 4)

    boton_sum = tk.Button(self.master, text='+', width=5, height=2, command=lambda:self.sum_numbers(self.display_text.get()))
    boton_sum.grid(row= 3, column= 3)

    boton_number_three = tk.Button(self.master, text='3', width=5, height=2, command=lambda:self.press_key('3'))
    boton_number_three.grid(row= 3, column= 2)

    boton_number_two = tk.Button(self.master, text='2', width=5, height=2, command=lambda:self.press_key('2'))
    boton_number_two.grid(row= 3, column= 1)

    boton_number_one = tk.Button(self.master, text='1', width=5, height=2, command=lambda:self.press_key('1'))
    boton_number_one.grid(row= 3, column= 0)

    boton_number_zero = tk.Button(self.master, text='0', width=5, height=2, command=lambda:self.press_key('0'))
    boton_number_zero.grid(row=4, column= 0)

    boton_punto_coma = tk.Button(self.master, text=',', width=5, height=2, command=lambda:self.press_key('.'))
    boton_punto_coma.grid(row= 4, column= 1)

    boton_igual = tk.Button(self.master, text='=', width=20, height=2, command=lambda:self.result_operation())
    boton_igual.grid(row= 4, column=2, columnspan=3)