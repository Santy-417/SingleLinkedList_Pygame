precio_producto = float(input(" Ingrese el precio: "))
descuento_porcentaje = float(input("Ingrese el descuento: "))

descuento_decimal = descuento_porcentaje/100

precio_final = precio_producto-(precio_producto*descuento_decimal)

print(" El precio final es:", precio_final)
