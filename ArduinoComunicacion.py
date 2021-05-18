
import serial

# Inicializamos el puerto de serie a 9600 baud
# Escogemos el puerto depende de dondes se haya conectado,se verifica en el programa del arduino

comunicacion = serial.Serial('COM3', 9600)

# Lista de comandos para controlar el Led
print("OPCIONES : \n 'e' - Led (ON) \n 'a' - Led (OFF) \n 'q' - Salir \n")

#Opciones del programa
print("Introduce una opcion : ")

# Guardamos este caracter en una variable
entrada = input()

# Introduciendo 's' salimos del bucleq
while entrada != 'q':
    # Envio de datos y codificacion en Unicode
    comunicacion.write(str(entrada).encode())
    # Y pedimos un nuevo caracter al usuario
    print("Introduce una opcion: ")
    entrada = input()