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


# Iterar hasta que el usuario haga clic sobre el botón
done = False

# Se usa para establecer cuán rápido se actualiza la pantalla
clock = pygame.time.Clock()
# --------------Bucle principal del programa--------------
while not done:
    repositorio = font.render(" Hecho por Santiago Chavarro Osorio. ", True, BLACK)
    text = font.render(" SINGLE LINKED LIST ", True, MAGENT)
    # --Bucle Principal de Eventos
    for event in pygame.event.get():  # El usuario realizó alguna acción
        if event.type == pygame.QUIT:  # Si el usuario hizo clic sobre salir
            done = True  # Marcamos como hecho y salimos de este bucle
    
    # La lógica del juego debe ir aquí
    # El código de dibujo debería ir aquí
    screen.fill(WHITE)
    screen.blit(text, (350, 50))
    screen.blit(repositorio, (275, 550))

    pygame.display.flip()
    clock.tick(30)
