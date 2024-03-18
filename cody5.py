def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Llamadas a la función calcular_descuento
monto_compra1 = 1000
descuento1 = calcular_descuento(monto_compra1)
monto_final1 = monto_compra1 - descuento1

monto_compra2 = 1500
porcentaje_descuento2 = 15
descuento2 = calcular_descuento(monto_compra2, porcentaje_descuento2)
monto_final2 = monto_compra2 - descuento2

# Mostrar resultados
print(f"Monto de la compra 1: ${monto_compra1}")
print(f"Descuento aplicado 1: ${descuento1}")
print(f"Monto final a pagar 1: ${monto_final1}\n")

print(f"Monto de la compra 2: ${monto_compra2}")
print(f"Descuento aplicado 2: ${descuento2}")
print(f"Monto final a pagar 2: ${monto_final2}")

