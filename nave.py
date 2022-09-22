import pygame

class Nave():
    """Sirve para gestionar el comportamiento de la nave"""

    def __init__(self, pantalla):
        """Inicializa la nave y establece su posición de partida"""

        self.pantalla = pantalla

        # Carga la imagen de la nave y obtiene su rect
        self.imagen = pygame.image.load("imagenes/nave.bmp")
        self.rect = self.imagen.get_rect()
        self.pantalla_rect = pantalla.get_rect()

        # Empieza cada nueva nave en la parte inferior central de la pantalla
        self.rect.centerx = self.pantalla_rect.centerx
        self.rect.bottom = self.pantalla_rect.bottom
    
    def blitme(self):
        """Dibuja la nave en su ubicación actual"""
        self.pantalla.blit(self.imagen, self.rect)