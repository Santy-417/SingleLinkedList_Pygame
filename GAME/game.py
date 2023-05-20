import pygame, sys, pygame.locals

#inicicion de pygamew
pygame.init()

#panatalla - ventana
w,h = 1000,600
pantalla = pygame.display.set_mode((w,h))
pygame.display.set_caption("Exterminador")
icono = pygame.image.load(('D:\\Documents\\Desktop\\Programacion_2\\GAME\\img\\icono.png'))
pygame.display.set_icon(icono)


#fondo del juego
fondo = pygame.image.load(('D:\\Documents\\Desktop\\Programacion_2\\GAME\\img\\fondo.png')).convert()


#personaje

quieto = pygame.image.load(('D:\\Documents\\Desktop\\Programacion_2\\GAME\\img\\idle1.png'))

caminaDerecha = [pygame.image.load(('D:\\Documents\\Desktop\\Programacion_2\\GAME\\img\\run1.png')),
                pygame.image.load(('D:\\Documents\\Desktop\\Programacion_2\\GAME\\img\\run2.png')),
                pygame.image.load(('D:\\Documents\\Desktop\\Programacion_2\\GAME\\img\\run3.png')),
                pygame.image.load(('D:\\Documents\\Desktop\\Programacion_2\\GAME\\img\\run4.png')),
                pygame.image.load(('D:\\Documents\\Desktop\\Programacion_2\\GAME\\img\\run5.png')),
                pygame.image.load(('D:\\Documents\\Desktop\\Programacion_2\\GAME\\img\\run6.png'))]

caminaIzquierda = [pygame.image.load(('D:\\Documents\\Desktop\\Programacion_2\\GAME\\img\\run1-izq.png')),
                pygame.image.load(('D:\\Documents\\Desktop\\Programacion_2\\GAME\\img\\run2-izq.png')),
                pygame.image.load(('D:\\Documents\\Desktop\\Programacion_2\\GAME\\img\\run3-izq.png')),
                pygame.image.load(('D:\\Documents\\Desktop\\Programacion_2\\GAME\\img\\run4-izq.png')),
                pygame.image.load(('D:\\Documents\\Desktop\\Programacion_2\\GAME\\img\\run5-izq.png')),
                pygame.image.load(('D:\\Documents\\Desktop\\Programacion_2\\GAME\\img\\run6-izq.png'))]

caminaIzquierda = [pygame.image.load(('D:\\Documents\\Desktop\\Programacion_2\\GAME\\img\\jump1.png')),
                pygame.image.load(('D:\\Documents\\Desktop\\Programacion_2\\GAME\\img\\jump2.png'))]

x = 0
px = 50
py = 200
ancho = 40
velocidad = 10

#control de los fps

reloj = pygame.time.Clock()

#variable del salto
salto = False

#altura del salto
cuentaSalto = 10

#variables direccion
izquierda = False
derecha = False

#pasos
cuentaPasos = 0

#movimiento
def recargaPantalla():
    #variables globales
    global cuentaPasos
    global x

    #fondo en movimiento
    x_relativa = x % fondo.get_rect().width
    pantalla.blit(fondo,(x_relativa - fondo.get_rect().width,0))
    if x_relativa < w:
        pantalla.blit(fondo, (x_relativa,0))
    x -= 5

    #contador de pasos
    if cuentaPasos + 1 >=6:
        cuentaPasos = 0

    #movimientos a la izquierda
    if izquierda:
        pantalla.blit(caminaIzquierda[cuentaPasos //1],(int(px),int(py)))
        cuentaPasos += 1
    
    elif derecha:
        pantalla.blit(caminaDerecha[cuentaPasos //1],(int(px),int(py)))
        cuentaPasos += 1

    elif salto + 1>=2:
        cuentaPasos = 0
        pantalla.blit(salto[cuentaPasos // 1],int(px),int(py))
        cuentaPasos += 1

    else:
        pantalla.blit(quieto,(int(px),int(py)))

    #actualizacion de la pantalla
    pygame.display.update()

ejecuta = True

#bucle de acciones y controles
while ejecuta:
    #fps
    reloj.tick(18)

    #bucle del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecuta = False
    
    #opcion tecla pulsada
    keys = pygame.key.get_pressed()

    #tecla A - movimiento a la izquierda
    if keys[pygame.K_a] and px > velocidad:
        px -= velocidad
        izquierda = True
        derecha = False
    
    #tecla d - movimiento a la derecha
    elif keys[pygame.K_d] and px < 900 -velocidad - ancho:
        px += velocidad
        izquierda = False
        derecha = True
    
    #persoja quieto
    else:
        izquierda = False
        derecha = False
        cuentaPasos = 0
    
    #tecla w - movimiento hacia arriba
    if keys[pygame.K_w] and py > 100:
        py -= velocidad
    
    #tecla s - movimeinto haia abajo
    if keys[pygame.K_s] and py < 300:
        py += velocidad
    
    #tecla space - salto
    if not (salto):
        if keys[pygame.K_SPACE]:
            salto = True
            izquierda = False
            derecha = False
            cuentaPasos = 0
    else:
        if cuentaSalto >= -10:
            py -= (cuentaSalto * abs(cuentaSalto)) * 0.85
            cuentaSalto -= 1
        
        else:
            cuentaSalto = 10
            salto = False
    
    #llamada a la funcion de actualizacion de la ventana
    recargaPantalla()

#salida del juego
pygame.quit()
