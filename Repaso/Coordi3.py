print("|Elementos intercalados|")

n = 19

lista = []

for i in range(n):
    lista.append(0)

print(len(lista))

contador_derecho = 0
contador_izquierdo = n - 1
carga_derecho = True
i = 0

while contador_derecho <= contador_izquierdo:
    i += 1
    if carga_derecho:
        lista[contador_derecho] = i
        carga_derecho = False
        contador_derecho = contador_derecho + 1
    else:
        lista[contador_izquierdo] = i
        carga_derecho = True
        contador_izquierdo = contador_izquierdo - 1


print(lista)
