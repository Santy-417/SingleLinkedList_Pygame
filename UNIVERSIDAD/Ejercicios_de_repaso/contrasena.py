import random
import string

def generar_contrasena(longitud):

    caracter = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracter)for i in range (longitud))
    contrasena = generar_contrasena(longitud)
    print("Contraseña generada: ",contrasena)

longitud = int(input("ingrese la longitud de la contraseña: "))
