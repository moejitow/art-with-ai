__author__ = 'moejitow'

import sys, pygame
from pygame.locals import*
from art_with_ai import constants as c


def main():
    screen=pygame.display.set_mode(c.SCREEN_SIZE)
    screen.fill(c.DARK_GREY)
    pygame.display.flip()

    pygame.draw.line(screen, c.RED, (60, 80), (10, 100))

    pygame.display.flip()

    while True:
        for events in pygame.event.get():
            if events.type == QUIT:
                sys.exit(0)
