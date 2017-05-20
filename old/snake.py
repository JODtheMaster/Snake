
import pygame as pg
from pygame.locals import *

from variables import *


class Snake:

    def __init__(self):

        # Call different Segment objects as list. This will make up the snake
        self.snake = [Segment(Type.head, [100, 100]), Segment(Type.body, [100, 140]), Segment(Type.tail, [100, 180])]

    def __display__(self, screen):

        # Render the snake onto the board
        for segment in self.snake:

            if segment.type == Type.head:
                screen.blit(head, segment.pos)
            elif segment.type == Type.body:
                screen.blit(body, segment.pos)
            elif segment.type == Type.tail:
                screen.blit(tail, segment.pos)

            # Turned versions
            if segment.type == Type.up:
                screen.blit(up, segment.pos)
            elif segment.type == Type.down:
                screen.blit(down, segment.pos)
            elif segment.type == Type.left:
                screen.blit(left, segment.pos)
            elif segment.type == Type.right:
                screen.blit(right, segment.pos)

    def __move__(self):

        # Move the entire snake
        for segment in self.snake:
            segment.__move__(segment.current_direction)


class Segment:

    def __init__(self, type, pos):
        self.direction = None  # Represents the direction that the instance of the snake object is moving
        self.type = type  # Represents the type it is (ie: rotated left, rotated right, head, tail, etc.)

        self.pos = pos
        self.current_direction = Directions.UP
        self.new_direction = None

    def __move__(self, current_direction):

        # Move the segment
        # Direction can either be left, right, up, down (l,r,u,d)
        if current_direction == Directions.RIGHT:
            self.pos[0] -= speed  # Remember that Pygame coordinates are negative quadrant-based
        elif current_direction == Directions.LEFT:
            self.pos[0] += speed
        elif current_direction == Directions.UP:
            self.pos[1] -= speed
        elif current_direction == Directions.DOWN:
            self.pos[1] += speed

    def __turn__(self, Turning):            # Turning references the turning class that we want.

        try:
            # Detect if the segment has reached the turning.
            if self.pos == Turning.pos:
                # Set the new_direction to that of the turning.
                self.new_direction = Turning.direction

                # Change segment version into turned version
                if self.type == Type.body:

                # Change segment type. Possible types include:
                # head, body, tail, left, right, up, down (lower case)
                    if Turning.direction == Directions.UP:
                        self.type = up
                    elif Turning.direction == Directions.DOWN:
                        self.type = down
                    elif Turning.direction == Directions.LEFT:
                        self.type = left
                    elif Turning.direction == Directions.RIGHT:
                        self.type = right

                # For the head, we shall just change the variable head to a rotated version
                # of itself (defined in VARIABLES).
                elif self.type == Type.head:
                    if Turning.direction == Directions.UP:
                        head = up_head
                    elif Turning.direction == Directions.DOWN:
                        head = down_head
                    elif Turning.direction == Directions.LEFT:
                        head = left_head
                    elif Turning.direction == Directions.RIGHT:
                        head = right_head

        except:
            raise Exception("This turning point doesn't exist!")

    def hit_edge(self):
        # Detect if the snake has hit the edge or not.

        # If the x pos of a segment is at the left or right:
        if self.pos[0] == 0 or self.pos[0] == 800:
            dead = True

        # If the y pos is at the top or bottom
        elif self.pos[1] == 0 or self.pos[1] == 600:
            dead = True


    # Python method for calling indexed objects.
    def __getitem__(self, key):
        return self.pos[key]
