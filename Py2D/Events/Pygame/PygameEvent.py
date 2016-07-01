from Py2D.Events.EventBase import EventBase
import pygame

class PygameEvent(EventBase):
    def __init__(self,event):
        EventBase.__init__(self)
        # The pygame event
        self.event = event


