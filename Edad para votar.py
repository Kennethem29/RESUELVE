# Programa que determina si el usuario puede votar
def edad_para_votar():
    edad = int(input("Ingresa tu edad: "))
    if edad >= 18:
        print("Puedes votar")
    else:
        print("No puedes votar")

edad_para_votar()
