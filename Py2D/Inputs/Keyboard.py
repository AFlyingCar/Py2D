import pygame
from pygame.locals import *

NULLEVENT = pygame.event.Event(0,{})

class Keyboard(object):
    def __init__(self):
        self.held = pygame.key.get_pressed()
        self.timesChecked=[0]*len(self.held)
    def Execute(self):
        self.held=pygame.key.get_pressed()
        for i in range(len(self.held)):
            if self.held[i]:
                if self.timesChecked[i]>=1:
                    self.timesChecked[i]+=1
            else: self.timesChecked[i] = 0

    def GetHeld(self,key):
        return self.held[key]

    def getKeyOnce(self,key):
        if self.timesChecked[key] == 0:
            if self.held[key]:
                self.timesChecked[key]+=1
            return self.held[key]
        else:
            return False

    def getKeyNTimes(self,key,n):
        if self.timesChecked[key] < n:
            return self.held[key]
        else:
            return False

    def getKeyCombination(self,combo):
        for i in combo:
            if not self.GetHeld(i):
                return False
        return True

