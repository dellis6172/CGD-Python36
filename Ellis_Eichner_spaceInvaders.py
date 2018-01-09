#Creators: David Ellis and Michael Eichner
#Project: Space Invaders


#import pygame --> Importing this way imports pygame all at once via the pygame module.
#                  Meaning you have to type pygame.Whatever.you.want()
from pygame import * # Importing this way imports each module individually. Thus allowing
#                      the programmer to type time.Clock() instead of pygame.time.Clock()
from random import shuffle, randrange, choice
from sys import exit as EXIT

pygame.init()


#------------------------------------------------------------------------------------------
#Constant Variables
WINDOWWIDTH = 900
WINDOWHEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Entity Variables
PLAYERMOVESPEED = 5
MISSILESPEED = 5
ALIENMOVESPEED = 2

'''
Hey, I figured out how to make the barriers and have them disappear after being shot. I'm
gonna put the code in below.
'''
'''
# Create a new sprite for the barrier as a class.
class Barrier(sprite.Sprite):
    def __init__(self, sizex,, sizey color, row, column):
        sprite.Sprite.__init__(self) # Initialize the barrier as a sprite
        self.height = sizey
        self.width = sizex
        self.color = color
        self.image = Surface((self.width, self.height))
        self.image.fill(self.color)
'''
