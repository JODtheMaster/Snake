import pygame as pg
from enum import Enum
import time

# colours
white = (255, 255, 255)
black = (0, 0, 0)


# Images
play_i = pg.image.load("assets\images\play inactive.png")
play_a = pg.image.load("assets\images\play active.png")

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


# Game settings
speed        = 40
score        = 0
highscore    = 0
games_played = 0

dead = False            # Determines whether the snake has died yet

