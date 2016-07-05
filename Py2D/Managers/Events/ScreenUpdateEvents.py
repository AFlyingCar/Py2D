from Py2D.Events.EventBase import *

class PreScreenUpdateEvent(EventBase):
    def __init__(self):
        EventBase.__init__(self)
        self.MAX_LIFECYCLE = 0

class ScreenUpdateEvent(EventBase):
    def __init__(self):
        EventBase.__init__(self)
        self.MAX_LIFECYCLE = 0

class PostScreenUpdateEvent(EventBase):
    def __init__(self):
        EventBase.__init__(self)
        self.MAX_LIFECYCLE = 0

