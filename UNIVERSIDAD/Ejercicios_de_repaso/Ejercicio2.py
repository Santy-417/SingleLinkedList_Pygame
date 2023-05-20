numero = int(input(" Ingrese la tabla que quiere calcular: "))

print(" La tabla de multiplicar es: ")
for i in range(1, 11):
    resultado = numero * i
    print(numero, " x ", i, " = ", resultado)
