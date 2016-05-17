from Py2D.Events.EventBase import *

class ScreenManagerAddToQueueEvent(EventBase):
    def __init__(self,renderable):
        EventBase.__init__(self)
        self.renderable = renderable

