import pygame

class Scoreboard:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.score = 0
        self.lives = settings.ship_limit
        self.high_score = 0

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.lives = self.settings.ship_limit

    def draw(self, font):
        score_text = font.render(f"PUAN: {self.score}", True, (0, 0, 0))
        self.screen.blit(score_text, (7, 7))
