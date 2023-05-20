import random
import string

def generar_contrasena(longitud):

    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))

longitud = str(input("Ingrese la longitud de la contraseña: "))

contrasena = generar_contrasena(longitud)
print("Contraseña generada: ", contrasena)