import pygame
import pygame.locals
import sys

pygame.init() #inicia las funcionalidades de control de pygame

pantalla=pygame.display.set_mode((600,400))
#Tomamos control de la pantalla. 
#Fijamos dimensiones pantalla, se hace con una tupla

pygame.display.set_caption("Hola mundo") 
#Título de la pantalla

rojo=0

while True:
    for event in pygame.event.get():
    #Devuelve todos los eventos sucedidos desde el anterior event.get(). Los recorremos, aunque sea con un pass.
    #Pygame necesita que se haga de forma periódica
        if event.type==pygame.locals.QUIT:
            pygame.quit()
            sys.exit()

    if rojo>=255:
        direccion=-1

    if rojo<=0:
        direccion=+1

    rojo+=direccion
    
    pantalla.fill((rojo,0,0))
    #Fijamos el color de pantalla

    pygame.display.flip()
    #Actualiza la pantalla

    pygame.time.delay(5)
    #Tiempo en milisegundos
