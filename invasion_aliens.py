from pickle import TRUE
import sys 
import pygame

def run_game():
    # Inicializar el juego y crear un objeto pantalla
      pygame.init()
      pantalla = pygame.display.set_mode((800, 600))
      pygame.display.set_caption("Invasión Alienígena")
    
    # Iniciar el bucle principal del juego
      while True:
        
        # Sirve para escuahr eventos de teclado o ratón
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Se hace visible la pantalla dibujada más reciente
        pygame.display.flip()

run_game()