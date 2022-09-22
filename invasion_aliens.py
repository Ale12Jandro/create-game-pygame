import pygame
from nave import Nave
from configuraciones import Configuraciones

import funciones_juego as fj

def run_game():
    # Inicializar el juego, las configuraciones y creamos un objeto pantalla
      pygame.init()
      ai_configuraciones = Configuraciones()

      pantalla = pygame.display.set_mode((ai_configuraciones.screen_width, ai_configuraciones.screen_height))
      pygame.display.set_caption("Invasión Alienígena")

      # Crea una nave
      nave = Nave(pantalla)
     

    # Iniciar el bucle principal del juego
      while True:
        
        # Sirve para escuahr eventos de teclado o ratón
        fj.verificar_eventos()
        fj.actualizar_pantalla(ai_configuraciones, pantalla, nave)

run_game()
