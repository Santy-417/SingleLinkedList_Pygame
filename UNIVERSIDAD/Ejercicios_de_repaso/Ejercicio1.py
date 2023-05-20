import datetime

fecha_nacimiento = input(" Ingrese su fecha de nacimiento (DD/MM/AAAA): ")

fecha_actual = datetime.date.today()

fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento, "%d/%m/%Y").date()

edad = fecha_actual.year - fecha_nacimiento.year

if fecha_actual.month < fecha_nacimiento.month or (fecha_actual.month == fecha_nacimiento.month and fecha_actual.day < fecha_nacimiento.day):
    edad -= 1

print(" Su edad es: ", edad, " años. ")
