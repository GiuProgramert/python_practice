palabra = input("Ingrese la palabra a ser decodificada: ")

alfabeto = "abcdefghijklmnñopqrstuvwxyz"
alfabeto_codigo = "bcdebcdefghijklmnñopqrstuvwxyza"

palabra_decodificada = ""

for caracter in palabra:
    palabra_decodificada += alfabeto[alfabeto_codigo.find(caracter)]


print(palabra_decodificada)