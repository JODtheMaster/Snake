
import pygame as pg
from pygame.locals import *

from variables import *


class Snake:

    def __init__(self):

        # Call different Segment objects as list. This will make up the snake
        self.snake = [Segment(Type.head, [100, 200]), Segment(Type.body, [100, 240]), Segment(Type.tail, [100, 280])]

    def __display__(self, screen):

        # Render the snake onto the board
        for segment in self.snake:

            if segment.type == Type.head:
                screen.blit(head, segment.pos)
            elif segment.type == Type.body:
                screen.blit(body, segment.pos)
            elif segment.type == Type.tail:
                screen.blit(tail, segment.pos)

            # Blit pivot point versions
            elif segment.type == Type.up_pivot:
                screen.blit(up, segment.pos)
            elif segment.type == Type.down_pivot:
                screen.blit(down, segment.pos)
            elif segment.type == Type.left_pivot:
                screen.blit(left, segment.pos)
            elif segment.type == Type.right_pivot:
                screen.blit(right, segment.pos)

            # Blit rotated head versions
            elif segment.type == Type.head_up:
                screen.blit(up_head, segment.pos)
            elif segment.type == Type.head_down:
                screen.blit(down_head, segment.pos)
            elif segment.type == Type.head_left:
                screen.blit(left_head, segment.pos)
            elif segment.type == Type.head_right:
                screen.blit(right_head, segment.pos)

            # Blit rotated body versions
            elif segment.type == Type.body_up:
                screen.blit(up_body, segment.pos)
            elif segment.type == Type.body_down:
                screen.blit(down_body, segment.pos)
            elif segment.type == Type.body_left:
                screen.blit(left_body, segment.pos)
            elif segment.type == Type.body_right:
                screen.blit(right_body, segment.pos)

            # Blit rotated tail versions
            elif segment.type == Type.tail_up:
                screen.blit(up_tail, segment.pos)
            elif segment.type == Type.tail_down:
                screen.blit(down_tail, segment.pos)
            elif segment.type == Type.tail_left:
                screen.blit(left_tail, segment.pos)
            elif segment.type == Type.tail_right:
                screen.blit(right_tail, segment.pos)



    def __move__(self):

        # Move the entire snake
        for segment in self.snake:
            segment.__move__(segment.direction)


class Segment:

    def __init__(self, type, pos):
        self.direction = Directions.UP
        self.type = type  # Represents the type it is (ie: rotated left, rotated right, head, tail, etc.)

        self.pos = pos

    def __move__(self, direction):

        # Move the segment
        # Direction can either be left, right, up, down
        if direction == Directions.RIGHT:
            self.pos[0] += speed  # Remember that Pygame coordinates are negative quadrant-based
        elif direction == Directions.LEFT:
            self.pos[0] -= speed
        elif direction == Directions.UP:
            self.pos[1] -= speed
        elif direction == Directions.DOWN:
            self.pos[1] += speed

    """def __turn__(self, Turning):            # Turning references the turning class that we want.

        try:
            # Detect if the segment has reached the turning.
            if self.pos == Turning.pos:


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
            raise Exception("This turning point doesn't exist!")"""

    # Method for turning the snake
    def __turn__(self, direction):
        # If the segment is a body type, then change the type to the rotated segment type.
        # !!! If the segment is a head or tail type, we will not execute any turn because
        # !!! the direction changes only apply to self.type == body
        # !!! this is also true for for Type.up, Type.down, Type.left, Type.right. You need to
        # !!! rethink the logic here.
        #print("__turn__ direction", direction, "type: ", self.type)
        if self.type == Type.body or self.type == Type.body_up or self.type == Type.body_down or self.type == Type.body_left or self.type == Type.body_right:
            if direction == Directions.UP:
                self.type = Type.up_pivot
                self.direction = Directions.UP

            elif direction == Directions.DOWN:
                self.type = Type.down_pivot
                self.direction = Directions.DOWN

            elif direction == Directions.LEFT:
                self.type = Type.left_pivot
                self.direction = Directions.LEFT

            elif direction == Directions.RIGHT:
                self.type = Type.right_pivot
                self.direction = Directions.RIGHT

        elif self.type == Type.head or self.type == Type.head_down or self.type == Type.head_up or self.type == Type.head_left or self.type == Type.head_right:
            if direction == Directions.UP:
                self.type = Type.head_up
                self.direction = Directions.UP

            elif direction == Directions.DOWN:
                self.type = Type.head_down
                self.direction = Directions.DOWN

            elif direction == Directions.LEFT:
                self.type = Type.head_left
                self.direction = Directions.LEFT

            elif direction == Directions.RIGHT:
                self.type = Type.head_right
                self.direction = Directions.RIGHT

        elif self.type == Type.tail or self.type == Type.tail_up or self.type == Type.tail_down or self.type == Type.tail_left or self.type == Type.tail_right:
            if direction == Directions.UP:
                self.type = Type.tail_up
                self.direction = Directions.UP

            elif direction == Directions.DOWN:
                self.type = Type.tail_down
                self.direction = Directions.DOWN

            elif direction == Directions.LEFT:
                self.type = Type.tail_left
                self.direction = Directions.LEFT

            elif direction == Directions.RIGHT:
                self.type = Type.tail_right
                self.direction = Directions.RIGHT

    def __edge__(self):
        # Detect if the snake has hit the edge or not.

        # If the x pos of a segment is at the left or right:
        if self.pos[0] == 0 or self.pos[0] == 800:
            dead = True

        # If the y pos is at the top or bottom
        elif self.pos[1] == 0 or self.pos[1] == 600:
            dead = True

    def __notTurn__(self):
        # This method detects for turned versions of segments and turns them back to the original "body",
        # albeit rotated, after it leaves the turning point.
        # The fact that it has left the turning point is defined just before the line is referenced (see Graphics)

        # If it is a turned version:
        if self.type == Type.left_pivot or self.type == Type.right_pivot or self.type == Type.up_pivot or self.type == Type.down_pivot:
            # Change to rotated version for different directions.
            if self.direction == Directions.UP:
                self.type = Type.body_up
            elif self.direction == Directions.DOWN:
                self.type = Type.body_down
            elif self.direction == Directions.LEFT:
                self.type = Type.body_left
            elif self.direction == Directions.RIGHT:
                self.type = Type.body_right



    # Python method for calling indexed objects.
    def __getitem__(self, key):
        return self.pos[key]
