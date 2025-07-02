import pygame

class Ship:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load("images/ship.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.y -= 10  # biraz yukarı kaydır

        self.x = float(self.rect.x)
        self.speed = settings.ship_speed

        self.moving_right = False
        self.moving_left = False

        self.max_health = 3
        self.health = self.max_health

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.speed

        self.rect.x = self.x

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.y -= 10
        self.x = float(self.rect.x)
        self.health = self.max_health
        self.speed = self.settings.ship_speed
