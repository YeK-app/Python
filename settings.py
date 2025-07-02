class Settings:
    def __init__(self):
        # Ekran ayarları
        self.screen_width = 1024
        self.screen_height = 768

        # Gemi ayarları
        self.ship_speed = 5.0
        self.ship_limit = 3

        # Oyuncu mermisi ayarları (artık görsel kullanılacak)
        self.bullet_speed = 10
        self.max_bullets = 999999

        # Uzaylı ayarları
        self.alien_speed = 1.0

        # Uzaylı mermisi ayarları
        self.alien_bullet_speed = 5
        self.alien_bullet_width = 3
        self.alien_bullet_height = 15
        self.alien_bullet_color = (255, 0, 0)
