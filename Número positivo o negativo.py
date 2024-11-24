# Programa que determina si un número es positivo, negativo o cero
def positivo_negativo_cero():
    numero = float(input("Ingresa un número: "))
    if numero > 0:
        print("Es un número positivo")
    elif numero < 0:
        print("Es un número negativo")
    else:
        print("El número es cero")

positivo_negativo_cero()
