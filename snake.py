
import pygame as pg
from pygame.locals import *

from variables import *


class Snake:

    def __init__(self):

        # Call different Segment objects as list. This will make up the snake
        self.snake = [Segment(Type.head, [100, 200], Directions.UP), Segment(Type.body, [100, 240], Directions.UP), Segment(Type.tail, [100, 280], Directions.UP)]

    def display(self, screen):

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

            # Blit flipped versions of pivot points
            elif segment.type == Type.f_up_pivot:
                screen.blit(up_f, segment.pos)
            elif segment.type == Type.f_down_pivot:
                screen.blit(down_f, segment.pos)
            elif segment.type == Type.f_left_pivot:
                screen.blit(left_f, segment.pos)
            elif segment.type == Type.f_right_pivot:
                screen.blit(right_f, segment.pos)

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

    def detectHeadCollideFood(self, food_pos):
        # !!! Get the position of the head of the snake
        head_pos_x = self.snake[0].pos[0]
        head_pos_y = self.snake[0].pos[1]
        food_pos_x = food_pos[0]
        food_pos_y = food_pos[1]
        # !!! Work out the rectangle bounded by the snake head.
        # !!! On x axis, this is head_pos[0] - 20 .. head_pos[0] + 20
        # !!! On y axis, this is head_pos[1] - 20 .. head_pos[1] + 20
        if (food_pos_x >= head_pos_x - 20) and (food_pos_x <= head_pos_x + 20):
            if (food_pos_y >= head_pos_y - 20) and (food_pos_y <= head_pos_y + 20):
                # !!! We have food in the box bounded by the snake head
                return True


    def move(self):

        # Move the entire snake
        for segment in self.snake:
            segment.move(segment.direction)

    def eat(self):
        # Makes the snake longer by changing the last in the list to a body and then
        # appends a new tail.
        # Before just appending, we must know which direction it is travelling in so we know which version to append.

        if self.snake[-1].direction == Directions.LEFT:
            # Compute pos of appended segment:
            a_pos = [self.snake[-1].pos[0] + 40, self.snake[-1].pos[1]]

            # Append and change type
            self.snake[-1].type = Type.body_left
            self.snake.append(Segment(Type.tail_left, a_pos, Directions.LEFT))

        elif self.snake[-1].direction == Directions.RIGHT:
            a_pos = [self.snake[-1].pos[0] - 40, self.snake[-1].pos[1]]

            self.snake[-1].type = Type.body_right
            self.snake.append(Segment(Type.tail_right, a_pos, Directions.RIGHT))

        elif self.snake[-1].direction == Directions.UP:
            a_pos = [self.snake[-1].pos[0], self.snake[-1].pos[1] + 40]

            self.snake[-1].type = Type.body_up
            self.snake.append(Segment(Type.tail_up, a_pos, Directions.UP))

        elif self.snake[-1].direction == Directions.DOWN:
            a_pos = [self.snake[-1].pos[0], self.snake[-1].pos[1] - 40]

            self.snake[-1].type = Type.body_down
            self.snake.append(Segment(Type.tail_down, a_pos, Directions.DOWN))

        #print("Eat with new tail at: ", self.snake[-1].pos, " added after: ", self.snake[-2].pos)
        #print("... with new direction: ", self.snake[-1].direction, " after: ", self.snake[-2].direction)


