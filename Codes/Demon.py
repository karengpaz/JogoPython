import pygame
import os
import random
from Config import WIN_WIDTH, WIN_HEIGHT

class Demon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(base_dir, '..', 'asset', 'Attackdemo2.png') #image demon
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.x = WIN_WIDTH + random.randint(10, 200)
        self.rect.y = random.randint(20, WIN_HEIGHT - 100)
        self.speed = random.randint(2, 5)

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()