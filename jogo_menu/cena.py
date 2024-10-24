import pygame
import os
from camera import Camera
from fases import *
from fogo import *
from objetos import *
from variaveis import *
base_dir= os.path.dirname(__file__)
img_dir = os.path.join(base_dir, 'imagens')
img_dir2 = os.path.join(base_dir, 'png')

image_path1 = os.path.join(img_dir2, 'bloco.png')
image_path2 = os.path.join(img_dir2, 'fogo3.png')
image_path2_1 = os.path.join(img_dir2, 'fogo2.png')
image_path2_2 = os.path.join(img_dir2, 'fogo1.png')
image_path3 = os.path.join(img_dir, 'WhatsApp_Image_2024-10-12_at_19.46.21-removebg-preview.png')
image_path4 = os.path.join(img_dir, 'WhatsApp_Image_2024-10-13_at_10.47.12-removebg-preview.png')
image_path5 = os.path.join(img_dir, 'WhatsApp_Image_2024-10-14_at_17.12.45-removebg-preview.png')
image_path6 = os.path.join(img_dir, 'WhatsApp_Image_2024-10-14_at_12.52.29-removebg-preview.png')
image_path7 = os.path.join(img_dir, 'WhatsApp_Image_2024-10-14_at_17.15.24-removebg-preview.png')


bloco = pygame.image.load(image_path1)
imagem2 = pygame.image.load(image_path2)
imagem3 = pygame.image.load(image_path3)
imagem4 = pygame.image.load(image_path4)
imagem5 = pygame.image.load(image_path5)
imagem6 = pygame.image.load(image_path6)
espinhos_teto = pygame.image.load(image_path7)



class Cena:
    def __init__(self):


        self.display = pygame.display.get_surface()
        self.colisão = pygame.sprite.Group()
        self.block = Camera()
        self.mapa()
        

    def mapa(self):

        for row_index, row in enumerate(fase1):
            for col_index, col in enumerate(row):
                x = col_index * tamanho
                y = row_index * tamanho
                print(x, y)

                if col == "x":
                    Obj(image_path1,
                        [x, y], camadas["segundo"], [150,150],self.block)

                if col == "l":       
                    Anima(
                        [x, y], camadas["primeiro"],[170,170], self.block)

                if col == "li":
                    Anima(
                        [x, y], camadas["primeiro"],[100,170], self.block)

                if col == "sp":
                    Obj(image_path4,
                        [x, y], camadas["primeiro"], [200, 200], self.block)

                if col == "t":
                    Obj(image_path5,
                        [x, y], camadas["primeiro"], [130, 130], self.block)

                if col == "p":
                    Obj(image_path6,
                        [x, y], camadas["terceiro"], [370, 370], self.block)

                if col == "tr":
                    Obj(image_path7,
                        [x, y], camadas["terceiro"], [130, 130], self.block)

    def run(self):
        self.block.seguindo()
        self.block.update()


