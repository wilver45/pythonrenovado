#lista de las boletas
descuentos_boletas = [
    {"color": "rojo", "descuento": 0.15},
    {"color": "verde", "descuento": 0.20}
]
#datos de la compra hechas por el usuario para la lista
total_compra=float(input('total_compra: '))
#datos del color de la boleta para el descuento del usuario
color_de_la_boleta=input("ingrese el color de la boleta (rojo, verde, otro color: )").strip().lower()
#defenir los valores de los colores para el descuento
if color_de_la_boleta=='rojo': 
    porcentaje_del_descuento=0.15
    
elif color_de_la_boleta=='verde':
    porcentaje_del_descuento=0.20
else:
    porcentaje_del_descuento=0.00
#la varibale para calcular el descuento
descuento=total_compra*porcentaje_del_descuento
#la variable del total de la compra con del descuento
total_con_descuento=total_compra-descuento
#imprimir los resultados
print(f"total de la compra  ${total_compra:.2f}")
print(f"el color de la boleta: {color_de_la_boleta.capitalize()}")
print(f"el valor del descuento ${descuento:.2f}")
print(f"el total con descuento es ${total_con_descuento:.2f}")