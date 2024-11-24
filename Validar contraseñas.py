# Programa para validar una contraseña
def validar_contrasena():
    contrasena_fija = "200629"
    contrasena = input("Ingresa la contraseña: ")
    
    if contrasena == contrasena_fija:
        print("Acceso concedido")
    else:
        print("Contraseña incorrecta")

validar_contrasena()
