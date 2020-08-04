# Javier Carpio
# Gustavo de Leon

# Parte 1
# Receptor

# Librerias para uso de sockets y serializacion
import socket, pickle
from bitarray import bitarray
import fletcher_checksum as check

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
    print("Recibiendo objeto: ",data_variable)
    msg = s.recv(1024) 

string = data_variable.to01()
print(string)

groups = [string[i:i+8] for i in range(0, len(string), 8)]
if( check.check_checksum(groups)):
    print("cadena buena")
else:
    print("cadena mala")
    data = string[:-8]
    codeHamming = check.CodificarHamming(data)
    


# Cerrar conexion
s.close() 
