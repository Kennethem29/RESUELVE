# Programa que determina si un número es mayor o menor que 10
def mayor_o_menor():
    numero = float(input("Ingresa un número: "))
    if numero > 10:
        print("Es mayor que 10")
    elif numero < 10:
        print("Es menor que 10")
    else:
        print("Es igual a 10")

mayor_o_menor()
