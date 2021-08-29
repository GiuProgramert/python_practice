# Se cuenta con una lista, ordenada ascendentemente, de las matrículas de N alumnos inscriptos para el
# semestre. Al final de esta lista se han agregado P matrículas de alumnos que se han inscripto
# tardíamente. Seleccionar el método de ordenamiento más adecuado y escribir un algoritmo que reciba y
# ordene la lista completa de (N+P) alumnos en forma ascendente.

n = int(input("Introduzca la cantidad N de matriculas: \n"))
p = int(input("Introduzca la cantidad P de matriculas tardias: \n"))

lista_n = []
lista_p = []

for i in range(n):
  elemento = int(input("Introduzca las matriculas de los primeros N alumnos: "))
  lista_n.append(elemento)

for i in range(p):
  elemento = int(input("Introduzca las matriculas tardias de los P alumnos: "))
  lista_p.append(elemento)

cambio = True
j = -1
while cambio:
  cambio = False
  j += 1
  for i in range(n-j-1):
    if lista_n[i + 1] < lista_n[i]:
      lista_n[i], lista_n[i + 1] = lista_n[i + 1], lista_n[i]
      cambio = True

cambio = True
j = -1
while cambio:
  cambio = False
  j += 1
  for i in range(p-j-1):
    if lista_p[i + 1] < lista_p[i]:
      lista_p[i], lista_p[i + 1] = lista_p[i + 1], lista_p[i]
      cambio = True

n_p = []
for i in range(n):
  n_p.append(lista_n[i])

for i in range(p):
  n_p.append(lista_p[i])

cambio = True
j = -1
while cambio:
  cambio = False
  j += 1
  for i in range(n + p - j - 1):
    if n_p[i + 1] < n_p[i]:
      n_p[i], n_p[i + 1] = n_p[i + 1], n_p[i]
      cambio = True

print("Lista N + P = ", *n_p)