import pygame

pygame.init()
pygame.font.init()

# Configuración de la pantalla
font = pygame.font.Font(None, 30)
size = (900,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Linked List')
color_fondo = (189, 195, 199)
screen.fill(color_fondo)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
MAGENT = (154, 13, 105)


class Node:
    def __init__(self, value, image):
        self.value = value
        self.image = image
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_first(self, value, image):
        new_node = Node(value, image)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def add_last(self, value, image):
        new_node = Node(value, image)
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


imagen_1 = pygame.image.load(("C:\\Users\\Asus-PC\\Documents\\Escritorio\\Programacion_2\\TRABAJO_PROPUESTA_PYGAME\\Imagen_1.jpg"))
imagen_2 = pygame.image.load(("C:\\Users\\Asus-PC\\Documents\\Escritorio\\Programacion_2\\TRABAJO_PROPUESTA_PYGAME\\Imagen_2.jpg"))
imagen_3 = pygame.image.load(("C:\\Users\\Asus-PC\\Documents\\Escritorio\\Programacion_2\\TRABAJO_PROPUESTA_PYGAME\\Imagen_3.jpg"))

linked_list = SingleLinkedList()

clock = pygame.time.Clock()
running = True
while running:
    repositorio = font.render(" Hecho por Santiago Chavarro Osorio. ", True, BLACK)
    text = font.render(" SINGLE LINKED LIST ", True, MAGENT)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Dibujado de los nodos
    screen.fill(color_fondo)
    screen.blit(text, (350, 50))
    screen.blit(repositorio, (275, 550))

    current_node = linked_list.head
    x_position = 50

    while current_node:
        image = current_node.image
        screen.blit(image, (x_position, 200))
        current_node = current_node.next
        x_position += 150

    pygame.display.update()
    linked_list.add_last(1, imagen_1)
    linked_list.add_last(3, imagen_3)
    linked_list.add_last(2, imagen_2)

    clock.tick(30)
pygame.quit()
