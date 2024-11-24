# Programa que clasifica al usuario según su edad
def clasificacion_de_edades():
    edad = int(input("Ingresa tu edad: "))
    if 0 <= edad <= 12:
        print("Eres un niño")
    elif 13 <= edad <= 17:
        print("Eres adolescente")
    elif edad >= 18:
        print("Eres adulto")
    else:
        print("Edad no válida")

clasificacion_de_edades()
