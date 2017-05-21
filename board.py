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


# This one returns a procedural food position.
# It makes sure that the food cannot be ANYWHERE near the food.
def get_food_pos(snake):
    food_pos = (random.randint(50, 750), random.randint(50, 550))

    # Detect if the food would be in the rectangle bounding any segment.
    # If so, repeat the function
    for segment in snake:

        if (food_pos[0] >= segment.pos[0] - 20) and (food_pos[0] <= segment.pos[0] + 20):
            if (food_pos[1] >= segment.pos[1] - 20) and (food_pos[1] <= segment.pos[1] + 20):

                get_food_pos(snake)

            else:
                return food_pos
        else:
            return food_pos

food_pos = (400, 300)