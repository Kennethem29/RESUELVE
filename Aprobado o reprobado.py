# Programa que determina si un estudiante está aprobado o reprobado
def aprobado_o_reprobado():
    calificacion = float(input("Ingresa la calificación del estudiante: "))
    if calificacion >= 7:
        print("Aprobado")
    else:
        print("Reprobado")

aprobado_o_reprobado()
