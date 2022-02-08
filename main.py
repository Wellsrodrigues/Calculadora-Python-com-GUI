from tkinter import *
from tkinter import ttk

tela = Tk()
tela.title("Calculadora")
tela.geometry("235x310+550+200")
tela.resizable(0, 0)
tela.config(background="white")

display = Frame(tela, width=235, height=50, background="#1e1f1e")
display.grid(row=0, column=0)

botoes = Frame(tela, width=235, height=268)
botoes.grid(row=1, column=0)

TodosValores = ''

def expressao(event):
    global TodosValores
    TodosValores = TodosValores + str(event)
    texto.set(TodosValores)

def calcular():
    global TodosValores
    result = eval(TodosValores)
    texto.set(result)

def limpar():
    global  TodosValores
    TodosValores = ""
    texto.set("")


texto = StringVar()

visor = Label(display, textvariable=texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=("Ivy 18"), fg="white", background="#1e1f1e")
visor.place(x=0, y=0)

b1 = Button(botoes,command=lambda: limpar(), text="C", width=11, height=2, background="#808080", font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b1.place(x=0, y=0)
b2 = Button(botoes, command=lambda: expressao('%'), text="%", width=5, height=2, background="#808080",  font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b2.place(x=120, y=0)
b3 = Button(botoes, command=lambda: expressao('/'), text="/", width=5, height=2, background="#FFA500", fg="white",  font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b3.place(x=180, y=0)


b4 = Button(botoes, command=lambda: expressao('7'), text="7", width=5, height=2, background="#808080",  font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b4.place(x=0, y=52)
b5 = Button(botoes, command=lambda: expressao('8'),text="8", width=5, height=2, background="#808080",  font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b5.place(x=60, y=52)
b6 = Button(botoes, command=lambda: expressao('9'),text="9", width=5, height=2, background="#808080",  font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b6.place(x=120, y=52)
b7 = Button(botoes, command=lambda: expressao('*'),text="*", width=5, height=2, background="#FFA500", fg="white",  font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b7.place(x=180, y=52)


b8 = Button(botoes, command=lambda: expressao('4'),text="4", width=5, height=2, background="#808080",  font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b8.place(x=0, y=104)
b9 = Button(botoes, command=lambda: expressao('5'),text="5", width=5, height=2, background="#808080",  font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b9.place(x=60, y=104)
b10 = Button(botoes, command=lambda: expressao('6'),text="6", width=5, height=2, background="#808080",  font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b10.place(x=120, y=104)
b11 = Button(botoes, command=lambda: expressao('-'),text="-", width=5, height=2, background="#FFA500", fg="white",  font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b11.place(x=180, y=104)


b8 = Button(botoes, command=lambda: expressao('1'),text="1", width=5, height=2, background="#808080",  font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b8.place(x=0, y=156)
b9 = Button(botoes, command=lambda: expressao('2'),text="2", width=5, height=2, background="#808080",  font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b9.place(x=60, y=156)
b10 = Button(botoes, command=lambda: expressao('3'),text="3", width=5, height=2, background="#808080",  font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b10.place(x=120, y=156)
b11 = Button(botoes, command=lambda: expressao('+'),text="+", width=5, height=2, background="#FFA500", fg="white",  font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b11.place(x=180, y=156)


b12 = Button(botoes, command=lambda: expressao('0'),text="0", width=11, height=2, background="#808080", font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b12.place(x=0, y=208)
b13 = Button(botoes, command=lambda: expressao('.'), text=".", width=5, height=2, background="#808080",  font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b13.place(x=120, y=208)
b14 = Button(botoes, command=lambda: calcular(), text="=", width=5, height=2, background="#FFA500", fg="white",  font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b14.place(x=180, y=208)


tela.mainloop()
