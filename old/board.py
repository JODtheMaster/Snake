import pygame as pg
import random

class Turning:
    def __init__(self, posx, posy, direction):
        # Generate a turning point at a certain point (posx, posy)
        # which has a direction attribute. When the
        # snake reaches that point, it will turn in
        # the specified direction.

        self.direction = direction
        self.pos = [posx, posy]                  # Two values: x and y


# Blit food at random location.
def food(screen, loc):
    screen.blit(food, loc)