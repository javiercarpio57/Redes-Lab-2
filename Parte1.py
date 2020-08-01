# Javier Carpio
# Gustavo de Leon

# Parte 1
# Emisor

# Librerias para uso de bitarray, sockets y serializacion
import socket, pickle   
from bitarray import bitarray

# Metodo para convertir de String a Binario
def toBinary(msj):
    print("Mensaje: "+msj)
    msj = ' '.join(format(ord(x), 'b') for x in msj)
    msj = msj.replace(" ", "0")
    print("Mensaje Binario: "+ msj)
    return msj

# Host y puerto
host = 'local host'
port = 5004

# Creacion de socket y conexion
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind(('', port)) 
s.listen(1)    
c, addr = s.accept() 

# Ingreso de Mensaje
msj = input("Ingrese su mensaje: ")

# Conversion
es = toBinary(msj)
ba = bitarray(es)

#Serializacion
data_string = pickle.dumps(ba)

# Mandando bitarray
c.send(data_string) 

# Cerrar conexion
c.close() 
