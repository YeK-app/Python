import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, screen, settings, alien_type, x, y):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.alien_type = alien_type

        # Alien türüne göre görsel ve puan ayarı
        if alien_type == 1:
            self.image = pygame.image.load("images/alien1.png").convert_alpha()
            self.points = 10
        elif alien_type == 2:
            self.image = pygame.image.load("images/alien2.png").convert_alpha()
            self.points = 20
        else:
            self.image = pygame.image.load("images/alien3.png").convert_alpha()
            self.points = 30

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, direction):
        """Alien'ı yatay yönde hareket ettirir"""
        self.rect.x += self.settings.alien_speed * direction

    def drop_down(self):
        """Alien'ları aşağı kaydırır"""
        self.rect.y += 20

    def draw(self):
        self.screen.blit(self.image, self.rect)
