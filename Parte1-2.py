# Javier Carpio
# Gustavo de Leon

# Parte 1
# Receptor

# Librerias para uso de sockets y serializacion
import socket, pickle   

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

# Cerrar conexion
s.close() 
