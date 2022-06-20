__author__ = 'moejitow'

import sys
import time
import pygame
from pygame.locals import QUIT
from art_with_ai import display
from art_with_ai import image


def main():
    display.init_screen()

    while True:

        image.take_image()
        landmarks = image.collect_landmarks()
        display.draw_lines(landmarks)
        time.sleep(1)

        for events in pygame.event.get():
            if events.type == QUIT:
                sys.exit(0)
