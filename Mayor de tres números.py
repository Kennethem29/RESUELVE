# Programa que determina el mayor de tres números
def mayor_de_tres_numeros():
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    num3 = float(input("Ingresa el tercer número: "))
    
    mayor = max(num1, num2, num3)  # Usa la función max para encontrar el mayor
    print(f"El número mayor es {mayor}")

mayor_de_tres_numeros()
