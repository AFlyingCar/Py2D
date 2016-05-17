from Py2D.Events.EventBase import EventBase

class TickEvent(EventBase):
    def __init__(self,ticks):
        EventBase.__init__(self)
        self.ticks = ticks

