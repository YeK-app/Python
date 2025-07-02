import pygame
import sys
import random

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from alien_bullet import AlienBullet
from explosion import Explosion
from fruit import Fruit
from scoreboard import Scoreboard
from button import Button

def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("ALIENS GAME")

    clock = pygame.time.Clock()
    font = pygame.font.SysFont("impact", 36)

    # Arka plan resmi
    background = pygame.image.load("images/background.jpg").convert()
    background = pygame.transform.scale(background, (settings.screen_width, settings.screen_height))

    # Sesler
    laser_sound = pygame.mixer.Sound("sounds/laser.wav")
    explosion_sound = pygame.mixer.Sound("sounds/explosion.wav")
    level_up_sound = pygame.mixer.Sound("sounds/level_up.wav")

    # Oyun nesneleri
    play_button = Button(screen, "images/play_button.png")
    ship = Ship(screen, settings)
    bullets = pygame.sprite.Group()
    aliens = pygame.sprite.Group()
    alien_bullets = pygame.sprite.Group()
    explosions = pygame.sprite.Group()
    fruits = pygame.sprite.Group()
    scoreboard = Scoreboard(screen, settings)

    game_active = False
    alien_direction = 1
    alien_shoot_timer = 0
    fruit_timer = 0
    level = 1

    def create_fleet():
        aliens.empty()
        alien_type_list = [1, 2, 3]
        for row in range(3):
            for col in range(10):
                x = 60 + col * 60
                y = 60 + row * 60
                alien_type = alien_type_list[row % 3]
                alien = Alien(screen, settings, alien_type, x, y)
                aliens.add(alien)

    def reset_game():
        nonlocal game_active, level
        game_active = True
        level = 1
        settings.alien_speed = 1.0
        settings.ship_speed = 5.0
        scoreboard.reset()
        bullets.empty()
        alien_bullets.empty()
        explosions.empty()
        fruits.empty()
        ship.center_ship()
        ship.health = 3
        ship.speed = settings.ship_speed
        create_fleet()

    def draw_health_bar(surface, x, y, health, max_health):
        ratio = health / max_health
        color = (0, 255, 0) if ratio > 0.7 else (255, 255, 0) if ratio > 0.3 else (255, 0, 0)
        pygame.draw.rect(surface, (255, 255, 255), (x - 2, y - 2, 64, 10))
        pygame.draw.rect(surface, (0, 0, 0), (x, y, 60, 6))
        pygame.draw.rect(surface, color, (x, y, 60 * ratio, 6))

    # Ana oyun döngüsü
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN and not game_active:
                if play_button.rect.collidepoint(pygame.mouse.get_pos()):
                    reset_game()

            elif event.type == pygame.KEYDOWN and game_active:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = True
                elif event.key == pygame.K_SPACE and len(bullets) < settings.max_bullets:
                    bullets.add(Bullet(screen, settings, ship))
                    laser_sound.play()

            elif event.type == pygame.KEYUP and game_active:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = False

        screen.blit(background, (0, 0))

        if game_active:
            # Güncelle
            ship.update()
            bullets.update()
            alien_bullets.update()
            explosions.update()
            fruits.update()

            # Çarpışmalar
            for bullet in bullets.copy():
                for alien in aliens.copy():
                    if bullet.rect.colliderect(alien.rect):
                        explosions.add(Explosion(screen, alien.rect.center))
                        explosion_sound.play()
                        scoreboard.score += alien.points
                        bullets.remove(bullet)
                        aliens.remove(alien)
                        break

            # Uzaylı yön değişimi
            change_direction = False
            for alien in aliens:
                alien.update(alien_direction)
                if alien.rect.right >= settings.screen_width or alien.rect.left <= 0:
                    change_direction = True
            if change_direction:
                alien_direction *= -1
                for alien in aliens:
                    alien.drop_down()

            # Uzaylı mermisi
            alien_shoot_timer += 1
            if alien_shoot_timer > 50:
                if aliens:
                    shooter = random.choice(list(aliens))
                    alien_bullets.add(AlienBullet(screen, settings, shooter))
                alien_shoot_timer = 0

            for alien_bullet in alien_bullets.copy():
                if alien_bullet.rect.colliderect(ship.rect):
                    explosions.add(Explosion(screen, ship.rect.center))
                    explosion_sound.play()
                    alien_bullets.remove(alien_bullet)
                    ship.health -= 1
                    if ship.health <= 0:
                        game_active = False

            # Elma
            fruit_timer += 0.5
            if fruit_timer > 300:
                fruits.add(Fruit(screen, settings, 'green'))
                fruit_timer = 0

            for fruit in fruits.copy():
                if fruit.rect.colliderect(ship.rect):
                    if ship.health < 3:
                        ship.health += 1
                    fruits.remove(fruit)

            if not aliens:
                level += 1
                settings.alien_speed += 1.2
                create_fleet()

            # Çizimler
            ship.draw()
            bullets.draw(screen)
            alien_bullets.draw(screen)
            for alien in aliens:
                alien.draw()
            for explosion in explosions:
                explosion.draw()
            for fruit in fruits:
                fruit.draw()
            scoreboard.draw(font)
            draw_health_bar(screen, ship.rect.centerx - 30, ship.rect.bottom + 1, ship.health, 3)

        else:
            # Başlangıç ekranı
            play_button.draw()
            rule1 = font.render("GREEN STARS = +1 HEALTH", True, (0, 0, 0))
            screen.blit(rule1, (screen.get_width() // 2 - rule1.get_width() // 2, 440))
            high_score_text = font.render(f"HIGH SCORE: {scoreboard.high_score}", True, (0, 0, 0))
            screen.blit(high_score_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    run_game()
 