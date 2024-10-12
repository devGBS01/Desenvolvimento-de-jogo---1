import pygame
from fases import fase1, tamanho, camadas
from objetos import *

class Cena:
    def __init__(self):


        self.display = pygame.display.get_surface()
        self.block = pygame.sprite.Group()
        self.mapa()

    def mapa(self):

        for row_index, row in enumerate(fase1):
            for col_index, col in enumerate(row):
                x = col_index * tamanho
                y = row_index * tamanho
                print(x, y)

                if col == "x":
                    Obj('/home/guilherme/Documentos/IFSP/lógica de  programação/Desenvolvimento_de_jogo/WhatsApp Image 2024-10-04 at 19.46.02.jpeg',
                        [x, y], camadas["blocos"], self.block)

    def run(self):
        self.block.draw(self.display)
        self.block.update()


