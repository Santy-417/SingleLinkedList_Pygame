import pygame       

pygame.init()
pygame.font.init()

# Configuración de la pantalla
font = pygame.font.Font(None, 30)
size = (900, 600)
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

linked_list = SingleLinkedList()


# Cargar imágenes de los números
number_images = []
number_images.append(pygame.image.load('C:\\Users\\Asus-PC\\Documents\\Escritorio\\Programacion_2\\TRABAJO_PROPUESTA_PYGAME\\Imagen_1.jpg'))
number_images.append(pygame.image.load('C:\\Users\\Asus-PC\\Documents\\Escritorio\\Programacion_2\\TRABAJO_PROPUESTA_PYGAME\\Imagen_2.jpg'))
number_images.append(pygame.image.load('C:\\Users\\Asus-PC\\Documents\\Escritorio\\Programacion_2\\TRABAJO_PROPUESTA_PYGAME\\Imagen_3.jpg'))

# Crear los botones
add_first_button_rect = pygame.Rect(50, 300, 150, 50)
add_first_button_color = (167,241,241)
add_last_button_rect = pygame.Rect(50 + 150 + 50, 300, 150, 50)
add_last_button_color = (167,241,241)
remove_first_button_rect = pygame.Rect(50 + (150 + 50) * 2, 300, 150, 50)
remove_first_button_color = (167,241,241)
remove_last_button_rect = pygame.Rect(50 + (150 + 50) * 3, 300, 150, 50)
remove_last_button_color = (167,241,241)

clock = pygame.time.Clock()
running = True
button_pressed = False
selected_option = None
selected_number = None
numbers = [1, 2, 3]

while running:
    button_pressed = False
    footer = font.render(" Hecho por Santiago Chavarro Osorio. ", True, BLACK)
    text = font.render(" SINGLE LINKED LIST ", True, MAGENT)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if add_first_button_rect.collidepoint(event.pos):
                    linked_list.add_first(numbers, None)
                    # selected_option = "add_first"
                    button_pressed = True
                elif add_last_button_rect.collidepoint(event.pos):
                    linked_list.add_last(numbers, None)
                    # selected_option = "add_last"
                    button_pressed = True
                elif remove_first_button_rect.collidepoint(event.pos):
                    linked_list.remove_first()
                    # selected_option = "remove_first"
                    button_pressed = True
                elif remove_last_button_rect.collidepoint(event.pos):
                    linked_list.remove_last()
                    # selected_option = "remove_last"
                    button_pressed = True

    # Dibujado de los nodos y botón
    screen.fill(color_fondo)
    screen.blit(text, (350, 50))
    screen.blit(footer, (275, 550))

    pygame.draw.rect(screen, add_first_button_color, add_first_button_rect)
    add_first_button_text = font.render("Add to first", True, BLACK)
    add_first_button_text_rect = add_first_button_text.get_rect(center=add_first_button_rect.center)
    screen.blit(add_first_button_text, add_first_button_text_rect)

    pygame.draw.rect(screen, add_last_button_color, add_last_button_rect)
    add_last_button_text = font.render("Add to last", True, BLACK)
    add_last_button_text_rect = add_last_button_text.get_rect(center=add_last_button_rect.center)
    screen.blit(add_last_button_text, add_last_button_text_rect)

    pygame.draw.rect(screen, remove_first_button_color, remove_first_button_rect)
    remove_first_button_text = font.render("Remove to star", True, BLACK)
    remove_first_button_text_rect = remove_first_button_text.get_rect(center=remove_first_button_rect.center)
    screen.blit(remove_first_button_text, remove_first_button_text_rect)

    pygame.draw.rect(screen, remove_last_button_color, remove_last_button_rect)
    remove_last_button_text = font.render("Remove to last", True, BLACK)
    remove_last_button_text_rect = remove_last_button_text.get_rect(center=remove_last_button_rect.center)
    screen.blit(remove_last_button_text, remove_last_button_text_rect)


    # Mostrar números seleccionables
    if selected_option is not None:
        for i, number in enumerate(numbers):
            x = 250 + 150 * i
            y = 400
            number_image = number_images[number - 1]
            screen.blit(number_image, (x, y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

