import pygame


class Obj(pygame.sprite.Sprite):
    def __init__(self, img, pos, z, t, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load(img).convert_alpha()
        self.image = pygame.transform.scale(self.image, t)
        self.rect = self.image.get_rect(topleft = pos)
        self.zcamadas = z

