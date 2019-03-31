import pygame

def debug(params):
    if type(params) == list:
        for item in params:
            print(item)

size = windowWidth, windowHeight = 400, 400
display_surf = pygame.display.set_mode(size)

cols = 5
rows = 5
grid = []

cellWidth = windowWidth / rows
cellHeight = windowHeight / cols

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
