# Programa de una calculadora básica
def calculadora_basica():
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    operacion = input("Ingresa la operación (+, -, *, /): ")

    if operacion == '+':
        resultado = num1 + num2
    elif operacion == '-':
        resultado = num1 - num2
    elif operacion == '*':
        resultado = num1 * num2
    elif operacion == '/':
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Error: División entre cero no permitida")
            return
    else:
        print("Operación no válida")
        return
    
    print(f"Resultado: {resultado}")

calculadora_basica()
