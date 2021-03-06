__author__ = 'moejitow'

import pygame
from art_with_ai import constants as c

screen = None


def init_screen():
    global screen
    screen = pygame.display.set_mode(c.SCREEN_SIZE)
    screen.fill(c.DARK_GREY)
    pygame.display.flip()


def draw_hand_motion(prev_landmarks: list, curr_landmarks: list):

    if prev_landmarks and curr_landmarks:
        for count, value in enumerate(prev_landmarks):
            prev = (
                value['x'] * c.SCREEN_WIDTH,
                value['y'] * c.SCREEN_HEIGHT
            )
            curr = (
                curr_landmarks[count]['x'] * c.SCREEN_WIDTH,
                curr_landmarks[count]['y'] * c.SCREEN_HEIGHT
            )
            pygame.draw.line(screen, c.COLORS[count], prev, curr, 2)

    pygame.display.flip()


color_counter = 0


def draw_lines(landmarks: list):
    global color_counter
    try:
        count = 0
        color_counter += 1
        while count < len(landmarks):
            curr = (
                landmarks[count]['x'] * c.SCREEN_WIDTH,
                landmarks[count]['y'] * c.SCREEN_HEIGHT
            )
            next = (
                landmarks[count+1]['x'] * c.SCREEN_WIDTH,
                landmarks[count+1]['y'] * c.SCREEN_HEIGHT
            )

            pygame.draw.line(
                screen,
                c.COLORS[color_counter % 5],
                curr,
                next,
                2
            )

            count += 1

    except IndexError:
        pass

    pygame.display.flip()
