# Para elaborar la planilla de evaluación de un curso de N alumnos, se requiere un algoritmo que
# reciba como datos para cada alumno: a) nota obtenida en el examen parcial; y b) nota
# obtenida en el examen final. A partir de estos elementos, se debe calcular la nota final para
# cada alumno y el promedio general del curso.
# El procedimiento de cálculo es el siguiente:
# Calificación = 0.4 (nota examen parcial) + 0.6 (nota examen final)
# Calificación Nota final
# 0 – 59 = 1
# 60 – 69 = 2
# 70 – 79 = 3
# 80 – 89 = 4
# 90 – 100 = 5

#pedir cantidad de alumnos
cantidad_alumnos = int(input("Introduzca la cantidad de N alumnos: "))
suma_promedio_puntajes = 0
suma_promedio_notas = 0

#Calcular notas de alumnos
for i in range(cantidad_alumnos):
  print("Estudiante número: ", i + 1)
  nota_examen_parcial = int(input("Introduzca la nota del examen parcial: "))
  nota_examen_final = int(input("Introduzca la nota del examen final: "))
  puntaje = 0.4 * nota_examen_parcial + 0.6 * nota_examen_final

  if puntaje >= 90:
    nota = 5
  elif puntaje >= 80:
    nota = 4
  elif puntaje >= 70:
    nota = 3
  elif puntaje >= 60:
    nota = 2
  else:
    nota = 1
  
  print(f"La nota del estudiante número {i + 1} es {nota} y su puntaje es {puntaje}")
  suma_promedio_puntajes += puntaje
  suma_promedio_notas += nota

#Imprimir promedios
promedio_puntajes = suma_promedio_puntajes / cantidad_alumnos
promedio_notas = suma_promedio_notas / cantidad_alumnos
print("El promedio de puntajes es: ", promedio_puntajes)
print("El promedio de notas es: ", promedio_notas)