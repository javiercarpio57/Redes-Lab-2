import math

def CalcularBitsRedundantes(longitud):
    for i in range(longitud):
        if 2**i >= longitud + i + 1:
            return i

def PosicionBitsRedundantes(palabra, bits):
    j = 0
    k = 1
    longitud = len(palabra)
    respuesta = ''

    for i in range(1, longitud + bits + 1):
        if i == 2**j:
            respuesta += '0'
            j += 1
        else:
            respuesta += palabra[-1 * k]
            k += 1

    return respuesta[::-1]

def CalcularParidadBits(info, bits):
    n = len(info)

    for i in range(bits):
        val = 0
        for j in range(1, n + 1):
            if j & (2**i) == 2**i:
                val = val ^ int(info[-1 * j])

        info = info[:n - (2**i)] + str(val) + info[n - (2**i) + 1:]
    return info

def EncontrarError(palabra, bits):
    n = len(palabra)
    res = 0

    for i in range(bits):
        val = 0
        for j in range(1, n + 1):
            if j & (2**i) == 2**i:
                val = val ^ int(palabra[-1 * j])

        res = res + val * (10**i)
    return int(str(res), 2)

def Corregir(palabra, posicion):
    eliminar = len(palabra) - posicion
    palabra = palabra[:eliminar] + str((int(palabra[eliminar]) + 1) % 2) + palabra[eliminar + 1:]
    return palabra

def CodificarHamming(palabra):
    m = len(palabra) 
    r = CalcularBitsRedundantes(m)
    arr = PosicionBitsRedundantes(palabra, r) 
    arr = CalcularParidadBits(arr, r) 

    return arr

def DecodificarHamming(palabra):
    largoOriginal = len(palabra)
    cont = math.floor(math.log2(len(palabra)))
    i = 0

    while i <= cont:
        pos = largoOriginal - 2**i
        palabra = palabra[: pos] + palabra[pos + 1:]

        i += 1

    return palabra


# data = '01101000'
# codeHamming = CodificarHamming(data)
# print("Data en HAMMING es\t" + codeHamming)  


# arr = '011001001110'
# r = CalcularBitsRedundantes(len(arr) - math.ceil(math.log2(len(arr))))
# print(r)
# print("Error Data is\t\t" + arr) 

# correction = EncontrarError(arr, r) 
# print("Posicion del error " + str(correction)) 

# corregido = Corregir(arr, correction)
# print("CORREGIDO:\t\t" + str(corregido))
# print('REAL:\t', data)

# limpio = DecodificarHamming(corregido)
# print('DECODE:\t', limpio)