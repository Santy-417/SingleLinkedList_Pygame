import pygame

# Clase para definir un nodo de la linkedlist
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Clase para definir la linkedlist
class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

# Inicializar Pygame
pygame.init()

# Configurar la ventana
window_width = 800
window_height = 600
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Linked List')

# Inicializar la linkedlist
linkedlist = LinkedList()
linkedlist.add_node(1)
linkedlist.add_node(2)
linkedlist.add_node(3)
linkedlist.add_node(4)

# Dibujar la linkedlist en la pantalla
font = pygame.font.Font(None, 36)
current_node = linkedlist.head
x = 50
y = 50
while current_node is not None:
    node_text = font.render(str(current_node.data), True, (255, 255, 255))
    screen.blit(node_text, (x, y))
    pygame.draw.circle(screen, (255, 255, 255), (x+50, y+25), 10, 2)
    current_node = current_node.next
    x += 100

# Actualizar la pantalla
pygame.display.update()

# Esperar hasta que el usuario cierre la ventana
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
