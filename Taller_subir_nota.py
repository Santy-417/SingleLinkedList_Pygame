class Node:

    def __init__(self, data):
        self.value = data
        self.next = None

class SingleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def empty_list(self):
        if self.head is None:
            return print('La lista no tiene nodos')
        else:
            return print('La lista tiene nodo')
    
    def print_single_linked_list(self):
        if not self.head:
            return print('La lista no tiene nodos')
        else:
            current_node = self.head
            while current_node:
                print(current_node.value)
                current_node = current_node.next

    def add_node_at_start(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def add_node_at_end(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def delete_at_start(self):
        if not self.head:
            return print('Lista vacía, nada que eliminar')     
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -=1
        else:
            current_node = self.head
            print('El Nodo a eliminar es ', current_node.value)
            self.head = current_node.next
            current_node = None
            self.length -=1

    def delete_at_end(self):
        if not self.head:
            return print('Lista vacìa, nada que eliminar')
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -=1
        else:
            current_node = self.head
            new_tail = current_node
            while current_node.next != None:
                new_tail = current_node
                current_node = current_node.next
            print('El Nodo a eliminar es ', self.tail.value)
            self.tail = new_tail
            self.tail.next = None
            self.length -= 1


    def get_value_node_by_index(self, index):
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
            if remove_node != None:
                previous_node = self.get_value_node_by_index(index-1)
                previous_node.next = remove_node.next
                remove_node = None
                self.length -= 1

    def remove_node_by_value(self, value):
        if not self.head:
            return print('Lista vacía, nada que eliminar')
        if self.head.value == value:
            self.delete_at_start()
            return
        current_node = self.head
        previous_node = None
        found = False
        while current_node and not found:
            if current_node.value == value:
                found = True
            else:
                previous_node = current_node
                current_node = current_node.next
        if found:
            previous_node.next = current_node.next
            if current_node == self.tail:
                self.tail = previous_node
            self.length -= 1
        else:
            print('Valor no encontrado en la lista.')

    def reverse_single_linked_list(self):
        if not self.head:
            return print('Lista vacía, nada que eliminar.')
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
            return print('Lista vacía.')
        else:
            slow_pointer = self.head
            fast_pointer = self.head
            while fast_pointer and fast_pointer.next:
                slow_pointer = slow_pointer.next
                fast_pointer = fast_pointer.next.next
            return slow_pointer.value

    def add_odd_values_at_end(self, data):
        if data % 2 == 0:
            new_node = Node(data)
            if self.head == None:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node
            self.length += 1

    def add_not_odd_values_at_start(self, data):
        if data % 2 != 0:
            new_node = Node(data)
            if self.head == None:
                self.head = new_node
                self.tail = new_node
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

    def get_size(self):
        return self.length

    def find_position_by_value(self, value):
        if not self.head:
            return print('Lista vacía')
        current_node = self.head
        position = 1
        while current_node:
            if current_node.value == value:
                return position
            current_node = current_node.next
            position += 1
        return print('El valor no se encuentra en la lista.')

    def get_value_by_position(self, position):
        if not self.head:
            return print('Lista vacía')
        if position < 1 or position > self.length:
            return print('Posición fuera de rango.')
        current_node = self.head
        current_position = 1
        while current_node:
            if current_position == position:
                return current_node.value
            current_node = current_node.next
            current_position += 1
        return print('La posición no existe en la lista.')

    def selection_sort(self):
        if not self.head or not self.head.next:
            return print('La lista no tiene nodos.')
        current_node = self.head
        while current_node:
            min_node = current_node
            next_node = current_node.next
            while next_node:
                if next_node.value < min_node.value:
                    min_node = next_node
                next_node = next_node.next
            current_node.value, min_node.value = min_node.value, current_node.value
            current_node = current_node.next

    def insert_at_position(self, data, position):
        if position < 1 or position > self.length + 1:
            print('Posición de inserción inválida.')
            return
        new_node = Node(data)
        if position == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            current_node = self.head
            previous_node = None
            count = 1
            while count < position:
                previous_node = current_node
                current_node = current_node.next
                count += 1
            previous_node.next = new_node
            new_node.next = current_node
        self.length += 1

    def update_value_at_position(self, new_value, position):
        if position < 1 or position > self.length:
            print('Posición de actualización inválida.')
            return
        current_node = self.head
        count = 1
        while count < position:
            current_node = current_node.next
            count += 1
        current_node.value = new_value
