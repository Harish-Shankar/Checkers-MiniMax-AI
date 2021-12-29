from sys import path
import pygame
import os.path as path

temp = path.abspath(path.join(__file__, "../.."))
filepath = path.join(temp, "images/crown.png")

""" print(two_up)
print(filepath) """

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

# rgb
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

#CROWN = pygame.transform.scale(pygame.image.load('images/crown.png'), (45, 25))
CROWN = pygame.transform.scale(pygame.image.load(filepath), (45, 25))
