import random

numero_generado = random.randint(1, 100)

intentos_maximos = 10

for intento_actual in range(1, intentos_maximos + 1):
    print(" Intento ", intento_actual, " de ", intentos_maximos)
    intento = int(input(" Ingrese un número: "))

    if intento == numero_generado:
        print(" Has adivinado el número.")
        break
    elif intento < numero_generado:
        print(" El número es menor. ")
    else:
        print(" El número es mayor. ")

if intento != numero_generado:
    print(" No te quedan mas intentos. ")
    print(" El número era:" , numero_generado)
