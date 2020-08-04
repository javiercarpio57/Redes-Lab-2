# Javier Carpio
# Gustavo de Leon

# Parte 1
# Emisor

# Librerias para uso de bitarray, sockets y serializacion
import socket, pickle   
from bitarray import bitarray
import random

# Metodo para convertir de String a Binario
def toBinary(msj):
    print("Mensaje: "+msj)
    msj = ' '.join(format(ord(x), 'b') for x in msj)
    msj = msj.replace(" ", "0")
    msj = "0"+msj
    print("Mensaje Binario: "+ msj)
    return msj

# Host y puerto
host = 'local host'
port = 5003

# Creacion de socket y conexion
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind(('', port)) 
s.listen(1)    
c, addr = s.accept() 

# Ingreso de Mensaje
msj = input("Ingrese su mensaje: ")
prop = input("Ingrese tasa de ruido cada 100 bits (De 0 a 100):")

print("Se tendra una probabilidad de ", int(prop)/100, " de tener ruido en cada bit")

# Conversion
es = toBinary(msj)
ba = bitarray(es)

cont = 0
bitsC = []
for i in range(len(ba)):
    randNumber = random.randrange(1, 100)
    if (randNumber < int(prop)):
        if(ba[i]):
            ba[i] = 0
            print("Se cambio el bit ", i)
            cont+=1
            bitsC.append(i)
        else:
            ba[i] = 1
            print("Se cambio el bit ", i)
            cont+=1
            bitsC.append(i)

print("Numero de bits cambiados ", cont)

if(cont > 0):
    print("El nuevo BitArray es de: ",ba)
    print("Bits cambiados: ", bitsC)
else:
    print("No hubo ruido, el BitArray sigue igual")


#Serializacion
data_string = pickle.dumps(ba)

# Mandando bitarray
c.send(data_string) 

# Cerrar conexion
c.close() 















