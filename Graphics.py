"""
Snake game - code by Joshua O'Donoghue, as project for COMSCI 2017
Graphics.py

This module is in charge of handling graphics and movement of the snake.
However, the actual snake classes and commands for moving it are defined in snake.py.
"""
import pygame as pg
from pygame.locals import *
import time

from button import *
from variables import *
from snake import *
from board import *

# Call snake class
snake = Snake()


# NB: The Graphics happens under the while loop, so it continues to execute.
class Graphics:
    def __init__(self, screen):

        screen.fill((51, 102, 0))           # This is a dark forest green colour

        # Render snake. This must be given under the while loop
        snake.__display__(screen)

        """      Motion handler      """

       # Get key events
        keys = pg.key.get_pressed()

        # Initialise turning
        # !!! If you initialise turning each time you enter the loop, you get rid of
        # !!! all of the turning history. You probably don't want to do this.
        turning = None


        # Define different "turnings" for different key events
        # !!! You are correctly setting a turning point when a key is pressed
        # !!! but... you are allowing only a single turning point, and each time
        # !!! a key is pressed this will change, so the other snake segments never
        # !!! turn to follow the first one.
        if keys[K_w]:
            turning = Turning(snake.snake[0].pos[0], snake.snake[0].pos[1], Directions.UP)

        elif keys[K_a]:
            turning = Turning(snake.snake[0].pos[0], snake.snake[0].pos[1], Directions.LEFT)

        elif keys[K_s]:
            turning = Turning(snake.snake[0].pos[0], snake.snake[0].pos[1], Directions.DOWN)

        elif keys[K_d]:
            turning = Turning(snake.snake[0].pos[0], snake.snake[0].pos[1], Directions.RIGHT)


        # Continuously detect whether the segment is at a turning point:
        if turning is not None:
            for segment in snake.snake:
                if turning.__isTurn__(segment):                 # turning.__isTurn__()returns true if segment and turning have same pos
                    segment.__turn__(turning.direction)         # Turn the snake's segment in the direction specified

        # Constantly move the snake forward.
        # !!! I moved this until after the key press detection. It makes more sense to
        # !!! detect which keys have been pressed and then do the moving afterwards.
        # !!! I also slowed down speed to 5, for now.
        snake.__move__()
        time.sleep(0.5)  # Delay before next movement of snake

        """
        We are placing the turning at the snake's head position.
        snake.snake[0].pos[0] is snake head, position x value, and snake.snake[0].pos[1] is y value.

        This is rather complex. The first "snake" is the OBJECT of class Snake, the second "snake" is
        the list snake[] within the snake object. The [0] means head (the head is the first instance in
        the list).
        The pos[] is a list containing 2 values that are the x and y pos of each segment. We are creating
        the Turning point at the position of the head.
        """