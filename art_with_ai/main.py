__author__ = 'moejitow'

import sys
import time
import configparser
import pygame
from pygame.locals import QUIT
from art_with_ai import display
from art_with_ai import image


def main():
    config = configparser.ConfigParser()
    config.read('config.ini')
    mode = config['IMAGE']['hand_tracking']

    display.init_screen()

    render(mode)


def render(mode):
    if mode == 'motion':
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

    if mode == 'single':
        while True:

            image.take_image()
            landmarks = image.collect_landmarks()
            display.draw_lines(landmarks)

            for events in pygame.event.get():
                if events.type == QUIT:
                    sys.exit(0)

            time.sleep(1)
