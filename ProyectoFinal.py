import pygame# Importar la libreria

pygame.init()# Inicializar la libreria
pygame.font.init()# Inicializar font(fuentes)

# Configuración de la pantalla
font = pygame.font.Font(None, 30)# Fuente
screen = pygame.display.set_mode((900,600))# Renderizar tamaño de la pantalla
pygame.display.set_caption('Linked List') # Texto del archivo

# Paleta de colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (167, 241, 241)
TITLE = (133, 193, 233)
COLORBACK = (31,97,141)

# Clase Node la cual va a contener el valor y el puntero del nodo
class Node:
    def __init__(self, value, image):
        self.value = value
        self.image = image
        self.next = None

# Clase SingleLinkedlist la cual va a contener los metodos para interactuar con los nodos
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


linked_list = SingleLinkedList()# Instancia linked_list la cual contiene la clase SingleLinkedList
clock = pygame.time.Clock()# Instancia clock que contiene el tiempo de actualizacion de la pantalla

# Crear los botones
Button_AddFisrt = pygame.Rect(50, 300, 150, 50)# Posicion del primer boton(1)
Button_AddFisrt_color = BLUE
Button_AddLast = pygame.Rect(250, 300, 150, 50)# Posicion del segundo boton(2)
Button_AddLast_color = BLUE
Button_RemoveFirst = pygame.Rect(450, 300, 150, 50)# Posicion del tercer boton(3)
Button_RemoveFirst_color = BLUE
Button_RemoveLast = pygame.Rect(650, 300, 150, 50)# Posicion del cuarto boton(4)
Button_RemoveLast_color = BLUE

# Crear los botones que contienen los numeros
numero_1 = pygame.Rect(330, 175, 50, 50)
numero_2 = pygame.Rect(430, 175, 50, 50)
numero_3 = pygame.Rect(530, 175, 50, 50)

# Crear la barra que va a contiene la actualizacion de la lista
barra_estado_lista = pygame.Rect(100, 410, 700, 80)

# Cargar las imagenes de los numeros
numero1_img = pygame.image.load(("C:\\Users\\Asus-PC\\Documents\\Escritorio\\Programacion_2\\TRABAJO_PROPUESTA_PYGAME\\RepositorioGit_Proyecto\\SingleLinkedList_Pygame\\Imagen_1.jpg"))
numero2_img = pygame.image.load(("C:\\Users\\Asus-PC\\Documents\\Escritorio\\Programacion_2\\TRABAJO_PROPUESTA_PYGAME\\RepositorioGit_Proyecto\\SingleLinkedList_Pygame\\Imagen_2.jpg"))
numero3_img = pygame.image.load(("C:\\Users\\Asus-PC\\Documents\\Escritorio\\Programacion_2\\TRABAJO_PROPUESTA_PYGAME\\RepositorioGit_Proyecto\\SingleLinkedList_Pygame\\Imagen_3.jpg"))

# Escalar las imagenes al tamaño del boton
numero1_img = pygame.transform.scale(numero1_img, (numero_1.width, numero_1.height))
numero2_img = pygame.transform.scale(numero2_img, (numero_2.width, numero_2.height))
numero3_img = pygame.transform.scale(numero3_img, (numero_3.width, numero_3.height))

# Inicializar el bucle, los colores y la seleccion de los los numeros
running = True
color_n1 = BLACK
color_n2 = BLACK
color_n3 = BLACK
selec_number = 0

# Crear un diccionario que va a contener las imagenes, ya que de esta manera me parecio que es mas facil acceder a ellas
number_images = {
    1: numero1_img,# Imagen 1
    2: numero2_img,# Imagen 2
    3: numero3_img# Imagen 3
}

