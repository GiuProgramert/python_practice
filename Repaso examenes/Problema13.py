# texto = input("Ingrese el texto que desea codificar")
# clave = int(input("Ingrese el valor de la clave: "))


texto = "REPLEGAR 07"
clave = 2

def obtener_caracter_abc(posicion):
    if posicion + clave < len(abc):
        return abc[posicion + clave]
    
    return abc[(posicion + clave) - len(abc) + 1]

inicio = 0
def obtener_caracter_texto(texto, n, antiguo_caracter):
    caracter = ""
    i = 0
    if antiguo_caracter != 0:
        j = antiguo_caracter + 1
    else:
        j = 0 

    while i < n:
        if j > len(texto) - 1:
            j = 0

        if antiguo_caracter == 0:
            caracter = j
            i = i + 1
            j = j + 1
        else:    
            if j != antiguo_caracter:
                caracter = j
                i = i + 1
                j = j + 1
            else:
                j = j + 1

    return caracter

def quitar_caracter(texto, antiguo_caracter):
    return texto[0:antiguo_caracter:1] + texto[antiguo_caracter + 1:len(texto):1]

abc = [
    0  , 'A', 'B', 'C', 'D', 
    'E', 'F', 'G', 'H', 'I', 
    'J', 'K', 'L', 'M', 'N', 
    'Ñ', 'O', 'P', 'Q', 'R', 
    'S', 'T', 'U', 'V', 'W', 
    'X', 'Y', 'Z', '0', '1', 
    '2', '3', '4', '5', '6', 
    '7', '8', '9', ' '
]

codificado = ""
n = clave
caracter = obtener_caracter_texto(texto, n, 0)

while len(texto) > 0:
    print(len(texto))
    codificado = codificado + obtener_caracter_abc(abc.index(texto[caracter]))
    n = abc.index(texto[caracter])
    copia_caracter = caracter

    caracter = obtener_caracter_texto(texto, n, caracter)
    if caracter > copia_caracter:
        caracter = caracter - 1

    texto = quitar_caracter(texto, copia_caracter)

print(codificado)