# Programa para adivinar un número aleatorio
import random

def juego_numeros():
    numero_aleatorio = random.randint(1, 10)
    intento = int(input("Adivina el número (entre 1 y 10): "))

    if intento == numero_aleatorio:
        print("¡Felicidades, acertaste!")
    else:
        print(f"Intenta de nuevo. El número era {numero_aleatorio}")

juego_numeros()
