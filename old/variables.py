import pygame as pg
from enum import Enum

# colours
white = (255, 255, 255)
black = (0, 0, 0)

# Images
play_i = pg.image.load("assets\images\play inactive.png")
play_a = pg.image.load("assets\images\play active.png")

head   = pg.image.load("assets\images\snake head.png")
body   = pg.image.load("assets\images\snake body.png")
tail   = pg.image.load("assets\images\snake tail.png")

left   = pg.image.load("assets\images\snake head.png")
right  = pg.image.load("assets\images\snake right.png")
up     = pg.image.load("assets\images\snake head.png")
down   = pg.image.load("assets\images\snake head.png")

# Rotated versions of head
up_head    = pg.image.load("assets\images\snake head.png")
down_head  = pg.transform.rotate(up_head, 180)
left_head  = pg.transform.rotate(up_head, 270)
right_head = pg.transform.rotate(up_head, 90)

#food = pg.image.load("assets\images\food.png")

# Directions
class Directions(Enum):
    LEFT  = 0
    RIGHT = 1
    UP    = 2
    DOWN  = 3

# Snake types
class Type(Enum):
    up    = 0
    down  = 1
    left  = 2
    right = 3

    head = 4
    body = 5
    tail = 6

# Game settings
speed        = 30
score        = 0
highscore    = 0
games_played = 0

dead = False            # Determines whether the snake has died yet
