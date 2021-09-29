lista = [5, 4, 2, 1, 3]
k = 1 

def secuential_search(lista, k):
  pos_k = -1
  i = 0

  while pos_k == -1 and i < 5:
    if lista[i] == k:
      pos_k = i
    i = i + 1
  
  return pos_k

def shell_sort(lista):
  #Ordenar lista
  salto = int(5 / 2)
  while salto >= 1:
    i = 0
    cambio = False
    while (i + salto) <= 4:
      if lista[i] > lista[i + salto]:
        lista[i], lista[i + salto] = lista[i + salto], lista[i]
        cambio = True
      i = i + 1
    
    if not cambio:
      salto = int(salto / 2)
  
  return lista

def binary_search(lista, k):
  inicio = 0
  fin = 4
  medio = int((inicio + fin) / 2)

  while lista[medio] != k and inicio <= fin:
    if lista[medio] > k:
      fin = medio - 1
    else:
      inicio = medio + 1  
    medio = int((inicio + fin) / 2)

  pos_k = -1
  if lista[medio] == k:
    pos_k = medio

  return pos_k
  
print("Búsqueda secuencial: elemento encontrado en la posición", secuential_search(lista, k) + 1)
print("Búsqueda binaria: elemento encontrado en la posición", binary_search(shell_sort(lista), k) + 1)