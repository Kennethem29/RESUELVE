# Programa para convertir una calificación numérica a letra
def sistema_calificaciones():
    calificacion = float(input("Ingresa tu calificación: "))

    if 90 <= calificacion <= 100:
        letra = "A"
    elif 80 <= calificacion < 90:
        letra = "B"
    elif 70 <= calificacion < 80:
        letra = "C"
    elif 60 <= calificacion < 70:
        letra = "D"
    elif calificacion < 60:
        letra = "F"
    else:
        print("Calificación no válida")
        return

    print(f"Tu calificación es {letra}")

sistema_calificaciones()
