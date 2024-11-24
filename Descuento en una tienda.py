# Programa que calcula el monto final con descuento si el gasto es mayor a $100
def descuento_en_tienda():
    gasto = float(input("Ingresa el monto del gasto: $"))
    if gasto > 100:
        monto_final = gasto * 0.8  # Aplicar un descuento del 20%
    else:
        monto_final = gasto  # Sin descuento
    print(f"Monto final: ${monto_final:.2f}")

descuento_en_tienda()
