import pygame

from fases import *


class Camera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

        self.display = pygame.display.get_surface()
        self.mov = pygame.math.Vector2()

    def seguindo(self):
        for layer in camadas.values():
            for sprites in self.sprites():
                if sprites.zcamadas == layer:
                    self.display.blit(sprites.image, sprites.rect)
