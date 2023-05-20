import pygame
pygame.init()
#Definir Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (220,240,241)
BLUE2 = (220,250,251)
MOR = (236,209,244)
#Definir dimensiones de la pantalla
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Mi juego')
#Iterar hasta que el usuario haga click sobre el botón de cierre
done = False
#Se usa para establecer cuan rapido se actualiza la pantalla
clock = pygame.time.Clock()
fuente = pygame.font.SysFont("arial", 15 ) # creo el objeto fuente 
fuente2 = pygame.font.SysFont("arial", 20 )

Alinicio = pygame.Rect(310,220,150,30)
Alfin = pygame.Rect(310,260,150,30)
EliminaInicio = pygame.Rect(310,300,150,30)
EliminaFin = pygame.Rect(310,340,150,30)

num1 = pygame.Rect(280,130,50,50)
num2 = pygame.Rect(350,130,50,50)
num3 = pygame.Rect(420,130,50,50)

mostrar = pygame.Rect(100,410,600,50)

lista =[]
color1 = BLUE2
color2 = BLUE2
color3 = BLUE2
dato = 0
#---- Funcion para eszcribir texto ----
def escribirl(palabras,corx,cory):
    mytexto = fuente.render(palabras,0,(BLACK))
    screen.blit(mytexto,(corx,cory))

def escribirl2(palabras,corx,cory):
    mytexto = fuente2.render(palabras,0,(BLACK))
    screen.blit(mytexto,(corx,cory))

#--------------Bucle principal del programa--------------
while not done:
    #--Bucle Principal de Eventos
    for event in pygame.event.get(): #El usuario realizo alguna acción
        if event.type == pygame.QUIT: #Si el usuario hizo click sobre salir
            done = True  #Marcamos como hecho y salimos de este bucle

        #-----Evento cuando orpimen un boton----
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if num1.collidepoint(pygame.mouse.get_pos()):
                color1=MOR
                color2=BLUE2
                color3=BLUE2
                dato = 1
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if num2.collidepoint(pygame.mouse.get_pos()):
                color1=BLUE2
                color2=MOR
                color3=BLUE2
                dato = 2
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if num3.collidepoint(pygame.mouse.get_pos()):
                color1=BLUE2
                color2=BLUE2
                color3=MOR
                dato = 3

        #-----Evento cuando orpimen una opcion ----
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if Alinicio.collidepoint(pygame.mouse.get_pos()):
                lista.insert(0,dato)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if Alfin.collidepoint(pygame.mouse.get_pos()):
                lista.append(dato)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if EliminaInicio.collidepoint(pygame.mouse.get_pos()):
                lista.pop(0)
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if EliminaFin.collidepoint(pygame.mouse.get_pos()):
                lista.pop(len(lista)-1)
                
    #La logica del juego debe ir aqui
    #El codigo de dibujo deberia ir aqui
    #Primero, limpia la pantalla con planco. No vayas a poner otros comandos de dibujo encima de esto, de otra forma seran borrados por este comando:
    screen.fill(BLUE)
    #screen.blit(mytexto,(0,0))  # escribe en pantalla 
    escribirl("PARA INICIAR DEBES SELECCIONAR AL MENOS UNA IMAGEN DE SERÁ LA CABEZA DE LA LISTA",100,100)
    escribirl("Selecciona un método",140,210)
    escribirl(">> Estado actual de la lista <<",140,380)
    
    
    pygame.draw.rect(screen,(WHITE),Alinicio,0)
    escribirl("Añadir al inicio",345,220)
    pygame.draw.rect(screen,(WHITE),Alfin,0)
    escribirl("Añadir al final",344,260)
    pygame.draw.rect(screen,(WHITE),EliminaInicio,0)
    escribirl("Eliminar el inicio",340,300)
    pygame.draw.rect(screen,(WHITE),EliminaFin,0)
    escribirl("Eliminar el final",340,340)
    pygame.draw.rect(screen,(WHITE),mostrar,0)

    pygame.draw.rect(screen,(color1),num1,0)
    escribirl2("1",300,140)
    pygame.draw.rect(screen,(color2),num2,0)
    escribirl2("2",370,140)
    pygame.draw.rect(screen,(color3),num3,0)
    escribirl2("3",440,140)

    escribirl("Desarrollado por: ____________",320,500)
    escribirl("SEM - 2023 ",340,520)
    conta = 0
    for i in range(len(lista)):
        escribirl2(str(lista[i]),200 + conta ,420)
        conta=conta+50
    pygame.display.flip()
    clock.tick(60)

pygame.quit()