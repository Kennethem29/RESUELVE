# Programa que determina si un número es par o impar
def par_o_impar():
    numero = int(input("Ingresa un número entero: "))
    if numero % 2 == 0:
        print("Es par")
    else:
        print("Es impar")

par_o_impar()
