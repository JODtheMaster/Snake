import pygame as pg
import random

import button
import variables

class Turning:
    def __init__(self, posx, posy, direction):
        # Generate a turning point at a certain point (posx, posy)
        # which has a direction attribute. When the
        # snake reaches that point, it will turn in
        # the specified direction.

        self.direction = direction
        self.pos = [posx, posy]                  # Two values: x and y

    # Detect whether the segment is at the same position as the turning (within bounds of 40, which is the size of a seg)
    # Returns a value of true if it is, false if it is not.
    def __isTurn__(self, segment):
        #if self.pos[0] - 10 < segment.pos[0] and self.pos[0] + 10 > segment.pos[0]:
            #if self.pos[1] + 10 > segment.pos[1] and self.pos[1] - 10 < segment.pos[1]:
                #return True
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


def boardObjects(screen):
    # Create bar at top with highscore, pause, exit,
    pg.draw.rect(screen, (38, 77, 0), (0, 0, 800, 40))

    # Initialise font
    Font = pg.font.SysFont("yugothicregularyugothicuisemilight", 30, False, False)
    # Draw text by creating Surface and then blitting
    Score = Font.render("Score: " + str(variables.score), True, (225, 255, 0))
    screen.blit(Score, (500, 5))

    # Draw walls
    for x in range(0, 800, 40):
        screen.blit(variables.wall, (x, 580))
    for y in range(0, 600, 40):
        screen.blit(variables.wall, (-20, y))
        screen.blit(variables.wall, (780, y))


""" Commands which change the game state """
def play():
    # Change game status to play
    variables.state = variables.States.RUNNING

def settings():
    # Change game status to display settings page
    variables.state = variables.States.SETTINGS

def highscores():
    # Change game status to display highscore page
    variables.state = variables.States.HIGHSCORES


""" Commands which draw the different types of window """

def homescreen(screen, graphics_command):
    # Draw homescreen background
    screen.blit(variables.homescreen, (0, 0))

    #Draw buttons
    button.picture_button(screen, variables.play_inactive, variables.play_active, 150, 250, play)
    button.picture_button(screen, variables.settings_inactive, variables.settings_active, 525, 250, settings)
    button.picture_button(screen, variables.highscores_inactive, variables.highscores_active, 525, 375, highscores)


