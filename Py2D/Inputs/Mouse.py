import pygame
from pygame.locals import *

class Mouse(object):
    def __init__(self):
        self.held = pygame.mouse.get_pressed()

    def GetX(self):
        return GetRawPos()[0]

    def GetY(self):
        return GetRawPos()[1]

    def GetRawPos(self):
        return pygame.mouse.get_pos()

    def GetHeld(self,button):
        return self.held[button]
