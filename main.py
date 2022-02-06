import sys

import pygame

from level import Level
from setting import *
from tiles import Tile

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Naruto Fight")
clock = pygame.time.Clock()
level = Level(level_map, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(bg_color)
    level.run()

    # update the UI
    pygame.display.update()
    clock.tick(60)
