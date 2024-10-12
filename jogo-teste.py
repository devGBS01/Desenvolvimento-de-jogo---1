import pygame
import sys
from pygame.locals import *
from fases import *
from objetos import *
from sena import Cena
from variaveis import *

pygame.init()


#classes
class Chao(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        pygame.init()
        self.display = pygame.display.set_mode([lar,alt])
        self.Block = Cena()
        self.mapa()
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Escape from the Castle")



 

    def update(self):
        pass


    def run(self):
        # loop
        while True:
            mov = lar
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


            self.display.fill('black')
            self.Block.run()
            pygame.display.flip()
            self.clock.tick(60)



        keys = pygame.key.get_pressed()

        if keys == [K_d]:
            mov += 1

    def mapa(self):
        pass


game = Chao()
game.run()

