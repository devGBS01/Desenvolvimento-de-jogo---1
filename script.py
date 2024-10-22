import pygame
import time
from pygame.locals import *
from sys import exit

pygame.init()
xpersonagem= 100
ypersonagem= 600
lar = 800
alt = 700
tel = pygame.display.set_mode((lar,alt))
running = True
clock = pygame.time.Clock()
tela = pygame.image.load('fundo.jpg')
bg = pygame.transform.scale(tela,(lar,alt))
mov = 0
img = pygame.image.load('fundo.jpg')
img_smooth = pygame.transform.smoothscale(img, (10,20))
slide_start_time = None
slide_duration = 1
 

class personagem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        super().__init__()
        
        self.img_smooth = pygame.transform.smoothscale(img, (800,700))
        self.sprites_idle = []
        self.sprites_idle.append(pygame.image.load('png/Idle (1).png'))
        self.sprites_idle.append(pygame.image.load('png/Idle (2).png'))
        self.sprites_idle.append(pygame.image.load('png/Idle (3).png'))
        self.sprites_idle.append(pygame.image.load('png/Idle (4).png'))
        self.sprites_idle.append(pygame.image.load('png/Idle (5).png'))
        self.sprites_idle.append(pygame.image.load('png/Idle (6).png'))
        self.sprites_idle.append(pygame.image.load('png/Idle (7).png'))
        self.sprites_idle.append(pygame.image.load('png/Idle (8).png'))
        self.sprites_idle.append(pygame.image.load('png/Idle (9).png'))
        self.sprites_idle.append(pygame.image.load('png/Idle (10).png'))
        self.sprites_hurt = []
        self.sprites_hurt.append(pygame.image.load('png/Hurt (1).png'))
        self.sprites_hurt.append(pygame.image.load('png/Hurt (2).png'))
        self.sprites_hurt.append(pygame.image.load('png/Hurt (3).png'))
        self.sprites_hurt.append(pygame.image.load('png/Hurt (4).png'))
        self.sprites_hurt.append(pygame.image.load('png/Hurt (5).png'))
        self.sprites_hurt.append(pygame.image.load('png/Hurt (6).png'))
        self.sprites_hurt.append(pygame.image.load('png/Hurt (7).png'))
        self.sprites_hurt.append(pygame.image.load('png/Hurt (8).png'))
        self.sprites_dead = []
        self.sprites_dead.append(pygame.image.load('png/Dead (1).png'))
        self.sprites_dead.append(pygame.image.load('png/Dead (2).png'))
        self.sprites_dead.append(pygame.image.load('png/Dead (3).png'))
        self.sprites_dead.append(pygame.image.load('png/Dead (4).png'))
        self.sprites_dead.append(pygame.image.load('png/Dead (5).png'))
        self.sprites_dead.append(pygame.image.load('png/Dead (6).png'))
        self.sprites_dead.append(pygame.image.load('png/Dead (7).png'))
        self.sprites_dead.append(pygame.image.load('png/Dead (8).png'))
        self.sprites_dead.append(pygame.image.load('png/Dead (9).png'))
        self.sprites_dead.append(pygame.image.load('png/Dead (10).png'))
        self.sprites_jump = []
        self.sprites_jump.append(pygame.image.load('png/Jump (1).png'))
        self.sprites_jump.append(pygame.image.load('png/Jump (2).png'))
        self.sprites_jump.append(pygame.image.load('png/Jump (3).png'))
        self.sprites_jump.append(pygame.image.load('png/Jump (4).png'))
        self.sprites_jump.append(pygame.image.load('png/Jump (5).png'))
        self.sprites_jump.append(pygame.image.load('png/Jump (6).png'))
        self.sprites_jump.append(pygame.image.load('png/Jump (7).png'))
        self.sprites_jump.append(pygame.image.load('png/Jump (8).png'))
        self.sprites_jump.append(pygame.image.load('png/Jump (9).png'))
        self.sprites_jump.append(pygame.image.load('png/Jump (10).png'))
        self.sprites_jump.append(pygame.image.load('png/Jump (11).png'))
        self.sprites_jump.append(pygame.image.load('png/Jump (12).png'))
        self.sprites_run = []
        self.sprites_run.append(pygame.image.load('png/Run (1).png'))
        self.sprites_run.append(pygame.image.load('png/Run (2).png'))
        self.sprites_run.append(pygame.image.load('png/Run (3).png'))
        self.sprites_run.append(pygame.image.load('png/Run (4).png'))
        self.sprites_run.append(pygame.image.load('png/Run (5).png'))
        self.sprites_run.append(pygame.image.load('png/Run (6).png'))
        self.sprites_run.append(pygame.image.load('png/Run (7).png'))
        self.sprites_run.append(pygame.image.load('png/Run (8).png'))
        self.sprites_slide = []
        self.sprites_slide.append(pygame.image.load('png/Slide (1).png'))
        self.sprites_slide.append(pygame.image.load('png/Slide (2).png'))
        self.sprites_slide.append(pygame.image.load('png/Slide (3).png'))
        self.sprites_slide.append(pygame.image.load('png/Slide (4).png'))
        self.sprites_slide.append(pygame.image.load('png/Slide (5).png'))
        self.agora = 0
        self.image = self.sprites_idle[self.agora]
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect(center=(100,100))
        self.rect.topleft = (100, 600)
        self.estado = "idle"
        
    def update(self):
        self.agora +=0.09
        if self.estado == "run":
            if self.agora >=len(self.sprites_run):
                self.agora=0
            self.image = self.sprites_run[int(self.agora)]
        elif self.estado == "slide":
            if self.agora >=len(self.sprites_slide):
                self.agora = 0
            self.image = self.sprites_slide[int(self.agora)]
        
        else:
            if self.agora >=len(self.sprites_idle):
                self.agora=0
            self.image = self.sprites_idle[int(self.agora)]
        self.image = pygame.transform.scale(self.image, (150, 150))

todas_sprites = pygame.sprite.Group()
person = personagem()
todas_sprites.add(person)
xpersonagem= 100
ypersonagem= 600


#programação
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        keys = pygame.key.get_pressed()
    
    if person.estado == "slide" and time.time() - slide_start_time > slide_duration:
        person.estado = "run"
    

    person.estado = "idle"
    if keys[K_d]:
        xpersonagem += 5
        if keys[K_LCTRL] and person.estado != "slide":
            person.estado = "slide"
            slide_start_time = time.time()         
        else:
            if keys [K_LSHIFT]:
                xpersonagem += 5
            xpersonagem += 5
            person.estado = "run"
    if keys[K_a]:
        if keys[K_LSHIFT]:
            xpersonagem -= 5
        xpersonagem -= 5
        person.estado = "run"
    if keys[K_s]:
        ypersonagem += 10
        person.estado = "run"
    if keys[K_w]:
        ypersonagem -= 10
        person.estado = "run"
    
    person.rect.topleft = (xpersonagem, ypersonagem)
    
    tel.fill((0,0,0))
    tel.blit(img_smooth, (500,0))
    tel.blit(bg, (mov, 0))
    tel.blit(bg,(lar+mov,0))
    mov -= 0.4

    if mov<= -lar:
        mov = 0

    todas_sprites.draw(tel)
    todas_sprites.update()
    


   
    pygame.display.flip()
    clock.tick(60)