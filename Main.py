import pygame
from Slide1 import S1
from Slide2 import S2
from Slide3 import S3
from Slide4 import S4
from Slide5 import S5
from Slide6 import S6
from Slide7 import S7
from Slide8 import S8
from Slide9 import S9

#Setup
pygame.init()
screen = pygame.display.set_mode((1000, 700))
WIDTH = screen.get_width()
HEIGHT = screen.get_height()

run = True
clock = pygame.time.Clock()

#Initialization
S1(screen)
S2(screen)
S3(screen)
S4(screen)
S5(screen)
S6(screen)
S7(screen)
S8(screen)
S9(screen)