numeros = input(" Ingrese una lista de números (separados con ,): ")

numeros = [int(numero) for numero in numeros.split(",")]

numeros.sort()

print(" La lista ordenada es: ", numeros)
