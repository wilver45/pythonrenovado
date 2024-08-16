#Construya un algoritmo que calcule el sueldo total de un vendedor, dado su sueldo base y las
#comisiones de sus ventas. Para esto es necesario definir una variable que almacene el nombre del
#vendedor, una variable que almacene el sueldo y otra variable que almacene el valor de la comisión
#de las ventas realizadas. Se debe calcular el valor final de sueldo. El algoritmo debe imprimir el
#nombre del vendedor, el valor del sueldo, el valor de su comisión y el sueldo total del vendedor.

#la vartiable de Pedir al usuario los datos
nombre_del_vendedor=input("Vendedor: ")
sueldo_del_vendedor=int(input("sueldo: "))
valor_de_la_comision=int(input("comision: "))
#la varibale del total sueldo
sueldo_total=sueldo_del_vendedor+valor_de_la_comision
# imprimir los datos ya calculados y puestos
print("nombre del vendor: {0} su sueldo es: {3} su comision: {1} y su suedlo total es: {2}".format(nombre_del_vendedor, valor_de_la_comision, sueldo_total, sueldo_del_vendedor))
