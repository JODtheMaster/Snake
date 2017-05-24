import pygame as pg
from enum import Enum
import time


# Images

# The following start as these certain defined images,
# But their contents shall change as the snake is rotated.
# That is why some of the other parts have exactly the same default value
# as them.
head   = pg.image.load("assets\images\snake head.png")
body   = pg.image.load("assets\images\snake body.png")
tail   = pg.image.load("assets\images\snake tail.png")

# Pivot point versions of body
left   = pg.image.load("assets\images\snake left.png")
right  = pg.image.load("assets\images\snake right.png")
up     = pg.image.load("assets\images\snake up.png")
down   = pg.image.load("assets\images\snake down.png")

# Flipped versions of pivot points
left_f   = pg.transform.flip(left, True, False)
right_f  = pg.transform.flip(right, True, False)
up_f     = pg.transform.flip(up, True, False)
down_f   = pg.transform.flip(down, True, False)

# Rotated versions of head
up_head    = pg.image.load("assets\images\snake head.png")
down_head  = pg.transform.rotate(up_head, 180)
left_head  = pg.transform.rotate(up_head, 90)
right_head = pg.transform.rotate(up_head, 270)

# Rotated versions of body
up_body    = pg.image.load("assets\images\snake body.png")
down_body  = pg.transform.rotate(up_body, 180)
left_body  = pg.transform.rotate(up_body, 90)
right_body = pg.transform.rotate(up_body, 270)

# Rotated versions of tail
up_tail    = pg.image.load("assets\images\snake tail.png")
down_tail  = pg.transform.rotate(up_tail, 180)
left_tail  = pg.transform.rotate(up_tail, 90)
right_tail = pg.transform.rotate(up_tail, 270)

food = pg.image.load("assets\images\\food.png")

grass = pg.image.load("assets\images\grass.png")
# Grass sprite provided by http://spritefx.blogspot.co.uk/2013/04/sprite-grass.html

wall       = pg.image.load("assets\images\wall.png")

game_over  = pg.image.load("assets\images\game over.png")

homescreen = pg.image.load("assets\images\homescreen.png")

# Load buttons
play_inactive = pg.image.load("assets\images\\buttons\play inactive.png")
play_active   = pg.image.load("assets\images\\buttons\play active.png")

settings_inactive = pg.image.load("assets\images\\buttons\settings inactive.png")
settings_active   = pg.image.load("assets\images\\buttons\settings active.png")

highscores_inactive = pg.image.load("assets\images\\buttons\highscores inactive.png")
highscores_active   = pg.image.load("assets\images\\buttons\highscores active.png")

home_inactive = pg.image.load("assets\images\\buttons\home inactive.png")
home_active = pg.image.load("assets\images\\buttons\home active.png")

pause_inactive = pg.image.load("assets\images\\buttons\pause inactive.png")
pause_active = pg.image.load("assets\images\\buttons\pause active.png")


# Directions
class Directions(Enum):
    LEFT  = 0
    RIGHT = 1
    UP    = 2
    DOWN  = 3

# Snake types
class Type(Enum):
    up_pivot    = 0
    down_pivot  = 1
    left_pivot  = 2
    right_pivot = 3

    head = 4
    body = 5
    tail = 6

    head_up = 7
    head_down = 8
    head_left = 9
    head_right = 10

    body_left  = 11
    body_right = 12
    body_up    = 13
    body_down  = 14

    tail_left  = 15
    tail_right = 16
    tail_up    = 17
    tail_down  = 18

    f_up_pivot    = 19
    f_down_pivot  = 20
    f_left_pivot  = 21
    f_right_pivot = 22

# Game settings
speed        = 40
score        = 0
games_played = 0

highscore_1 = 0
highscore_2 = 0
highscore_3 = 0

# Highscores for 2nd level
highscore_2x1 = 0
highscore_2x2 = 0
highscore_2x3 = 0

class States(Enum):
    # Different states the program can have at a certain time.
    RUNNING    = 0
    PAUSED     = 1
    GAMEOVER   = 2
    HOME       = 3                  # Home menu
    SETTINGS   = 4                  # Settings menu
    HIGHSCORES = 5                  # Highscores display

# Define the state the game is in.
state = States.HOME

# Game clock speed
fps = 10

# Method for getting highscores from the HIGHSCORES file
def get_highscores():
    # Open text file
    fp = open("highscores.txt", mode="r")

    # If the file contains nothing, keep highscores as 0 and break
    if fp.read() == None:
        return

    else:

        # Set as global so can be read
        global highscore_1, highscore_2, highscore_3, highscore_2x1, highscore_2x2, highscore_2x3
        # read each line and assign the value as a highscore.
        highscore_1 = fp.readline()
        highscore_2 = fp.readline()
        highscore_3 = fp.readline()

        highscore_2x1 = fp.readline()
        highscore_2x2 = fp.readline()
        highscore_2x3 = fp.readline()

        fp.close()

