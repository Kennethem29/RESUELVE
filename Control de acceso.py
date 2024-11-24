# Programa para validar nombre de usuario y contraseña con tres intentos
def control_de_acceso():
    usuario_fijo = "kenneth"
    contrasena_fija = "1234"
    intentos = 3

    while intentos > 0:
        usuario = input("Ingresa tu nombre de usuario: ")
        contrasena = input("Ingresa tu contraseña: ")

        if usuario == usuario_fijo and contrasena == contrasena_fija:
            print(f"Bienvenido, {usuario}.")
            return
        else:
            intentos -= 1
            print(f"Usuario o contraseña incorrectos. Te quedan {intentos} intentos.")

    print("Acceso bloqueado. Intenta más tarde.")

control_de_acceso()
