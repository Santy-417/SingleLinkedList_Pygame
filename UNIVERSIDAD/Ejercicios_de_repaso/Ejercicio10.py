import random

numero_generado = random.randint(1, 100)

intentos = 0

while True:
    intento = int(input("I ngrese un número: "))
    intentos += 1

    if intento == numero_generado:
        print(" !Felicitaciones! Has adivinado el número en ", intentos, " intentos. ")
        break
    elif intento < numero_generado:
        print(" El número es menor. Intenta de nuevo. ")
    else:
        print(" El número es mayor. Intenta de nuevo. ")
