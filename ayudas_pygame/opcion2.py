import pygame

pygame.init()

# Configuración de la pantalla
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Linked List")

# Definición de la clase Node
class Node:
    def __init__(self, data, image):
        self.data = data
        self.image = image
        self.next = None

# Definición de la clase LinkedList
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # Método para agregar un nodo al final de la lista
    def append(self, value, image):
        new_node = Node(value, image)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    # Método para agregar un nodo al inicio de la lista
    def add_star(self, value, image):
        new_node = Node(value, image)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    
    # Método para eliminar un nodo por su valor
    def remove(self, value):
        if not self.head:
            return None
        elif self.head.data == value:
            removed_node = self.head
            self.head = self.head.next
            self.length -= 1
            return removed_node
        else:
            current_node = self.head
            while current_node.next:
                if current_node.next.data == value:
                    removed_node = current_node.next
                    current_node.next = current_node.next.next
                    if current_node.next is None:
                        self.tail = current_node
                    self.length -= 1
                    return removed_node
                current_node = current_node.next
            return None
    
    # Método para obtener un nodo por su índice
    def get_node(self, index):
        if index < 0 or index >= self.length:
            return None
        else:
            current_node = self.head
            for i in range(index):
                current_node = current_node.next
            return current_node

# Carga de las imágenes
head_image = pygame.image.load(("C:\\Users\\Asus-PC\\Documents\\Escritorio\\Programacion_2\\zorro.png"))
node_image = pygame.image.load(("C:\\Users\\Asus-PC\\Documents\\Escritorio\\Programacion_2\\TRABAJO_PROPUESTA_PYGAME\\leon.jpg"))

# Creación de la lista
linked_list = LinkedList()
linked_list.append("Node 1", head_image)  # Agregar imagen de cabeza al final
linked_list.add_star("Node 2", node_image)
linked_list.add_star("Node 3", node_image)

# Ciclo principal del juego
running = True
while running:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Dibujado de los nodos
    screen.fill((0, 0, 0))
    current_node = linked_list.head
    x = 50
    y = 50
    while current_node is not None:
        # Dibujar el círculo
        pygame.draw.circle(screen, (255, 255, 255), (x+50, y+25), 20)
        # Dibujar la imagen
        screen.blit(current_node.image, (x+10, y+5))
        # Actualización de las coordenadas
        x += 150
        current_node = current_node.next
    
    # Actualización de la pantalla
    pygame.display.update()
# Salida del juego
pygame.quit()
