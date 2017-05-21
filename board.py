import pygame as pg
import random

from variables import *


class Turning:
    def __init__(self, posx, posy, direction):
        # Generate a turning point at a certain point (posx, posy)
        # which has a direction attribute. When the
        # snake reaches that point, it will turn in
        # the specified direction.

        self.direction = direction
        self.pos = [posx, posy]                  # Two values: x and y

    # Detect whether the segment is at the same position as the turning.
    # Returns a value of true if it is, false if it is not.
    def __isTurn__(self, segment):
        return self.pos == segment.pos


def mk_food(screen, food_pos):
    # Create first food. Must not be created in the snake segments.
    screen.blit(food, food_pos)