class Segment:

    def __init__(self, type, pos, direction):
        self.direction = direction
        self.type = type  # Represents the type it is (ie: rotated left, rotated right, head, tail, etc.)

        self.pos = pos


    def move(self, direction):

        # Move the segment. The way we will do this is to change the pos, which
        # thus affects where the segment is blitted.
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
    def turn(self, direction, previous_segment):
        # If the segment is a body type, then change the type to the rotated segment type.
        # Here, we need to handle every single case so the code is very long.
        # Most of it is just repetitions of itself with different event cases.
        # Thus, explanations are only given for the first of each type of motion

        """# !!! If the segment is a head or tail type, we will not execute any turn because
        # !!! the direction changes only apply to self.type == body
        # !!! this is also true for for Type.up, Type.down, Type.left, Type.right. You need to
        # !!! rethink the logic here.
        #print("__turn__ direction", direction, "type: ", self.type)"""

        # If the segment is any sort of BODY:
        if self.type == Type.body or self.type == Type.body_up or self.type == Type.body_down or self.type == Type.body_left or self.type == Type.body_right:

            """"# If the turning point wants it to turn UP:
            if direction == Directions.UP:
                # Turn it up
                self.direction = Directions.UP
                # Change the pivot type so it fits between this one and the previous. (This is why we need the prev direction)
                if previous_segment.direction == Directions.LEFT:
                    self.type = Type.up_pivot
                elif previous_segment.direction == Directions.RIGHT:
                    self.type = Type.f_up_pivot

            elif direction == Directions.DOWN:
                self.direction = Directions.DOWN
                if previous_segment.direction == Directions.LEFT:
                    self.type = Type.down_pivot
                elif previous_segment.direction == Directions.RIGHT:
                    self.type = Type.f_down_pivot

            elif direction == Directions.LEFT:
                self.direction = Directions.LEFT
                if previous_segment.direction == Directions.UP:
                    self.type = Type.left_pivot
                elif previous_segment.direction == Directions.DOWN:
                    self.type = Type.f_left_pivot

            elif direction == Directions.RIGHT:
                self.direction = Directions.RIGHT
                if previous_segment.direction == Directions.UP:
                    self.type = Type.right_pivot
                elif previous_segment.direction == Directions.DOWN:
                    self.type = Type.f_right_pivot"""

            # If the turning point wants it to turn UP:
            if direction == Directions.UP:
                # Turn it up
                self.direction = Directions.UP
                # Change the pivot type so it fits between this one and the previous. (This is why we need the prev direction)
                if previous_segment.direction == Directions.LEFT:
                    self.type = Type.up_pivot
                    # Move the segment and previous segments (why? This is so they do not go inside each other whilst turning)
                    # This is different depending on the direction of the previous segment.
                    #self.pos[1] -= 40
                    #previous_segment.pos[0] -= 40
                elif previous_segment.direction == Directions.RIGHT:
                    self.type = Type.f_up_pivot

                    #self.pos[1] -= 40
                    #previous_segment.pos[0] += 40

            elif direction == Directions.DOWN:
                self.direction = Directions.DOWN
                if previous_segment.direction == Directions.LEFT:
                    self.type = Type.down_pivot

                    #self.pos[1] += 40
                    #previous_segment.pos[0] -= 40

                elif previous_segment.direction == Directions.RIGHT:
                    self.type = Type.f_down_pivot

                    #self.pos[1] += 40
                    #previous_segment.pos[0] += 40

            elif direction == Directions.LEFT:
                self.direction = Directions.LEFT
                if previous_segment.direction == Directions.UP:
                    self.type = Type.left_pivot

                    #self.pos[0] -= 40
                    #previous_segment.pos[1] -= 40

                elif previous_segment.direction == Directions.DOWN:
                    self.type = Type.f_left_pivot

                    #self.pos[0] -= 40
                    #previous_segment.pos[1] += 40

            elif direction == Directions.RIGHT:
                self.direction = Directions.RIGHT
                if previous_segment.direction == Directions.UP:
                    self.type = Type.right_pivot

                    #self.pos[0] += 40
                    #previous_segment.pos[1] -= 40

                elif previous_segment.direction == Directions.DOWN:
                    self.type = Type.f_right_pivot

                    #self.pos[0] += 40
                    #previous_segment.pos[1] += 40

        # If the type is snake head:
        elif self.type == Type.head or self.type == Type.head_down or self.type == Type.head_up or self.type == Type.head_left or self.type == Type.head_right:

            """if direction == Directions.UP:
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
                self.direction = Directions.RIGHT"""
            if direction == Directions.UP:
                self.direction = Directions.UP
                self.type = Type.head_up
                # if previous_segment.direction == Directions.LEFT:
                #     #self.pos[1] -= 40
                #     previous_segment.pos[0] -= 40
                #
                # elif previous_segment.direction == Directions.RIGHT:
                #     self.pos[1] -= 40
                #     previous_segment.pos[0] += 40

            elif direction == Directions.DOWN:
                self.direction = Directions.DOWN
                self.type = Type.head_down
                # if previous_segment.direction == Directions.LEFT:
                #     self.pos[1] += 40
                #     previous_segment.pos[0] -= 40
                #
                # elif previous_segment.direction == Directions.RIGHT:
                #     self.pos[1] += 40
                #     previous_segment.pos[0] += 40

            elif direction == Directions.LEFT:
                self.direction = Directions.LEFT
                self.type = Type.head_left
                # if previous_segment.direction == Directions.UP:
                #     self.pos[0] -= 40
                #     previous_segment.pos[1] -= 40
                #
                # elif previous_segment.direction == Directions.DOWN:
                #     self.pos[0] -= 40
                #     previous_segment.pos[1] += 40

            elif direction == Directions.RIGHT:
                self.direction = Directions.RIGHT
                self.type = Type.head_right
                # if previous_segment.direction == Directions.UP:
                #     self.pos[0] += 40
                #     previous_segment.pos[1] -= 40
                #
                # elif previous_segment.direction == Directions.DOWN:
                #     self.pos[0] += 40
                #     previous_segment.pos[1] += 40


        elif self.type == Type.tail or self.type == Type.tail_up or self.type == Type.tail_down or self.type == Type.tail_left or self.type == Type.tail_right:

            """if direction == Directions.UP:
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
                self.direction = Directions.RIGHT"""
            if direction == Directions.UP:
                self.direction = Directions.UP
                self.type = Type.tail_up
                # if previous_segment.direction == Directions.LEFT:
                #     self.pos[1] -= 40
                #     previous_segment.pos[0] -= 40
                #
                # elif previous_segment.direction == Directions.RIGHT:
                #     self.pos[1] -= 40
                #     previous_segment.pos[0] += 40

            elif direction == Directions.DOWN:
                self.direction = Directions.DOWN
                self.type = Type.tail_down
                # if previous_segment.direction == Directions.LEFT:
                #     self.pos[1] += 40
                #     previous_segment.pos[0] -= 40
                #
                # elif previous_segment.direction == Directions.RIGHT:
                #     self.pos[1] += 40
                #     previous_segment.pos[0] += 40

            elif direction == Directions.LEFT:
                self.direction = Directions.LEFT
                self.type = Type.tail_left
                # if previous_segment.direction == Directions.UP:
                #     self.pos[0] -= 40
                #     previous_segment.pos[1] -= 40
                #
                # elif previous_segment.direction == Directions.DOWN:
                #     self.pos[0] -= 40
                #     previous_segment.pos[1] += 40

            elif direction == Directions.RIGHT:
                self.direction = Directions.RIGHT
                self.type = Type.tail_right
                # if previous_segment.direction == Directions.UP:
                #     self.pos[0] += 40
                #     previous_segment.pos[1] -= 40
                #
                # elif previous_segment.direction == Directions.DOWN:
                #     self.pos[0] += 40
                #     previous_segment.pos[1] += 40


    def isEdge(self):
        # Detect if the snake has hit the edge or not.

        # If the x pos of a segment is at the left or right:
        if self.pos[0] == 0 or self.pos[0] == 800:
            dead = True

        # If the y pos is at the top or bottom
        elif self.pos[1] == 0 or self.pos[1] == 600:
            dead = True


    def notTurn(self):
        # This method detects for turned versions of segments and turns them back to the original "body",
        # albeit rotated, after it leaves the turning point.
        # The fact that it has left the turning point is defined just before the line is referenced (see Graphics)

        # If it is a turned version:
        if self.type == Type.left_pivot or self.type == Type.right_pivot or self.type == Type.up_pivot or self.type == Type.down_pivot or self.type == Type.f_left_pivot or self.type == Type.f_right_pivot or self.type == Type.f_up_pivot or self.type == Type.f_down_pivot:
                # Change to rotated version for different directions.
                if self.direction == Directions.UP:
                    self.type = Type.body_up
                elif self.direction == Directions.DOWN:
                    self.type = Type.body_down
                elif self.direction == Directions.LEFT:
                    self.type = Type.body_left
                elif self.direction == Directions.RIGHT:
                    self.type = Type.body_right


    def collision(self, posx, posy):
        # Method for working out if segment has collided with another (40x40) object.
        # Assumes width of everything is 40.
        if (posx >= self.pos[0] - 20) and (posx <= self.pos[0] + 20):
            if (posy >= self.pos[1] - 20) and (posy <= self.pos[1] + 20):
                return True


    # Python method for calling indexed objects.
    def __getitem__(self, key):
        return self.pos[key]
