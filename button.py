"""
VERSION USED IN SNAKE GAME FOR COMSCI PROJECT

When I was coding a project at home, I discovered that simply implementing buttons
in Pygame took a lot of time. So, with a couple of hours, I sat down and made this
module that allowed a button to easily be created on the screen in a single command.

At the moment, the buttons MUST be exactly the same size or they won't work, and one will be overlayed
on top of the other.
"""
import pygame as pg
import time

def Button(Surface, text, font, posx, posy, width, height, colour, textCol, eventColour, command=None):
    """This command is used to call a Button.
    Surface describes the pygame.Surface to draw the button on.
    Text described the caption of the button.
    Font describes the font of the text.
    posx represents x coordinate, posy represents y coordinate.
    Width and height control the size of the button.
    Colour describes the seize of the button.
    textCol represents the colour of the text.
    eventColour tells you what color to change the button to when the mouse is hovered over it.
    command described the function the button calls when clicked.
    I had lots of help writing this from:
    https://pythonprogramming.net/pygame-button-function-events/?completed=/pygame-button-function/
    Thank you to that website.
    """
    mousepos = pg.mouse.get_pos()   #get mouse position
    clicked = pg.mouse.get_pressed()    #check if click event happens
    #Here we are checking where the mouse is and if anything has been clicked.
    if posx + width > mousepos[0] > posx and posy + height > mousepos[1] > posy:    #if mouse is in rect. I did not make up this maths, it is from the website.
        pg.draw.rect(Surface, eventColour, (posx, posy, width, height))      #Draw a rect of event colour
        if clicked[0] == True and command != None:      #and if click happens and there IS a command to do:
            command()               #Do the command
            clicked = False
            time.sleep(0.1)         #Create a delay so the button doesn't think it keeps being pressed.

    else:
        pg.draw.rect(Surface, colour, (posx, posy, width, height))   #Otherwise, just draw a normal button.

    #Define text:
    Font = pg.font.SysFont(font, 20)   #Define font
    text = Font.render(text, True, textCol)     #Define text.
    textcentre = ((posx + (width / 2)), (posy + (height / 2))) #Work out the place to blit the text object from. I didn't make up this math either.
    Surface.blit(text, textcentre)       #Blit text


def picture_button(Surface, image, activeImage, posx, posy, command=None):
    """
    This command is used to create a button that is not just a rectangle
     but based on an image.
     The activeImage variable represents a change in the displayed image when the mouse clicks/ hovers over it.
     posx, posy, width, height and command take the same values as in the other command.
     Very similar code to in the last button has been used, and as such less explanation has been given.
    """
    # Get click and pos:
    mousepos = pg.mouse.get_pos()
    clicked = pg.mouse.get_pressed()

    # In this command, we must compute the width and height of the image manually as we do not know it.
    # In order to do this, I shall use a Rectstyle object.
    imageSize = image.get_rect().size    #Find size of rect

    # Assign these values to the width and height to make the code easier to read.
    width = imageSize[0]
    height = imageSize[1]

    # Compute whether button clicked or hovered over.
    if posx + width > mousepos[0] > posx and posy + height > mousepos[1] > posy:
        # Blit new image
        Surface.blit(activeImage, (posx, posy))
        if clicked[0] == True and command != None:
            command()
            time.sleep(0.1)

    else:
        # If the button is not hovered on:
        # Draw new image
        Surface.blit(image, (posx, posy))
