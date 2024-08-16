#las variables de obtoner los datos del usuario
monto_de_la_compra=float(input("La Compra: "))
# Definir las variables para los porcentajes de inversión
porcentaje_inversion_propia = 0.55
porcentaje_prestamo_bancario = 0.30
porcentaje_credito_fabricante = 0.15
#defenir las variables de obtoner los datos asginados por las variables
if monto_de_la_compra > 500000:
    inversion_propia = monto_de_la_compra * porcentaje_inversion_propia
    prestamo_bancario = monto_de_la_compra * porcentaje_prestamo_bancario
    credito_fabricante = monto_de_la_compra * porcentaje_credito_fabricante
else:
    inversion_propia = monto_de_la_compra
    prestamo_bancario = 0
    credito_fabricante = 0

# Imprimir los resultados
print(f"Monto total de la compra: ${monto_de_la_compra:.2f}")
print(f"Inversión propia: ${inversion_propia:.2f} ({porcentaje_inversion_propia * 100:.0f}%)")
print(f"Préstamo bancario: ${prestamo_bancario:.2f} ({porcentaje_prestamo_bancario * 100:.0f}%)")
print(f"Crédito al fabricante: ${credito_fabricante:.2f} ({porcentaje_credito_fabricante * 100:.0f}%)")