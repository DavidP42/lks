import tkinter as tk
from tkinter import ttk
from tkinter import *

from tkinter.ttk import *

from tkinter.ttk import Progressbar

from tkinter import Menu

def calculadora(num1, num2,operador):
    if operador == '+':
        resultado = num1 + num2
    elif operador== '*':
        resultado = num1 * num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '/':
        resultado = num1 / num2
    else:
        resultado = num1 ** num2
    return resultado

def click_calcular(label, num1, num2, operador):

    valor1 = float(num1)
    valor2 = float(num2)

    res = calculadora(valor1, valor2, operador)

    label.configure(text ='Resultado: ' + str(res))

def init_window():

    window = tk.Tk()
    window.title('Calculadura')
    window.geometry('400x250')

    lebel = tk.Label(window, text='Calculadora', font=('Arial bold', 15))
    lebel.grid(column = 0, row = 0)

    entrada1 = tk.Entry(window, width=10)
    entrada2 = tk.Entry(window, width=10)

    entrada1.grid(column=1, row=1)
    entrada2.grid(column=1, row=2)

    lebel_entrada1 = tk.Label(window, text='Ingrese numero: ', font=('Arial bold', 10))
    lebel_entrada1.grid(column=0, row=1)

    lebel_entrada2 = tk.Label(window, text='Ingrese numero: ', font=('Arial bold', 10))
    lebel_entrada2.grid(column=0, row=2)

    lebel_operador = tk.Label(window, text='Escoja Operador', font=('Arial bold', 10))
    lebel_operador.grid(column=0, row=3)

    combo_operadores = ttk.Combobox(window)
    combo_operadores['values'] = ['+','-','*','/','pow']
    combo_operadores.current(0)
    combo_operadores.grid(column=1, row=3)


    lebel_resultado = tk.Label(window, text='Resultado ', font=('Arial bold', 15))
    lebel_resultado.grid(column=0, row=5)

    boton = tk.Button(window,
                    command = lambda: click_calcular(
                        lebel_resultado,
                        entrada1.get(),
                        entrada2.get(),
                        combo_operadores.get()),
                    text='Calcular',
                    bg='Purple',
                    fg='white')

    boton.grid(column = 1, row = 4)


    style = ttk.Style()

    style.theme_use('default')

    style.configure("black.Horizontal.TProgressbar", background='black')

    bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')

    bar['value'] = 100

    bar.grid(column=0, row=300)


    menu = Menu(window)

    new_item = Menu(menu)

    new_item.add_command(label='Copiar')

    new_item.add_separator()

    new_item.add_command(label='Historial')

    menu.add_cascade(label='Funciones', menu=new_item)

    window.config(menu=menu)





    chk_state = BooleanVar()

    chk_state.set(True)  # set check state

    chk = Checkbutton(window, text='Choose', var=chk_state)

    chk.grid(column=300, row=0)

    window.mainloop()
def main():
    init_window()

main()
