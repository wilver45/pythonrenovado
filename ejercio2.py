#Construya un algoritmo que calcule el perímetro y el área de un rectángulo dada su base y su altura.
#La base y la altura deberán ser almacenadas previamente en dos variables respectivamente. El
#algoritmo debe mostrar en pantalla el siguiente mensaje: El perímetro del rectángulo es: xxx el área
#del rectángulo es: yyyy

#vaarible de la base y la altura
base=int(input("introduzca el numero de la base del rectagulo "))
altura=int(input("introduzca el numero de la area  del rectagulo "))

# Calculamos el perimetro
perimetro = 2 * (base + altura)
area = base + altura
# Mostramos los resultados de la base y la altura
print("El perimetro del rectangulo es:", perimetro)
print("El area del rectangulo es:", area)


