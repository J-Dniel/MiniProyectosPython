#Python Tkinter Calculadora
#Codigo simple de una calculadora Python Tkinter
import parser
from tkinter import *
from tkinter import font
from typing import Sized

def Click(nu):

    nuScreen.set(nuScreen.get() + nu)

def Resultado():
    nuScreenStates = nuScreen.get()
    try:
        expresion = parser.expr(nuScreenStates).compile()
        result = eval(expresion)
        nuScreen.set(result)
    except Exception:
        nuScreen.set("Error")

def createButton(t, x, y):

        Button(miFrame, text=t, width=3, relief="flat", font=("Roboto Cn",14,"bold"), command=lambda:Click(t)).grid(row=x, column=y, pady=2, padx=2)

def delete():
    nuScreen.set("")

def undo():
    nuScreenStates = nuScreen.get()

    if nuScreenStates:
        nuScreen.set(nuScreenStates[:-1])
    else:
        nuScreen.set("Error")

if __name__ == "__main__":

    raiz = Tk()
    raiz.title("Calculadora")
    raiz.resizable(0,0)
    raiz.iconbitmap("calculadora.ico")

    miFrame = Frame(raiz)
    miFrame.pack()

    nuScreen = StringVar()
    
    screen = Entry(miFrame, textvariable=nuScreen,font=("Roboto Cn",16,"bold"))
    screen.grid(row=1, column=1, columnspan=4, padx=4,pady=4)
    screen.config(bg="black", fg="#03f943", justify="right")

    createButton("(",2,1)
    createButton(")",2,2)
    Button(miFrame, text="AC", width=3, relief="flat", font=("Roboto Cn",14,"bold"), command=lambda:delete()).grid(row=2, column=3, pady=2, padx=2)
    Button(miFrame, text="C", width=3, relief="flat", font=("Roboto Cn",14,"bold"), command=lambda:undo()).grid(row=2, column=4, pady=2, padx=2)

    createButton("7",3,1)
    createButton("8",3,2)
    createButton("9",3,3)
    createButton("/",3,4)
 
    createButton("4",4,1)
    createButton("5",4,2)
    createButton("6",4,3)
    createButton("*",4,4)

    createButton("1",5,1)
    createButton("2",5,2)
    createButton("3",5,3)
    createButton("-",5,4)

    createButton(".",6,1)
    createButton("0",6,2)
    Button(miFrame, text="=", width=3, relief="flat", font=("Roboto Cn",14,"bold"), command=lambda:Resultado()).grid(row=6, column=3, pady=2, padx=2)
    createButton("+",6,4)



    raiz.mainloop()