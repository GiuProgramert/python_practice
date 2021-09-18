print("Hallar una lista de p números primos mayores a 1000")

p = int(input("Introduzca el valor de p: "))

PRUEBA = []
for i in range(1000, p + 1):
  es_primo = True
  
  for j in range(2, i):
    if (i % j) == 0:
      es_primo = False
  
  if es_primo:
    PRUEBA.append(i)


print("Los números primos desde 1000 hasta", p, "son", PRUEBA)