from Py2D.Events.EventBase import *

class ScreenManagerRenderQueueEvent(EventBase):
    def __init__(self):
        EventBase.__init__(self)
        self.MAX_LIFECYCLE = 0

