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

turns = []


# NB: The Graphics happens under the while loop, so it continues to execute.
class Graphics:
    def __init__(self, screen):

        # Render grass
        for x in range(0, 800, 40):
            for y in range(0, 600, 40):
                screen.blit(grass, (x, y))

        # Render snake. This must be given under the while loop
        snake.__display__(screen)

        """      Motion handler      """

       # Get key events
        keys = pg.key.get_pressed()


        # Define different "turnings" for different key events
        # !!! You are correctly setting a turning point when a key is pressed
        # !!! but... you are allowing only a single turning point, and each time
        # !!! a key is pressed this will change, so the other snake segments never
        # !!! turn to follow the first one.

        """
        We are placing the turning at the snake's head position.
        snake.snake[0].pos[0] is snake head, position x value, and snake.snake[0].pos[1] is y value.

        This is rather complex. The first "snake" is the OBJECT of class Snake, the second "snake" is
        the list snake[] within the snake object. The [0] means head (the head is the first instance in
        the list).
        The pos[] is a list containing 2 values that are the x and y pos of each segment. We are creating
        the Turning point at the position of the head.
        """
        if keys[K_w]:
            turns.append(Turning(snake.snake[0].pos[0], snake.snake[0].pos[1], Directions.UP))

        elif keys[K_a]:
            turns.append(Turning(snake.snake[0].pos[0], snake.snake[0].pos[1], Directions.LEFT))

        elif keys[K_s]:
            turns.append(Turning(snake.snake[0].pos[0], snake.snake[0].pos[1], Directions.DOWN))

        elif keys[K_d]:
            turns.append(Turning(snake.snake[0].pos[0], snake.snake[0].pos[1], Directions.RIGHT))


        # Continuously detect whether the segment is at a turning point:
        for segment in snake.snake:
            for turn in turns:

                if turn.__isTurn__(segment):                 # turning.__isTurn__()returns true if segment and turning have same pos
                    segment.__turn__(turn.direction)         # Turn the snake's segment in the direction specified
                    #print("Turning in", turn.direction, "segment type", segment.type, "snake direction:", segment.direction)
                else:
                # We also need to continuously detect whether the turned segment has LEFT the turning point.
                # If it has, we change it to a rotated version of the body.
                    segment.__notTurn__()


        # Constantly move the snake forward.
        # !!! I moved this until after the key press detection. It makes more sense to
        # !!! detect which keys have been pressed and then do the moving afterwards.
        # !!! I also slowed down speed to 5, for now.
        snake.__move__()
        #time.sleep(0.5)  # Delay before next movement of snake

        mk_food(screen, (500, 500))

        if
            print("Food eaten!")
            food_pos = (random.randint(50, 750), random.randint(50, 550))
            mk_food(screen, food_pos)

        # Every 4 secs, reset Turning point list so it does not turn if you collide with a turning again.


