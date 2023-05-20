import os

carpeta = input(" Ingrese donde se encuentra la carpeta: ")
extension = input(" Ingrese la extensión de archivo a buscar (.pdf): ")

archivos_encontrados = []
for raiz, directorios, archivos in os.walk(carpeta):
    for archivo in archivos:
        if archivo.endswith("." + extension):
            archivos_encontrados.append(os.path.join(raiz, archivo))

if len(archivos_encontrados) > 0:
    print(" Los archivos son:")
    for archivo in archivos_encontrados:
        print(archivo)
else:
    print(" No se encontraron archivos con esa referencia. ")
