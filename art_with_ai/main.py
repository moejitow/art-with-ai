__author__ = 'moejitow'

import sys
import time
import pygame
from pygame.locals import QUIT
from art_with_ai import display
from art_with_ai import image


def main():
    display.init_screen()

    prev_landmarks = []

    while True:
        image.take_image()

        curr_landmarks = image.collect_fingertip_landmarks()

        if (curr_landmarks):
            display.draw_hand_motion(prev_landmarks, curr_landmarks)
            prev_landmarks = curr_landmarks

        for events in pygame.event.get():
            if events.type == QUIT:
                sys.exit(0)

        time.sleep(1)
