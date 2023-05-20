class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SingleLinkedList:
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

    def add_first(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def add_last(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def remove_first(self):
        if not self.head:
            return
        self.head = self.head.next
        if not self.head:
            self.tail = None
        self.length -= 1

    def remove_last(self):
        if not self.head:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
            return
        current_node = self.head
        while current_node.next != self.tail:
            current_node = current_node.next
        current_node.next = None
        self.tail = current_node
        self.length -= 1

    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

    def remove_all(self):
        self.head = None
        self.tail = None
        self.length = 0

    def remove_at(self, position):
        if position < 0 or position >= self.length:
            return
        if position == 0:
            self.head = self.head.next
            if not self.head:
                self.tail = None
            self.length -= 1
            return
        current_node = self.head
        for i in range(position - 1):
            current_node = current_node.next
        current_node.next = current_node.next.next
        if not current_node.next:
            self.tail = current_node
        self.length -= 1

    def insert_at(self, position, value):
        if position < 0 or position > self.length:
            return
        if position == 0:
            self.add_first(value)
            return
        if position == self.length:
            self.add_last(value)
            return
        current_node = self.head
        for i in range(position - 1):
            current_node = current_node.next
        new_node = Node(value)
        new_node.next = current_node.next
        current_node.next = new_node
        self.length += 1
