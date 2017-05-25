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
import variables
from snake import *
from board import *
from variables import States, Directions

# Call snake class
snake = Snake()
global snake

turns = []


# NB: The Graphics happens under the while loop, so it continues to execute.
def Graphics(screen):

        variables.state = States.RUNNING

        # Render grass
        for x in range(0, 800, 40):
            for y in range(0, 600, 40):
                screen.blit(grass, (x, y))

        boardObjects(screen)

        # Render snake. This must be given under the while loop
        snake.display(screen)

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
            if snake.snake[0].direction is not Directions.DOWN:             # You cannot turn from down to up.
                turns.append(Turning(snake.snake[0].pos[0], snake.snake[0].pos[1], Directions.UP))

        elif keys[K_a]:
            if snake.snake[0].direction is not Directions.RIGHT:
                turns.append(Turning(snake.snake[0].pos[0], snake.snake[0].pos[1], Directions.LEFT))

        elif keys[K_s]:
            if snake.snake[0].direction is not Directions.UP:
                turns.append(Turning(snake.snake[0].pos[0], snake.snake[0].pos[1], Directions.DOWN))

        elif keys[K_d]:
            if snake.snake[0].direction is not Directions.LEFT:
                turns.append(Turning(snake.snake[0].pos[0], snake.snake[0].pos[1], Directions.RIGHT))


        # Continuously detect whether the segment is at a turning point:
        for segment in snake.snake:
            for i in range(len(snake.snake)):
                for turn in turns:

                    if turn.__isTurn__(segment):                          # turning.__isTurn__()returns true if segment and turning have same pos
                        segment.turn(turn.direction, snake.snake[i - 1])         # Turn the snake's segment in the direction specified

                        #print("Turning in", turn.direction, "segment type", segment.type, "snake direction:", segment.direction)
                    else:

                    # We also need to continuously detect whether the turned segment has LEFT the turning point.
                    # If it has, we change it to a rotated version of the body.
                        segment.notTurn()

        global food_pos
        screen.blit(food, food_pos)

        # !!! Detect whether snake has collided with food
        if snake.detectHeadCollideFood(food_pos):
            #print("Food eaten!")
            snake.eat()
            variables.score += speed                # Why are we doing this? The faster you go, the more your score multiplier!

            #print(variables.score)
            #for turn in turns:
                #print("Turn at: ", turn.pos)

            food_pos = (random.randint(50, 750), random.randint(50, 550))

            screen.blit(food, get_food_pos(snake.snake))

        # Remove turn once the tail has passed the turning point.
        # Since this is after the code that turns in the tail should already have been turned.
        for turn in turns:
            if turn.pos == snake.snake[-1].pos:
                turns.remove(turn)

        """ Snake Death Messages """

        # Kill the snake if a segment collides with another.
        # We need 2 "for" loops to test every single segment with every single other segment.
        for seg1 in snake.snake:
            for seg2 in snake.snake:
                if seg1 is not seg2:
                    if seg1.collision(seg2.pos[0], seg2.pos[1]):
                        variables.state = States.GAMEOVER
                        #print("Dead at: ", seg1.pos, seg2.pos, "Type: ", seg1.type, seg2.type)

        # Kill the snake if any segment of it hits the side.
        # Originally it was just going to be tge head
        for segment in snake.snake:
            if segment.pos[0] <= 30 or segment.pos[0] >= 770:
                variables.state = States.GAMEOVER
                #print("Dead")
            elif segment.pos[1] <= 30 or segment.pos[1] >= 560:
                variables.state = States.GAMEOVER
                #print("Dead")

        """ Constantly move the snake forward. """
        # This is only done every certain number of frames. After that, we will reset the timer.
        # That is why we are using TIMER.
        # !!! I moved this until after the key press detection. It makes more sense to
        # !!! detect which keys have been pressed and then do the moving afterwards.
        # !!! I also slowed down speed to 5, for now.
        if variables.state is States.RUNNING:
            if variables.timing > variables.delay:
                snake.move()
                variables.timing = 0
                #print(delay)
        #time.sleep(0.5)  # Delay before next movement of snake


        def game_over():
            # Method for displaying game over screen (used a LOT in next section)
            screen.blit(variables.game_over, (0, 0))
            button.picture_button(screen, variables.home_inactive, variables.home_active, 325, 600, home)
            snake.reset()

        # Lose screen
        if variables.state is States.GAMEOVER:
            # Detect for new highscore, for each different level type
            # This is quite long, but it is basically iterating over each different case.
            if level2 is False:
                if variables.score > variables.highscore_1:
                    variables.highscore_1 = variables.score
                    screen.blit(variables.new_highscore, (0, 0))
                    snake.reset()

                elif variables.score > variables.highscore_2:
                    variables.highscore_2 = variables.score
                    game_over()
                elif variables.score > variables.highscore_3:
                    variables.highscore_3 = variables.score
                    game_over()
                else:
                    game_over()

            elif level2 is True:
                if variables.score > variables.highscore_2x1:
                    variables.highscore_2x1 = variables.score
                    screen.blit(variables.game_over, (0, 0))
                    snake.reset()

                elif variables.score > variables.highscore_2x2:
                    variables.highscore_2x2 = variables.score
                    game_over()
                elif variables.score > variables.highscore_2x3:
                    variables.highscore_2x3 = variables.score
                    game_over()
                else:
                    game_over()
            # Refresh Highscore Storage
            variables.store_highscores()

        # Update timer.
        # The delay between each update would be 0.05, since it is 20 FPS (regularly)
        variables.timing += 0.05
