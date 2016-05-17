import pygame

class EventBase(object):
    def __init__(self):
        self.lifecycle = 0
        self.MAX_LIFECYCLE = 10
        self.canceled = False

