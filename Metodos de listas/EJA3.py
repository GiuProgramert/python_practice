productos = []
nuevos = []
viejos = []

productos_actualizada = []
len_productos = int(input("Introduzca la cantidad de productos: "))
len_nuevos = int(input("Introduzca la cantidad de productos nuevos: "))
len_viejos = int(input("Introduzca la cantidad de productos viejos: "))

for i in range(len_productos):
    productos.append(int(input("Introduzca el código del producto: ")))

for i in range(len_nuevos):
    nuevos.append(int(input("Introduzca el código del producto: ")))

for i in range(len_viejos):
    viejos.append(int(input("Introduzca el código del producto: ")))

for i in range(len_nuevos):
    productos.append(nuevos[i])

for i in range(len_viejos):
    productos.remove(viejos[i])

print(productos)