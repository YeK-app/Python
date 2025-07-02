import pygame
from pygame.sprite import Sprite

class AlienBullet(Sprite):
    def __init__(self, screen, settings, alien):
        super().__init__()
        self.screen = screen

        # Mermi görseli yerine basit dolu dikdörtgen kullanılıyor
        self.image = pygame.Surface((settings.alien_bullet_width, settings.alien_bullet_height))
        self.image.fill(settings.alien_bullet_color)
        self.rect = self.image.get_rect()

        # Başlangıç pozisyonu alien'ın altından
        self.rect.centerx = alien.rect.centerx
        self.rect.top = alien.rect.bottom

        self.speed = settings.alien_bullet_speed
        self.y = float(self.rect.y)

    def update(self):
        """Mermiyi aşağı doğru hareket ettirir"""
        self.y += self.speed
        self.rect.y = self.y

    def draw(self):
        self.screen.blit(self.image, self.rect)
