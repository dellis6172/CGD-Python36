#Creators: David Ellis and Michael Eichner
#Project: Space Invaders

from pygame import *
from random import shuffle, randrange, choice
from sys import exit as EXIT

pygame.init()

WINDOWWIDTH = 900
WINDOWHEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

PLAYERMOVESPEED = 5
MISSILESPEED = 5
ALIENMOVESPEED = 2


screen = pygame.display.set_mode((WINDOWIDTH, WINDOWHEIGHT))
