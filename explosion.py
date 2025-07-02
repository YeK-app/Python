import pygame
from pygame.sprite import Sprite

class Explosion(Sprite):
    def __init__(self, screen, center):
        super().__init__()
        self.screen = screen
        self.images = []
        self.load_images()
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.counter = 0

    def load_images(self):
        # Patlama animasyonundaki tüm kareleri yükle
        for i in range(9):
            img_path = f"images/explosion{0}.png"
            img = pygame.image.load(img_path).convert_alpha()
            self.images.append(img)

    def update(self):
        # Animasyonu ilerlet
        self.counter += 1
        if self.counter >= 4:  # Her 4 frame’de bir kare değişir
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.kill()  # Animasyon bittiğinde nesneyi sil
            else:
                self.image = self.images[self.index]

    def draw(self):
        self.screen.blit(self.image, self.rect)
