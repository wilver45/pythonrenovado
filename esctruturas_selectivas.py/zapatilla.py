#las variables de obtoner los datos del usuario
cantidad_de_zapatillas=int(input("ingrese la cantidad de zapatillas"))
valor_de_compras=float(input("ingrese valor de compras"))
valor_del_descuento=float(input("ingrese valor de descuento de compras"))

#calculando el descuento   
descuento = (valor_del_descuento * cantidad_de_zapatillas) / 100
# Convertir el valor a decimal
descuento_decimal = valor_del_descuento / 100

#calculando el valor final
valor_final = valor_de_compras - descuento

#mostrando el resultado

print("El valor final de la compra es:", valor_final)
print("La cantidad de zapatillas es:", cantidad_de_zapatillas)
print("El valor de compras es:", valor_de_compras)
print("El valor de descuento es:", valor_del_descuento)