from Py2D.Events.Pygame.PygameEvent import PygameEvent
import pygame

class QuitEvent(PygameEvent):
    def __init__(self,event):
        PygameEvent.__init__(self,event)


