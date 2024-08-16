#las variables de obtoner los datos del usuario
nombre_del_estudiante=input("escriba el nombre del estudiante")
actividades_promedio=float(input("la calificacion de las actividades "))
proyecto_final=float(input("la calificacion del proyecto final "))
parciales_promedio=float(input("la calificacion de las parciales "))

#variable para calcular el valor de la calificación final
nota_final=(actividades_promedio*0.30)+(proyecto_final*0.50)+(parciales_promedio*0.20)/3
#la impresion de la calificacion y la variable par la nota calificacion
if nota_final >= 70:
    print(f"{nombre_del_estudiante}, su promedio es {nota_final:.1f}, su calificacion es aceptable")
elif nota_final <= 70:
    print(f"{nombre_del_estudiante}, su promedio es {nota_final:.1f}, su calificacion es reprobo")