# Bucle principal del juego
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # En esta parte lo que se hace es validar la posicion del mouse en los numeros
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_posicion = pygame.mouse.get_pos()
            if numero_1.collidepoint(mouse_posicion):
                color_n1 = BLUE   
                color_n2 = BLACK
                color_n3 = BLACK
                selec_number = 1
            elif numero_2.collidepoint(mouse_posicion):
                color_n1 = BLACK
                color_n2 = BLUE
                color_n3 = BLACK
                selec_number = 2
            elif numero_3.collidepoint(mouse_posicion):
                color_n1 = BLACK
                color_n2 = BLACK
                color_n3 = BLUE
                selec_number = 3

        # En esta parte lo que se hace es validar la posicion del mouse en los metodos
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_posicion = pygame.mouse.get_pos()
            if Button_AddFisrt.collidepoint(mouse_posicion):
                if selec_number is not None:
                    image = number_images.get(selec_number)
                    linked_list.add_first(selec_number, image)
            elif Button_AddLast.collidepoint(mouse_posicion):
                if selec_number is not None:
                    image = number_images.get(selec_number)
                    linked_list.add_last(selec_number, image)
            elif Button_RemoveFirst.collidepoint(mouse_posicion):
                linked_list.remove_first()
            elif Button_RemoveLast.collidepoint(mouse_posicion):
                linked_list.remove_last()

    text_title = font.render("SINGLE LINKED LIST WITH PYGAME", True, BLACK)# TITLE del programa
    text_informacion = font.render("Selecione un número y luego un metodo para poder agregarlo a la lista.",True,BLACK)# Instrucciones de uso
    text_estado_lista = font.render("Estado lista: ", True, BLACK)# Actualizacion de la lista
    text_footer = font.render(" Hecho por Santiago Chavarro Osorio. ", True, BLACK)# Texto del pie de pagina

    screen.fill(COLORBACK)# Darle color al fondo
    screen.blit(text_title, (290, 50))# Mostrar el TITLE del programa
    screen.blit(text_informacion, (120, 120))# Mostrar las intruciones de uso
    screen.blit(text_estado_lista, (100, 375))# Mostrar la barra que actualiza la lista
    screen.blit(text_footer, (275, 550))# Mostrar el pie de pagina

    pygame.draw.rect(screen, Button_AddFisrt_color, Button_AddFisrt)# Dibujar el rectangulo(Boton)
    Button_AddFisrt_text = font.render("Add to first", True, BLACK)# Añadir texto al boton(Renderizar)
    Button_AddFisrt_text_rect = Button_AddFisrt_text.get_rect(center=Button_AddFisrt.center)# Centrar el texto haciendo salculos con la funcion .get_rect
    screen.blit(Button_AddFisrt_text, Button_AddFisrt_text_rect)# Mostrarlo en pantalla

    pygame.draw.rect(screen, Button_AddLast_color, Button_AddLast)# Dibujar el rectangulo(Boton)
    Button_AddLast_text = font.render("Add to last", True, BLACK)# Añadir texto al boton(Renderizar)
    Button_AddLast_text_rect = Button_AddLast_text.get_rect(center=Button_AddLast.center)# Centrar el texto haciendo salculos con la funcion .get_rect
    screen.blit(Button_AddLast_text, Button_AddLast_text_rect)# Mostrarlo en pantalla

    pygame.draw.rect(screen, Button_RemoveFirst_color, Button_RemoveFirst)# Dibujar el rectangulo(Boton)
    Button_RemoveFirst_text = font.render("Remove first", True, BLACK)# Añadir texto al boton(Renderizar)
    Button_RemoveFirst_text_rect = Button_RemoveFirst_text.get_rect(center=Button_RemoveFirst.center)# Centrar el texto haciendo salculos con la funcion .get_rect
    screen.blit(Button_RemoveFirst_text, Button_RemoveFirst_text_rect)# Mostrarlo en pantalla

    pygame.draw.rect(screen, Button_RemoveLast_color, Button_RemoveLast)# Dibujar el rectangulo(Boton)
    Button_RemoveLast_text = font.render("Remove last", True, BLACK)# Añadir texto al boton(Renderizar)
    Button_RemoveLast_text_rect = Button_RemoveLast_text.get_rect(center=Button_RemoveLast.center)# Centrar el texto haciendo salculos con la funcion .get_rect
    screen.blit(Button_RemoveLast_text, Button_RemoveLast_text_rect)# Mostrarlo en pantalla

    pygame.draw.rect(screen, WHITE,  barra_estado_lista, 0) # Dibuja el rectangulo donde se renderiza y actualiza la lista

    pygame.draw.rect(screen, color_n1, numero_1, 0)# Dibuja los rectangulos en donde se encuentras las imagenes de los numero (imagne1)
    screen.blit(numero1_img, (335, 180))
    pygame.draw.rect(screen, color_n2, numero_2, 0)# Dibuja los rectangulos en donde se encuentras las imagenes de los numero (imagne2)
    screen.blit(numero2_img, (435, 180))
    pygame.draw.rect(screen, color_n3, numero_3, 0)# Dibuja los rectangulos en donde se encuentras las imagenes de los numero (imagne3)
    screen.blit(numero3_img, (535, 180))

    espacio = 0# Inicializar un contador que nos permite darle espacio a la imagenes 
    current_node = linked_list.head# Inicializar current_node como la cabeza de la lista, ya que vamos a renderizar el primer numero que se seleccione
    while current_node is not None:# Mientras que current_node no sea none(vacia) vamos a continuar
        if current_node.image is not None:# Si la imagen del nodo actual no sea none(vacia) vamos a agregar una nueva imagen
            screen.blit(current_node.image, (120 + espacio, 420))# Renderizamos la imagen del nodo actual y la posicionamos dandole espacio en alto y ancho
        espacio += 75# Sumamos 75 pixels que es la separacion que va a tener cada imagen
        current_node = current_node.next# Actualizamos el current_node para que apunte al siguiente nodo y comenzamos de nuevo el ciclo

    pygame.display.flip()# Actualizamos la pantalla 
    clock.tick(60)# Definimos que tan rapido queremos que se actualice la pantalla

pygame.quit()# Finalizar el programa 

#Button_AddFisrt_text_rect = Button_AddFisrt_text.get_rect(center=Button_AddFisrt.center)
""" calcula y guarda en la variable Button_AddLast_text_rect el 
    rectángulo que representa la posición y el tamaño del texto 
    renderizado, centrándolo dentro del rectángulo del botón. """