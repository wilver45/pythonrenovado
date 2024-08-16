nombre_del_estudiante=input("escriba el nombre del estudiante")
actividades_promedio=float(input("la calificacion de las actividades "))
proyecto_final=float(input("la calificacion del proyecto final "))
parciales_promedio=float(input("la calificacion de las parciales "))

nota_final=(actividades_promedio*0.30)+(proyecto_final*0.50)+(parciales_promedio*0.20)/3

if nota_final >= 90:
    print(f"{nombre_del_estudiante}, su promedio es {nota_final}, su calificacion es superior")

elif nota_final >= 80:
    print(f"{nombre_del_estudiante}, su promedio es {nota_final}, su calificacion es alto")

elif nota_final >= 70:
    print(f"{nombre_del_estudiante}, su promedio es {nota_final}, su calificacion es aceptable")
else: nota_final <=60
print(f"{nombre_del_estudiante}, su promedio es {nota_final}, su calificacion es bajo")
