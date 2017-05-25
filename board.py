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

    # Draw pause button
    screen.blit( Font.render("Pause", True, (255, 255, 255)) , (150, 5))
    button.picture_button(screen, variables.pause_inactive, variables.pause_active, 250, 5, pause)

    #screen.blit( Font.render("Home", True, (255, 255, 255)) , (250, 5))
    #button.picture_button(screen, variables.home_inactive, variables.home_active, 300, 5, home)

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

def home_screen(screen):
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
    screen.blit(score_4, (250, 380))
    screen.blit(score_5, (250, 410))
    screen.blit(score_6, (250, 440))

    #print("Your highscore is" + str(variables.highscore_1))



def settings_screen(screen):
    # Draws the screen where all the settings are

    # Draw background (same as Homescreen)
    screen.blit(variables.homescreen, (0, 0))

    """ Render title text """
    Font = pg.font.SysFont("yugothicregularyugothicuisemilight", 35, False, False)
    FontSmall = pg.font.SysFont("yugothicregularyugothicuisemilight", 20, False, False)
    title = Font.render("SETTINGS", True, (255, 255, 255))
    screen.blit(title, (310, 200))

    """ Now, we shall draw the speed-changer thing"""
    screen.blit( Font.render("Change Speed", True, (0, 220, 250)) , (280, 250))

    pg.draw.rect(screen, (48, 59, 51), (345, 290, 80, 50))

    screen.blit( Font.render(str( round(variables.delay, 2) ), True, (255, 0, 0)) , (353, 300))
    screen.blit(FontSmall.render("(Lower numbers are faster. Speed affects your score.)", True, (0, 0, 0)), (175, 350))

    # Draw buttons to change delay time (speed)
    button.picture_button(screen, variables.minus_inactive, variables.minus_active, 300, 295, variables.decrease_speed)
    button.picture_button(screen, variables.add_inactive, variables.add_active, 430, 295, variables.increase_speed)

    """ Draw buttons to change the level """

    screen.blit(Font.render("Change Level", True, (0, 220, 250)), (280, 400))

    # Set one level button to be active depending on which level is played.
    if variables.level2 == True:
        button.picture_button(screen, variables.level_1_inactive, variables.level_1_active, 325, 450, variables.level_1)
        button.picture_button(screen, variables.level_2_active, variables.level_2_active, 390, 450, variables.level_2)
    else:
        button.picture_button(screen, variables.level_1_active, variables.level_1_active, 325, 450, variables.level_1)
        button.picture_button(screen, variables.level_2_inactive, variables.level_2_active, 390, 450, variables.level_2)

    # Render the HOME button
    button.picture_button(screen, variables.home_inactive, variables.home_active, 680, 475, home)


def pausescreen(screen):
    # Render the screen for PAUSED mode
    screen.blit(variables.pause_screen, (0, 0))
    # Render RESUME button
    button.picture_button(screen, variables.resume_inactive, variables.resume_active, 225, 150, play)
    # Render the HOME button
    button.picture_button(screen, variables.home_inactive, variables.home_active, 325, 250, home)
    # Render SETTINGS button
    button.picture_button(screen, variables.settings_inactive, variables.settings_active, 325, 375, settings)


#def level_two():
    # Method for drawing second level, which has