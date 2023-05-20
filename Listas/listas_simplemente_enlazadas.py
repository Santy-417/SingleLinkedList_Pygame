class Node():

    def __init__(self, data):
        self.value = data
        self.next = None

class SingleLinkedlist:

    def __init__(self):

        self.head = None
        self.tail = None
        self.lenght = 0

    def print_single_linked_list(self):

        #Validamos si la lista esta vacia

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
        # 2. Var¡lidar cunado al menos existe un nodo
        else:
            self.tail.next = new_node
            self.tail = new_node
            
        self.lenght += 1

    def anadir_al_inicio(self):

        print('\t Añadir al inicio.')
        
        self.head 
