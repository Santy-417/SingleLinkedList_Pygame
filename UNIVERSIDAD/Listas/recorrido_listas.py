import random
class Recorridolistas:
    def __init__(self):
        self.lista_valores = list()
    def agregarValoreslista(self):
        cantidad_valores = input ('Cantidad de valores a añadir: ')
        if cantidad_valores.isnumeric() == True:
            for i in range (1,(int(cantidad_valores))+1):
                self.lista_valores.append(random.randint(1,500))
            print(self.lista_valores)
            posicion_consultar = input(' Indice: ')
            if int(posicion_consultar) > 0 and int(posicion_consultar) <=len(self.lista_valores):
                #print(int(posicion_consultar))
                print(self.lista_valores[(int(posicion_consultar))-1])
            else:
                print('Indice fuera del ranog de la lista.')
            indice_inicial = input('Indice inicial: ')
            indice_final = input(' Inidice final: ')
            if int(indice_inicial)>0 and int(indice_final) <= len(self.lista_valores) and int(indice_final) > int(indice_inicial) and int(indice_final) <= len(self.lista_valores):
                print(self.lista_valores[((int(indice_inicial))-1) : (int(indice_final))])
                print('Solo las posiciones intermedias del grango seleccionado.')
                print(self.lista_valores[((int(indice_inicial))-1) : (int(indice_final)) : 2])
            else:
                print(' Uno de los valores se encuentra fuera del rango. ')
            print(f' El ultimo valor de la lista es:  {self.lista_valores[-1]}')
            print(f' Los ultimos 10 valores de la lista son:  {self.lista_valores[-11:]}')
            print(f' Los primeros 10 valores de la lista son:  {self.lista_valores[:10]}')
            print('------------------------------------------------------------------------')
            print('\t Lita ordenada. ')
            self.lista_valores.sort(
                print(self.lista_valores)
            )
        else:
            print('No ingreso un numero.')                

    agregarValoreslista()