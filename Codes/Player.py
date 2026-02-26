import pygame
import os
from Config import WIN_WIDTH, WIN_HEIGHT

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(base_dir, '..', 'asset', 'Attack1.png') #image dragon
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (120, 120))
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.centery = WIN_HEIGHT // 2
        self.speed = 5
        self.health = 100

      #movements with wasd
    def update(self):
        keys = pygame.key.get_pressed() #captures keys pressed
        if keys[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.bottom < WIN_HEIGHT:
            self.rect.y += self.speed
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.right < WIN_WIDTH:
            self.rect.x += self.speed

    def draw_health_bar(self, display):
        bar_width = 200
        bar_height = 20
        fill = (self.health / 100) * bar_width
        border = pygame.Rect(10, 10, bar_width, bar_height)
        fill_rect = pygame.Rect(10, 10, fill, bar_height)
        pygame.draw.rect(display, (0, 255, 0), fill_rect)
        pygame.draw.rect(display, (255, 255, 255), border, 2)