class Node:

    def __init__(self, data):
        self.value = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def print_single_linked_list(self):
        # Validamos si la lista está vacía
        if not self.head:
            return print('La lista no tiene nodos')
        else:
            current_node = self.head
            while current_node:
                print(current_node.value)
                current_node = current_node.next

    def add_node_at_end(self, data):
        new_node = Node(data)
        # 1. Valido si la lista tiene al menos un nodo
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        # 2. Validar cuando al menos existe un nodo
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def add_node_at_start(self, data):
        new_node = Node(data)
        # 1. Valido si la lista tiene al menos un nodo
        if not self.head:
            self.head = new_node
            self.tail = new_node
        # 2. Validar cuando al menos existe un nodo
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def delete_at_end(self):
        # 1. Valido si la lista tiene al menos un nodo
        if not self.head:
            return print('Lista vacìa, nada que eliminar')
        # 1. Valido si la lista tiene al menos un nodo   
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -=1
        else:
            current_node = self.head
            new_tail = current_node
            while current_node.next != None:
                new_tail = current_node
                #Pasamos a visitar el siguiente nodo de la lista:
                current_node = current_node.next
            print('Nodo a eliminar es ', self.tail.value)
            self.tail = new_tail
            self.tail.next = None
            self.length -= 1
    
    def delete_at_start(self):
        if not self.head:
            return print('Lista vacía, nada que eliminar')     
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -=1
        else:
            current_node = self.head
            print('Nodo a eliminar es ', current_node.value)
            self.head = current_node.next
            current_node = None
            self.length -=1

    def get_value_node_by_index(self, index):
        #Validar que el indice suministrado si se encuentre en la lista
        if index < 1 and index > self.length:
            return print('Indice fuera del rango')
        elif index == 1:
            return self.head
        elif index == self.length:
            return self.tail
        else:
            current_node = self.head
            contador_nodos_visitados = 1
            while index != contador_nodos_visitados:
                current_node = current_node.next
                contador_nodos_visitados += 1
            return current_node
    
    def remove_node_by_index(self, index):
        if index == 1:
            self.delete_at_start()
        elif index == self.length:
            self.delete_at_end()
        else:
            remove_node = self.get_value_node_by_index(index)
            #Validar si si se encuentra el nodo a eliminar
            if remove_node != None:
                previous_node = self.get_value_node_by_index(index-1)
                previous_node.next = remove_node.next
                remove_node = None
                self.length -= 1
    
    def remove_node_by_value(self, value):
        if not self.head:
            return print('Lista vacía, nada que eliminar')

        # Caso especial si el valor a eliminar está en el primer nodo
        if self.head.value == value:
            self.delete_at_start()
            return

        current_node = self.head
        previous_node = None
        found = False

        # Buscamos el nodo que contenga el valor que deseamos eliminar
        while current_node and not found:
            if current_node.value == value:
                found = True
            else:
                previous_node = current_node
                current_node = current_node.next

        # Si se encontró el valor, se elimina el nodo que lo contiene
        if found:
            previous_node.next = current_node.next
            # Si el nodo a eliminar es el último de la lista, actualizamos el puntero tail
            if current_node == self.tail:
                self.tail = previous_node
            self.length -= 1
        else:
            print('Valor no encontrado en la lista')

    def reverse_single_linked_list(self):
        if not self.head:
            return print('Lista vacía, nada que eliminar')
        else:
            previous_node = None
            current_node = self.head
            while current_node:
                next_node = current_node.next
                current_node.next = previous_node
                previous_node = current_node
                current_node = next_node
            self.head = previous_node

    def get_value_middle_node(self):
        if not self.head:
            return print('Lista vacía, nada que eliminar')
        else:
            slow_pointer = self.head
            fast_pointer = self.head
            while fast_pointer and fast_pointer.next:
                slow_pointer = slow_pointer.next
                fast_pointer = fast_pointer.next.next
            return slow_pointer.value

    def add_odd_values_at_end(self, data):
    # Verificamos si el dato es un número par
        if data % 2 == 0:
            new_node = Node(data)
            # 1. Validamos si la lista tiene al menos un nodo
            if self.head == None:
                self.head = new_node
                self.tail = new_node
            # 2. Validar cuando al menos existe un nodo
            else:
                self.tail.next = new_node
                self.tail = new_node
            self.length += 1

    def add_not_odd_values_at_start(self, data):
        # Verificamos si el dato es un número impar
        if data % 2 != 0:
            new_node = Node(data)
            # 1. Validamos si la lista tiene al menos un nodo
            if self.head == None:
                self.head = new_node
                self.tail = new_node
            # 2. Validar cuando al menos existe un nodo
            else:
                new_node.next = self.head
                self.head = new_node
            self.length += 1

    def get_sum_all_values(self):
        current_node = self.head
        total_sum = 0
        while current_node:
            total_sum += current_node.value
            current_node = current_node.next
        return total_sum