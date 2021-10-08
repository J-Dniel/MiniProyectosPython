"""
Proyecto Básico de Python (El Ahorcado).
Basado en el proyecto de: Kylie Ying (@kylieyying). 
Versión en Español con Modificaciones: Estefania Cassingena Navone (@EstefaniaCassN).

Version en Español con pequeña Modificaciones: Julio D Cordero A (@J-Dniel).
"""

import random
import string
import os

from Palabras import *
from VidaAhorcado import vida_visual

def inicio():

    # comprobar la existencia del archivo que contiene las palabra.
    # si el archivo no existe, se crea y se guarda las palabra que tiene la lista.
    if chequearExistencia('palabras.txt') == False:
        guardarPalabras(palabras)

def obtenerPalabraValida(palabras):
    #Seleccionar una palabra al azar en la lista
    palabra = random.choice(palabras)

    #Si la palabra contiene un guion o espacio, selecciona otra palabra al azar
    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)

    return palabra.upper()

def ahorcado():

    palabra = obtenerPalabraValida(LeerArchivo())
    letraPorAdivinar = set(palabra) # Conjunto de letras de la palabra que se va adivinar
    abecedario = set(string.ascii_uppercase) # Abecedario en mayuscula
    letrasAdivinadas = set() # Letra que el usuario ha adivinado durante el juego

    vidas = 7
    #limpieza de pantalla de bienvenida
    os.system('cls')
    # letras pendientes y al jugador le queden vidas.
    while len(letraPorAdivinar) > 0 and vidas > 0:
        # letras adivinadas
        # ' '.join(['a','b','c']) --> 'a b c'
        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letrasAdivinadas)}")

        # Estado actual de la palabra que el jugador debe adivinar (por ejemplo:  H - L A)
        palabraLista = [letra if letra in letrasAdivinadas else '-' for letra in palabra]
        # Muestra la vida del ahorcado
        print(vida_visual[vidas])
        # Muestra las letras separadas por un espacio
        print(f"Palabra: {' '.join(palabraLista)}")

        # El usuario ingresa una letra nueva
        letraUsuario = input('Escoge una Letra: ').upper()

        os.system('cls')
        #Si la letra escogida por el usuario esta en el abecedario
        # y no esta en el conjunto de letras que ya se ha ingresado,
        # se añade la letra al conjunto de letras ingresadas. 
        if letraUsuario in abecedario - letrasAdivinadas:
            letrasAdivinadas.add(letraUsuario)
            # Si la letra está en la palabra, quitar la letra 
            # del conjunto de letras pendientes por adivinar. 
            if letraUsuario in letraPorAdivinar:
                letraPorAdivinar.remove(letraUsuario)
                print('')
            #si la letra no esta en la palabra, quita una vida
            else:
                vidas -= 1
                print(f"\nTu letra, {letraUsuario} no esta en la palabra.")
        #Si la letra escogida por el usuario ya fue ingresada.
        elif letraUsuario in letrasAdivinadas:
            print("\nya escogiste esa letra. por favor escoge una letra nueva.")
        else:
            print("\nEsta letra no es valida.")

    #Se llega a esta linea cuando se agotan la vidas del jugador
    # o cuando se adivinan todas las letras de la palabra
    if vidas == 0:
        print(vida_visual[vidas])
        print(f"\t!Ahorcado! Perdiste.\n\tLo lamento mucho.\n\tLa palabra era: {palabra}")
    else:
        print(f"\t!Excelente!\n\tAdivinaste la palabra: {palabra}!!!!!")

    
if __name__ == "__main__":

    inicio()

    print("----------------------------")
    print("     JUEGO DEL AHORCADO     ")
    print("----------------------------")
    print("     1.---Jugar")
    print("     2.---Agregar palabra")

    select = int(input("::: "))

    while True:
        if select == 1:
            #Comienzo del juego
            ahorcado()
            break
        elif select == 2:
            # Ingresar las nuevas palabras
            p = []
            p.append(input("Escriba una palabra: "))
            opc = ''

            while not(opc == 'NO'):
                opc = input("Desea agregar otra palabra--(SI o NO): ").upper()
                if opc == 'SI':
                    p.append(input("Escriba una palabra: "))
                elif opc == 'NO':
                    os.system('cls')
                    print(f"Palabras Guardadas: {p}")
                    print(f"Cantidad de palabras Guardadas en el juego: {len(LeerArchivo())+len(p)}")
                else:
                    print("\tERROR")
                
    
            guardarPalabras(p)

            break
        else:
            print("ERROR---Opcion Incorrecta")

        select = int(input("::: "))