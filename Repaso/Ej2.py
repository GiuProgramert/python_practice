n1 = int(input("Ingrese la cantidad de elementos de L1: "))
n2 = int(input("Ingrese la cantidad de elementos de L2: "))
n3 = int(input("Ingrese la cantidad de elementos de l3: "))

l1 = []
l2 = []
l3 = []

for i in range(n1):
  elemento = int(input("Ingrese el elemento de la lista L1: "))
  l1.append(elemento)

for i in range(n2):
  elemento = int(input("Ingrese el elemento de la lista L2: "))
  l2.append(elemento)

for i in range(n3):
  elemento = int(input("Ingrese el elemento de la lista L3: "))
  l3.append(elemento)

n = n1 + n2 + n3
n1 -= 1
n2 -= 1
n3 -= 1

print("La lista sin modificar es: ", l1, l2, l3)

#k: el valor para que no salga de rango al comparar con el otro vector de el frente
#s: el valor para que el vector actual no salga de rango
for i in range(n - 1):
  for j in range (i + 1, n):
    #Compara entre L1
    if j <= n1 and i <= n1:
      if l1[j] < l1[i]:
        l1[j], l1[i] = l1[i], l1[j]
    #Compara entre L1 y L2
    #n1 < j and j <= n2
    elif (n1 < j and j <= (n2 + n1 + 1)) and i <= n1:
      k = j - (n1 + 1)
      if l2[k] < l1[i]:
        l1[i], l2[k] = l2[k], l1[i]
    #Compara entre L1 y L3
    elif j > (n2 + n1) and i <= n1:
      k = j - ((n1 + 1) + (n2 + 1))
      if l3[k] < l1[i]:
        l1[i], l3[k] = l3[k], l1[i]
    #Compara entre L2 y L2
    #n1 < i and i <= n2 
    elif (n1 < i and i <= (n2 + n1) ) and j <= (n2 + n1):
      k = j - (n1 + 1)
      s = i - (n1 + 1)
      if l2[k] < l2[s]:
        l2[s], l2[k] = l2[k], l2[s]
    #Compara entre L2 y L3
    elif (n1 < i and i <= (n2 + n1 + 1)) and j > (n2 + n1):
      k = j - ((n1 + 1) + (n2 + 1))
      s = i - (n1 + 1)
      if l3[k] < l2[s]:
        l2[s], l3[k] = l3[k], l2[s]
    #Compara entre L3 y L3
    elif i > (n2 + n1) and j > (n2 + n1):
      s = i - ((n1 + 1) + (n2 + 1))
      k = j - ((n1 + 1) + (n2 + 1))
      if l3[k] < l3[s]:
        l3[s], l3[k] = l3[k], l3[s]

print("La listas modificada son: ", l1, l2, l3)