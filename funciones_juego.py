import sys 
import pygame

def verificar_eventos():
    """Responde a las pulsaciones de teclas y los eventos del ratón"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def actualizar_pantalla(ai_configuraciones, pantalla, nave):
    """Actualiza las imágenes en la pantalla y pasa a la nueva pantalla"""

    #Volver a dibujar la pantalla durante cada pasada del bucle while
    pantalla.fill(ai_configuraciones.bg_color)
    nave.blitme()
    # Se hace visible la pantalla dibujada más reciente
    pygame.display.flip()
