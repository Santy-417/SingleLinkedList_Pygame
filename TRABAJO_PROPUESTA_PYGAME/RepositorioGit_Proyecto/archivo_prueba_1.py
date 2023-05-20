import pygame       

pygame.init()
pygame.font.init()

# Configuración de la pantalla
font = pygame.font.Font(None, 30)
size = (900, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Lista Simplemente Enlazada')
fondo = (44, 39, 129 )
screen.fill(fondo)

BLACK = (0,0,0)
WHITE = (255,255,255)
MAGENT = (154,13,105)

class Node:
    def _init_(self, value, image):
        self.value = value
        self.image = image
        self.next = None

class SingleLinkedList:
    def _init_(self):
        self.head = None
        self.tail = None
        self.length = 0

    def remove_start(self):
        if not self.head:
            return
        self.head = self.head.next
        if not self.head:
            self.tail = None
        self.length -= 1

    def remove_end(self):
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

    def add_start(self, value, image):
        new_node = Node(value, image)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def add_end(self, value, image):
        new_node = Node(value, image)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

linked_list = SingleLinkedList()
clock = pygame.time.Clock()

#Se crean botones y añade color a cada uno 
add_first_button_rect = pygame.Rect(450, 150, 180, 50)
add_first_button_color = (167,241,241)
add_last_button_rect = pygame.Rect(650, 150, 180, 50)
add_last_button_color = (167,241,241)
remove_first_button_rect = pygame.Rect(450, 250, 180, 50)
remove_first_button_color = (167,241,241)
remove_last_button_rect = pygame.Rect(650, 250, 180, 50)
remove_last_button_color = (167,241,241)

numero_1 = pygame.Rect(130,150,50,50)
add_color_n1 = (167,241,241)
numero_2 = pygame.Rect(230,150,50,50)
add_color_n2 = (167,241,241)
numero_3 = pygame.Rect(180,235,50,50)
add_color_n3 = (167,241,241)

estado_lista = pygame.Rect(100,410,700,50)

running = True
selected_number = None  
lista =[]
add_color_n1 = BLACK
add_color_n2 = BLACK
add_color_n3 = BLACK
dato = 0


while running:
    #--Bucle Principal de Eventos
    for event in pygame.event.get(): # El usuario realizó alguna acción
        if event.type == pygame.QUIT: # Si el usuario hizo clic en salir
            running = False  # Marcamos como hecho y salimos de este bucle

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if numero_1.collidepoint(mouse_pos):
                add_color_n1 = MAGENT
                add_color_n2 = BLACK
                add_color_n3 = BLACK
                dato = 1
            elif numero_2.collidepoint(mouse_pos):
                add_color_n1 = BLACK
                add_color_n2 = MAGENT
                add_color_n3 = BLACK
                dato = 2
            elif numero_3.collidepoint(mouse_pos):
                add_color_n1 = BLACK
                add_color_n2 = BLACK
                add_color_n3 = MAGENT
                dato = 3

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if add_first_button_rect.collidepoint(pygame.mouse.get_pos()):
                lista.insert(0, dato)
            elif add_last_button_rect.collidepoint(pygame.mouse.get_pos()):
                lista.append(dato)
            elif remove_first_button_rect.collidepoint(pygame.mouse.get_pos()):
                lista.pop(0)
            elif remove_last_button_rect.collidepoint(pygame.mouse.get_pos()):
                lista.pop(len(lista)-1)

    footer = font.render("Desarrollado por: Santiago Giraldo ", True, BLACK)
    text = font.render(" 1) Seleccionar algun numero                2) Elegir un metodo para modificar la lista.", True, BLACK)
    estado__lista = font.render(">>Estado actual de la Lista<<", True, BLACK)
    num1 = font.render("1", True, WHITE)
    num2 = font.render("2", True, WHITE)
    num3 = font.render("3", True, WHITE)
    # Dibujado de los nodos y botón
    screen.fill(fondo)
    screen.blit(text, (30, 50))
    screen.blit(footer, (275, 550))
    screen.blit(estado__lista, (100, 375))

    pygame.draw.rect(screen, add_first_button_color, add_first_button_rect)
    add_first_button_text = font.render("Añadir al Inicio", True, BLACK)
    add_first_button_text_rect = add_first_button_text.get_rect(center=add_first_button_rect.center)
    screen.blit(add_first_button_text, add_first_button_text_rect)

    pygame.draw.rect(screen, add_last_button_color, add_last_button_rect)
    add_last_button_text = font.render("Añadir al Final", True, BLACK)
    add_last_button_text_rect = add_last_button_text.get_rect(center=add_last_button_rect.center)
    screen.blit(add_last_button_text, add_last_button_text_rect)

    pygame.draw.rect(screen, remove_first_button_color, remove_first_button_rect)
    remove_first_button_text = font.render("Eliminar al inicio", True, BLACK)
    remove_first_button_text_rect = remove_first_button_text.get_rect(center=remove_first_button_rect.center)
    screen.blit(remove_first_button_text, remove_first_button_text_rect)

    pygame.draw.rect(screen, remove_last_button_color, remove_last_button_rect)
    remove_last_button_text = font.render("Eliminar al final", True, BLACK)
    remove_last_button_text_rect = remove_last_button_text.get_rect(center=remove_last_button_rect.center)
    screen.blit(remove_last_button_text, remove_last_button_text_rect)


    pygame.draw.rect(screen,(WHITE),estado_lista,0)

    pygame.draw.rect(screen,(add_color_n1),numero_1,0)
    screen.blit(num1, (150,165))
    pygame.draw.rect(screen,(add_color_n2),numero_2,0)
    screen.blit(num2, (250,165))
    pygame.draw.rect(screen,(add_color_n3),numero_3,0)
    screen.blit(num3, (200,250))


    espacio = 0
    for i in range(len(lista)):
        numeros_lista = font.render(str(lista[i]), 0, BLACK)
        screen.blit(numeros_lista, (200 + espacio, 420))
        espacio += 50
    pygame.display.flip()
    clock.tick(60)
pygame.quit()