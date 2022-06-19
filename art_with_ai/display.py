__author__ = 'moejitow'

import pygame
from art_with_ai import constants as c

screen = None


def init_screen():
    global screen
    screen = pygame.display.set_mode(c.SCREEN_SIZE)
    screen.fill(c.DARK_GREY)
    pygame.display.flip()


def draw_lines():
    print(screen)
    pygame.draw.line(screen, c.RED, (60, 80), (10, 100))

    pygame.display.flip()
