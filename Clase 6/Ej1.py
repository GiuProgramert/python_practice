print("Gestion de N notas de una lista de alumnos del curso de algoritmica")

n = int(input("Introduzca la cantidad N de notas:\n"))
notas = []

for i in range(n):
  nota = int(input("Introduzca la nota del alumno " + str(i + 1) + " "))
  notas.append(nota)

menor = notas[1]
mayor = 0

#Calcular la nota de menor puntaje
for i in range(n):
  if nota < menor:
    menor = notas[i]


#Calcular la nota de mayor puntaje
for i in range(n):
  if nota  > mayor:
    mayor = notas[i]

print("La nota de menor puntaje es", menor, "y la nota de mayor puntaje es", mayor)
#Calcular promedio del curso
suma_promedio = 0
for i in range(n):
  suma_promedio = suma_promedio + notas[i]

promedio = suma_promedio / n
menor_promedio = 0
for i in range(n):
  if notas[i] < promedio:
    menor_promedio = menor_promedio + 1

print("El promedio del curso es", promedio, "y la cantidad de notas por debajo del promedio es", menor_promedio)

#Cantidad de notas
contador_notas = [0, 0, 0, 0, 0]
for i in range(n):
  if notas[i] > 80:
    contador_notas[4] = contador_notas[4] + 1
  elif notas[i] > 60:
    contador_notas[3] = contador_notas[3] + 1
  elif notas[i] > 40:
    contador_notas[2] = contador_notas[2] + 1
  elif notas[i] > 20:
    contador_notas[1] = contador_notas[1] + 1
  else:
    contador_notas[0] = contador_notas[0] + 1

print("Categorias de notas")
print("1 - 20 cantidad", contador_notas[0])
print("21 - 40 cantidad", contador_notas[1])
print("41 - 60 cantidad", contador_notas[2])
print("61 - 80 cantidad", contador_notas[3])
print("81 - 100 cantidad", contador_notas[4])
