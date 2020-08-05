# Javier Carpio
# Gustavo de Leon

# Parte 1
# Receptor

# Librerias para uso de sockets y serializacion
import socket, pickle
from bitarray import bitarray
import fletcher_checksum as check
import hamming as hamming
import math

def decode_binary_string(s):
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))

# Host y puerto
host = 'local host'
port = 5003
   
# Creacion de socket y conexion
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect(('127.0.0.1', port)) 

# Recepcion del mensaje
msg = s.recv(1024) 

# Recibir todo el mensaje
while msg:

    # Pickle para cargar el objeto serializado
    data_variable = pickle.loads(msg)
    msg = s.recv(1024) 

string = data_variable.to01()
print(string)

groups = [string[i:i+8] for i in range(0, len(string), 8)]
if( check.check_checksum(groups)):
    print("cadena buena")
else:
    print("cadena mala")
    data = string[:-8]
    
    # ------------------------------
    groups = [data[i:i+12] for i in range(0, len(data), 12)]
    print(groups)
    corregidos = []
    contador = 0
    for codeHamming in groups:
        r = hamming.CalcularBitsRedundantes(len(codeHamming) - math.ceil(math.log2(len(codeHamming))))

        correction = hamming.EncontrarError(codeHamming, r) 
        print("Posicion del error " + str(correction)) 

        if correction != 0:
            contador += 1
            corregido = hamming.Corregir(codeHamming, correction)
            limpio = hamming.DecodificarHamming(corregido)
        else:
            limpio = hamming.DecodificarHamming(codeHamming)
            
        corregidos.append(limpio)

    print('MENSAJE:', decode_binary_string(''.join(corregidos)))
    print(contador)


    


# Cerrar conexion
s.close() 
