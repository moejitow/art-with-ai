__author__ = 'moejitow'

import sys, pygame
from pygame.locals import QUIT
from art_with_ai import display


def main():
    display.init_screen()

    display.draw_lines()

    while True:
        for events in pygame.event.get():
            if events.type == QUIT:
                sys.exit(0)
