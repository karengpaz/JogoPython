import pygame
import os
from Config import WIN_WIDTH

class DragonFire(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(base_dir, '..', 'asset', 'Fire_Attack1.png') #image fire
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.centery = y
        self.speed = 10  #pixels for frame

    def update(self):
        self.rect.x += self.speed
        if self.rect.left > WIN_WIDTH:
            self.kill()