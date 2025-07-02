import pygame
import random
from pygame.sprite import Sprite

class Fruit(Sprite):
    def __init__(self, screen, settings, fruit_type='green'):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.fruit_type = fruit_type
        
        # Sadece yeşil yıldız var, kırmızı iptal
        if self.fruit_type == 'green':
            self.image = pygame.image.load("images/green_stars.png").convert_alpha()
        
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, settings.screen_width - self.rect.width)
        self.rect.y = -self.rect.height  # Ekranın üstünden başlar
        self.speed = 2

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > self.settings.screen_height:
            self.kill()

    def draw(self):
        self.screen.blit(self.image, self.rect)
