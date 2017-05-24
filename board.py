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

    # Draw pause and quit buttons
    screen.blit( Font.render("Pause", True, (255, 255, 255)) , (150, 5))
    button.picture_button(screen, variables.pause_inactive, variables.pause_active, 200, 5, pause)

    screen.blit( Font.render("Home", True, (255, 255, 255)) , (250, 5))
    button.picture_button(screen, variables.home_inactive, variables.home_active, 300, 5, home)

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

def home():
    # Change mode to display home screen
    variables.state = variables.States.HOME

def pause():
    # Change the game state so that the game pauses.
    variables.state = variables.States.PAUSED


""" Commands which draw the different types of window """

def homescreen(screen):
    # Draw homescreen background
    screen.blit(variables.homescreen, (0, 0))

    #Draw buttons
    button.picture_button(screen, variables.play_inactive, variables.play_active, 150, 250, play)
    button.picture_button(screen, variables.settings_inactive, variables.settings_active, 525, 250, settings)
    button.picture_button(screen, variables.highscores_inactive, variables.highscores_active, 525, 375, highscores)


def highscore_screen(screen):
    # Draw background (same as Homescreen)
    screen.blit(variables.homescreen, (0, 0))

    # draw rectangle where the scores are drawn in
    pg.draw.rect(screen, (48, 59, 51), (150, 190, 485, 350))

    # Draw home button
    button.picture_button(screen, variables.home_inactive, variables.home_active, 640, 60, home)

    """ Draw scores: """
    # Initialise font and draw text
    Font = pg.font.SysFont("yugothicregularyugothicuisemilight", 30, False, False)
    Title = Font.render("HIGHSCORES: ", True, (0, 255, 0))
    screen.blit(Title, (290, 200))

    Scores_1 = Font.render("Highest Scores on Level 1: ", True, (0, 255, 0))
    Scores_2 = Font.render("Highest Scores on Level 2: ", True, (0, 255, 0))

    score_1  = Font.render(str(variables.highscore_1), True, (255, 255, 255))
    score_2  = Font.render(str(variables.highscore_2), True, (255, 255, 255))
    score_3 = Font.render(str(variables.highscore_3), True, (255, 255, 255))

    score_4 = Font.render(str(variables.highscore_2x1), True, (255, 255, 255))
    score_5 = Font.render(str(variables.highscore_2x2), True, (255, 255, 255))
    score_6 = Font.render(str(variables.highscore_2x3), True, (255, 255, 255))

    # Blit all text to screen
    screen.blit(Scores_1, (210, 230))
    screen.blit(score_1, (250, 260))
    screen.blit(score_2, (250, 290))
    screen.blit(score_3, (250, 320))

    screen.blit(Scores_2, (210, 350))
    screen.blit(score_4, (250, 260))
    screen.blit(score_5, (250, 290))
    screen.blit(score_6, (250, 320))


def settings_screen(screen):
    # Draws the screen where all the settings are

    # Draw background (same as Homescreen)
    screen.blit(variables.homescreen, (0, 0))

    """ Render title text """
    Font = pg.font.SysFont("yugothicregularyugothicuisemilight", 35, False, False)
    title = Font.render("SETTINGS", True, (255, 255, 255))
    screen.blit(title, (300, 200))

    """ Now, we shall draw the speed-changer thing"""
    pg.draw.rect(screen, (48, 59, 51), (360, 290, 50, 50))

    screen.blit( Font.render(str(variables.speed), True, (255, 255, 255)) , (365, 300))

