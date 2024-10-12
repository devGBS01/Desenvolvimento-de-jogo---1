import pygame

#variaveis
lar = 1280
alt = 720
tel = pygame.display.set_mode((lar, alt))
running = True
clock = pygame.time.Clock()
bg = pygame.transform.scale(tel, (lar, alt))


#grupos
block = pygame.sprite.Group()