#Desarrolle un algoritmo que Programa que calcule el precio final de una compra, dado el valor de la
#compra y un descuento. Para esto es necesario declarar dos variables, una que guarde el valor de la
#compra y otra que almacene el valor del descuento. El algoritmo debe mostrar en pantalla, el valor
#de la compra el valor del descuento y el valor final a pagar.

#variable para pedir los datos de las compras
valor_de_la_compra=int(input("introduzaca el valor de la compra"))
valor_del_descuento=int(input("intoduzaca el valor de descuento"))

# variable para el valor de la compra y descuento
descuento = (valor_de_la_compra * valor_del_descuento) / 100
valor_final = valor_de_la_compra - descuento
#imprimir el resultado 
print("lo que costo la compra del producto {0} con su descuento {1} su valor final seria {2} ".format(valor_de_la_compra, descuento, valor_final)) 