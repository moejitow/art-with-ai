__author__ = 'moejitow'

from re import I
import cv2
import mediapipe as mp
import pygame
import pygame.camera

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

IMG_NAME = 'filename.png'


def collect_landmarks():
    # For static images:
    with mp_hands.Hands(static_image_mode=True, max_num_hands=2,
                        min_detection_confidence=0.5) as hands:
        # Read an image, flip it around y-axis for correct handedness output
        image = cv2.flip(cv2.imread(IMG_NAME), 1)
        # Convert the BGR image to RGB before processing
        results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        landmarks = []

        try:
            for face in results.multi_hand_landmarks:
                for landmark in face.landmark:
                    landmarks.append({'x': landmark.x, 'y': landmark.y})
        finally:
            return landmarks


def take_image():
    pygame.camera.init()
    if pygame.camera.list_cameras():
        # TODO: replace hardcoded argument
        cam = pygame.camera.Camera("/dev/video0", (1280, 720))
        cam.start()
        img = cam.get_image()
        pygame.image.save(img, IMG_NAME)
        cam.stop()
