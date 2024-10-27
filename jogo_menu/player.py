import pygame
from objetos import *
from variaveis import *
import os
import time
from pygame.locals import *
from script import *

base_dir= os.path.dirname(__file__)
img_dir = os.path.join(base_dir, 'imagens')
img_dir2 = os.path.join(base_dir, 'png')
image_path9= os.path.join(img_dir2, 'Idle (1).png')

class Player(pygame.sprite.Sprite):
  
    
    def __init__(self, img, pos, z, collision_sprite, t, *groups):
        super().__init__(*groups)
        self.time = time.time()
        self.todas_sprites = pygame.sprite.Group()
        self.person = personagem(pos, z, t)
        self.todas_sprites.add(self.person)

        self.image = pygame.image.load(img).convert_alpha()
        self.image = pygame.transform.scale(self.image, t)
        self.rect = self.image.get_rect(topleft = pos)
        self.zcamadas = z
        self.collision_sprites = collision_sprite
        self.direction = pygame.math.Vector2()
        self.speed=2
        self.frame = 0

    def input(self):
        self.slide_start_time = None
        self.slide_duration = 1

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        elif keys[pygame.K_LEFT]:
            self.rect.x -= 5
        else:
            self.direction.x = 0

        if self.person.estado == "slide" and self.time.time() - self.slide_start_time > self.slide_duration:
            self.person.estado = "run"

        self.person.estado = "idle"
        if keys[pygame.K_d]:
            self.rect.x += 5
            if keys[pygame.K_LCTRL] and self.person.estado != "slide":
                self.person.estado = "slide"
                self.slide_start_time = self.time.time()
            else:
                if keys[pygame.K_LSHIFT]:
                    self.rect.x += 5
                self.rect.x += 5
                self.person.estado = "run"
        if keys[pygame.K_a]:
            if keys[pygame.K_LSHIFT]:
                self.rect.x -= 5
            self.rect.x -= 5
            self.person.estado = "run"
        if keys[pygame.K_s]:
            self.rect.x -= 5
            self.person.estado = "run"
        if keys[pygame.K_w]:
            self.rect.x -= 5
            self.person.estado = "run"

    def move(self):
        self.rect.center += self.direction * self.speed
    def update(self):
        self.input()
        self.move()



running = True
clock = pygame.time.Clock()
base_dir = os.path.dirname(__file__)
img_dir2 = os.path.join(base_dir, 'png')

