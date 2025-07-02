import pygame

class Button:
    def __init__(self, screen, image_path):
        self.screen = screen
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = screen.get_rect().center

    def draw(self):
        self.screen.blit(self.image, self.rect)
