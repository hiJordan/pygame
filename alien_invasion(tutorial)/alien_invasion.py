import pygame
from settings import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from score_board import ScoreBoard


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    stats = GameStats(ai_settings)
    sb = ScoreBoard(ai_settings, screen, stats)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    play_button = Button(ai_settings, screen, 'PLAY')

    while True:
        gf.check_events(ai_settings, screen, ship, bullets, stats, play_button, aliens, sb)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets, stats, sb)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets, sb)

        gf.update_screen(ai_settings, screen, ship, aliens, bullets, stats, play_button, sb)


run_game()

