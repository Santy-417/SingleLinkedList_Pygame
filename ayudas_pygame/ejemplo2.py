import pygame

pygame.init()
pygame.font.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
MAGENT = (154, 13, 105)

font = pygame.font.Font(None, 30)
# Definir dimensiones de la pantalla
size = (900, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Mi juego')

# Opciones de la lista desplegable
options = ['Opción 1', 'Opción 2', 'Opción 3', 'Opción 4']
selected_option = None  # Opción seleccionada (inicialmente ninguna)

# Variables para el despliegue de la lista
dropdown_rect = pygame.Rect(350, 250, 200, 30)
dropdown_open = False

# Se usa para establecer cuán rápido se actualiza la pantalla
clock = pygame.time.Clock()

# --------------Bucle principal del programa--------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if dropdown_rect.collidepoint(event.pos):
                dropdown_open = not dropdown_open
            elif dropdown_open:
                option_index = (event.pos[1] - dropdown_rect.y) // 30
                if 0 <= option_index < len(options):
                    selected_option = options[option_index]
                    dropdown_open = False

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, dropdown_rect, 2)
    dropdown_text = font.render(selected_option or "Seleccione una opción", True, BLACK)
    screen.blit(dropdown_text, (dropdown_rect.x + 5, dropdown_rect.y + 5))

    if dropdown_open:
        for i, option in enumerate(options):
            option_rect = pygame.Rect(dropdown_rect.x, dropdown_rect.y + (i + 1) * 30, dropdown_rect.width, 30)
            pygame.draw.rect(screen, WHITE, option_rect)
            pygame.draw.rect(screen, BLACK, option_rect, 1)
            option_text = font.render(option, True, BLACK)
            screen.blit(option_text, (option_rect.x + 5, option_rect.y + 5))

    pygame.display.flip()
    clock.tick(30)

