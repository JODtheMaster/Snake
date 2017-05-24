"""
Snake game - code by Joshua O'Donoghue, as project for COMSCI 2017
main.py

This module is in change of creating the screen and initialising the main game loop.
This module is what actually runs the program.
"""

# Load builtins
import pygame as pg
from pygame.locals import *
import _thread

# Load my own modules
import button           # Button is a module that I wrote myself that allows simple and fast implementation of buttons
from snake import *
from variables import States
from board import *
from Graphics import *

pg.init()

# Create class for controlling the game.
class Controller():
    def __init__(self):

        # Initialise screen and its variables
        width, height = 800, 600
        screen = pg.display.set_mode((width, height))
        pg.display.set_caption("Snake v1.0")
        #screen.fill(white)

        # Load highscores
        get_highscores()

        # Initialise pygame game loop by getting all events and checking if quit is true
        while True:
            for ev in pg.event.get():
                if ev.type == pg.QUIT:
                    pg.quit()

            # Create game clock
            clock = pg.time.Clock()
            clock.tick(fps)

            # Check for different game states to render different "screens"
            if variables.state == States.HOME:
                homescreen(screen)
            elif variables.state == States.RUNNING:
                Graphics(screen)                                # This is the most important handler, contains all game data
            elif variables.state == States.HIGHSCORES:
                highscore_screen(screen)
            elif variables.state == States.SETTINGS:
                settings_screen(screen)
            #Graphics(screen)

            # Continuously update pygame display
            pg.display.flip()


# Run if type is __main__:
if __name__ == "__main__":
    Controller()
