import pygame
import os
from cena import *

#variaveis
image_path8 = os.path.join(img_dir2, 'ai-generated-8469399_1280.jpg')
image_path10 = os.path.join(img_dir, 'WhatsApp_Image_2024-10-10_at_22.26.36-removebg-preview.png')
image = pygame.image.load(image_path8)
fogo = pygame.image.load(image_path10)
lar = 1280
alt = 720
lar_fogo = 150
alt_fogo =150
tel = pygame.display.set_mode((lar, alt))
running = True
clock = pygame.time.Clock()
image_fogo = pygame.transform.scale(fogo,(lar_fogo,alt_fogo))
fundo = pygame.transform.scale(image,(lar,alt))




camera = 0
x = 0




#grupos
block = pygame.sprite.Group()