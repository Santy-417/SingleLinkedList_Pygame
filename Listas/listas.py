class Listas:
    def __init__(self):
        self.lista_animales = []
    def menu_opciones(self):
        while True:
            try:
                opcion_menu = int(input('Seleccione una opción:\n           1. Añadir animal a la lista\n           2. Eliminar animal de la lista\n           3. Consultar cantidad de animales creados\n           >>'))
                while True:
                    if (opcion_menu != 1 and opcion_menu !=2 and opcion_menu !=3):
                        print('Opción inválida')
                        opcion_menu = int(input("   >>"))
                    elif opcion_menu == 1:
                        self.crear_animales()
                        self.menu_opciones()
                        break
                    elif opcion_menu == 2:
                        if len(self.lista_animales) > 0:
                            self.eliminar_animales()
                            self.menu_opciones()
                            break
                        else:
                            print('La lista se encuentra vacía')
                            self.crear_animales()
                            self.eliminar_animales()
                            self.menu_opciones()
                            break
                    else:
                        self.contar_total_animales()
                        break
                break
            except ValueError:
                print(' >> Error <<')
                break
    def crear_animales(self):
        print('         >> REGISTRO DE ANIMALES <<')
        cantidad_animales = input('¿Cúantos animales deseas agregar?')
        if cantidad_animales.isnumeric() == True:
            for animal in range(int(cantidad_animales)):
                nombre_animal = input('     Animal >>')
                while True:
                    try:
                        indice = int(input('¿En qué posición de la lista?\n           1. Primera\n           2. Última\n           3. Indice específico\n           '))
                        while True:    
                            if (indice != 1 and indice !=2 and indice !=3):
                                print('Opción inválida')
                                indice= int(input('     >>'))
                            elif indice == 1:
                                self.lista_animales.insert(0, nombre_animal)
                                print(self.lista_animales)
                                break
                            elif indice == 2:
                                self.lista_animales.append(nombre_animal)
                                print(self.lista_animales)
                                break
                            else:
                                while True:
                                    try:
                                        nro_indice = int(input('     Indice de la lista >>'))
                                        if nro_indice < 0 or nro_indice > len(self.lista_animales):
                                            print('     >> El indice fuera de rango <<')
                                        else:
                                            self.lista_animales.insert(nro_indice, nombre_animal)
                                            print(self.lista_animales)
                                    except ValueError:
                                        print('El indice debe ser un nro')
                                    break
                                break
                        break
                    except ValueError:
                        print(' >> Error <<')
                        break
        else:
            print('No es número')
        
    def eliminar_animales(self):
        print('Seleccionaste la opción 2 del menú')
        while True:
            try:
                indice = int(input('Selecciona que eliminar \n           1. Primera\n           2. Última\n           3. Indice específico\n           4. Todos los elementos de la lista\n           5. Buscar por nombre y eliminar\n           6. Eliminar valores duplicados\n        7. Eliminar todas las coincidencias de un animal en la lista\n      >>>'))
                while True:    
                    if indice != 1 and indice !=2 and indice !=3  and indice !=4  and indice !=5 and indice!=6 and indice!=7:
                        print('Opción inválida')
                        indice= int(input('     >>'))
                    elif indice == 1:
                        print('Eliminando el primer animal de la lista')
                        self.lista_animales.pop(0)
                        print(self.lista_animales)
                        break
                    elif indice == 2:
                        print('Eliminando el último animal de la lista')
                        self.lista_animales.pop()
                        print(self.lista_animales)
                        break
                    elif indice == 3:
                        print('Posición intermedia:')
                        while True:
                            try:
                                nro_indice = int(input('     Indice de la lista >>'))
                                while True:
                                    if nro_indice < 0 or nro_indice >= len(self.lista_animales):
                                        print('     >> El indice fuera de rango <<')
                                        nro_indice = int(input('     >>>'))
                                    else:
                                        self.lista_animales.pop(nro_indice)
                                        print(self.lista_animales)
                                        break
                                    break
                            except ValueError:
                                print('El indice debe ser un nro')
                            break
                        break
                    elif indice == 4:
                        self.lista_animales.clear()
                        print(self.lista_animales)
                        break
                    elif indice==5:
                        animal = input('       Anima a eliminar\n       ')
                        print(" Buscando ")
                        self.lista_animales.remove(animal)
                        print(self.lista_animales)
                        break
                    elif indice==6:
                        lista_sin_duplicados = list(set(self.lista_animales))
                        print(lista_sin_duplicados)
                        break
                    else:
                        animal = input('       Anima a eliminar\n       ')
                        print(" Buscando ")
                        nueva_lista = list(filter((animal).__ne__,self.lista_animales))
                        print(nueva_lista)
                        break
                break
            except ValueError:
                print(' >> Error <<')
                break   
    def contar_total_animales(self):
        print('Seleccionaste la opción 3 del menú')
        print("----------------------------------")
        print(len(self.lista_animales))
        while True:
            try:
                opccion_menu = int(input("      1. Ver los primeros tres animales\n     2. Ver los ultimos tres animales\n      3. Ver el ultimo animal\n       "))
                if (opccion_menu !=1 and opccion_menu !=2 and opccion_menu !=3):
                    print(" Opcion incorrecta")
                    opccion_menu = int(input("      >>"))
                elif opccion_menu ==1:
                    if len(self.lista_animales) >=3:
                        print(self.lista_animales[0:4])
                    else:
                        print(" La lsita tiene menos de 3 elementos. ")
                    break
                elif opccion_menu ==2:
                    if len(self.lista_animales) >=3:
                        print(self.lista_animales[-4:-1])
                    else:
                        print(" La lsita tiene mas de 3 elementos. ")
                        break
                else:
                    print(self.lista_animales[-1])
                    break
            except ValueError:
                print(" Valor incorrecto")
                break

listas = Listas()
listas.menu_opciones()