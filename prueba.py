nota_parcial = float(input('Ingrese la nota parcial: \n'))
nota_final = float(input('Ingrese la nota final: \n'))

puntaje = 0.6 * nota_parcial + 0.4 * nota_final
nota = 0

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
    
print ("El puntaje es ",puntaje)
print ("La nota es ", nota)