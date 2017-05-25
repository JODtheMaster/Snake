import pygame as pg
from enum import Enum
import time
import shelve

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
new_highscore = pg.image.load("assets\images\\new highscore.png")

homescreen = pg.image.load("assets\images\homescreen.png")

pause_screen = pg.image.load("assets\images\paused screen.png")

""" Load buttons """
play_inactive = pg.image.load("assets\images\\buttons\play inactive.png")
play_active   = pg.image.load("assets\images\\buttons\play active.png")

settings_inactive = pg.image.load("assets\images\\buttons\settings inactive.png")
settings_active   = pg.image.load("assets\images\\buttons\settings active.png")

highscores_inactive = pg.image.load("assets\images\\buttons\highscores inactive.png")
highscores_active   = pg.image.load("assets\images\\buttons\highscores active.png")

home_inactive = pg.image.load("assets\images\\buttons\home inactive.png")
home_active   = pg.image.load("assets\images\\buttons\home active.png")

pause_inactive = pg.image.load("assets\images\\buttons\pause inactive.png")
pause_active   = pg.image.load("assets\images\\buttons\pause active.png")

add_inactive = pg.image.load("assets\images\\buttons\\add_speed_inactive.png")
add_active   = pg.image.load("assets\images\\buttons\\add_speed_active.png")

minus_inactive = pg.image.load("assets\images\\buttons\\minus_speed_inactive.png")
minus_active   = pg.image.load("assets\images\\buttons\\minus_speed_active.png")

resume_inactive = pg.image.load("assets\images\\buttons\\resume game inactive.png")
resume_active = pg.image.load("assets\images\\buttons\\resume game active.png")

level_1_inactive = pg.image.load("assets\images\\buttons\\level_1_inactive.png")
level_1_active = pg.image.load("assets\images\\buttons\\level_1_active.png")
level_2_inactive = pg.image.load("assets\images\\buttons\\level_2_inactive.png")
level_2_active = pg.image.load("assets\images\\buttons\\level_2_active.png")

level2 = False                  # If this is made true, then the second level is played.


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

# Highscores for first level
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
fps = 20

# Timing. This is used for moving the snake:
# The snake is only moved every certain number of frames
# determined by changing the next variable, which is DELAY
# These are both FLOATS
timing = 0.0
delay = 0.1


""" Functions used to change game states and variable values """

def store_highscores():
    # Method for storing highscores in the HIGHSCORES file.
    global highscore_1, highscore_2, highscore_3, highscore_2x1, highscore_2x2, highscore_2x3

    d = shelve.open("assets\highscores\highscores")
    # Store each as a variable.
    d['highscore 1'] = highscore_1
    d['highscore 2'] = highscore_2
    d['highscore 3'] = highscore_3

    d['highscore 2x1'] = highscore_2x1
    d['highscore 2x2'] = highscore_2x2
    d['highscore 2x3'] = highscore_2x3
    d.close()

def get_highscores():
    # Method for getting highscores from the HIGHSCORES file
    global highscore_1, highscore_2, highscore_3, highscore_2x1, highscore_2x2, highscore_2x3

    """# Open text file
    fp = open("highscores.txt", mode="r")

    # If the file contains nothing, keep highscores as 0 and break
    if fp.read() == None:
        return

    else:

        # Set as global so can be read
        global highscore_1, highscore_2, highscore_3, highscore_2x1, highscore_2x2, highscore_2x3
        # read each line and assign the value as a highscore.
        highscore_1 = int(fp.readline())
        highscore_2 = int(fp.readline())
        highscore_3 = int(fp.readline())

        highscore_2x1 = int(fp.readline())
        highscore_2x2 = int(fp.readline())
        highscore_2x3 = int(fp.readline())

        fp.close()"""
    try:
        d = shelve.open("assets\highscores\highscores")
        # Load each variable
        highscore_1 = d['highscore 1']
        highscore_2 = d['highscore 2']
        highscore_3 = d['highscore 3']

        highscore_2x1 = d['highscore 2x1']
        highscore_2x2 = d['highscore 2x2']
        highscore_2x3 = d['highscore 2x3']
        d.close()
    except:
        print("This file contains nothing!")


def timer():
    # This function creates a timer. The use of this is to speed the game up:
    # Setting the FPS to a slow level reduced the resposiveness of the game, meaning that
    # I decided to add a timer so that the snake is only moves every certain number of turns.
    # It is run under a second thread
    global frames_elapsed
    frames_elapsed = 0
    frames_elapsed += 1
    time.sleep(0.1)


def increase_speed():
    # Method for changing the delay time, thus increasing the speed.
    global delay
    if delay + 0.05 < 1:
        delay += 0.05

def decrease_speed():
    # Another method for changing the delay time, thus increasing the speed.
    # (we need two methods because currently, I cannot make the BUTTON command take arguments.
    global delay
    if delay - 0.05 > 0.05:
        delay -= 0.05

def level_1():
    # Change state to LEVEL 1:
    global level2
    level2 = False

def level_2():
    # Change state to LEVEL 2
    global level2
    level2 = True