import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, screen, settings, ship):
        super().__init__()
        self.screen = screen

        # PNG görüntüsünü yükle
        self.image = pygame.image.load("images/bullet.png").convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)
        self.speed = settings.bullet_speed

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw(self):
        self.screen.blit(self.image, self.rect)
