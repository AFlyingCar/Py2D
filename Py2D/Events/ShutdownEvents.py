from Py2D.Events.EventBase import EventBase

class PreShutdownEvent(EventBase):
    def __init__(self):
        EventBase.__init__(self)

class ShutdownEvent(EventBase):
    def __init__(self):
        EventBase.__init__(self)

class PostShutdownEvent(EventBase):
    def __init__(self):
        EventBase.__init__(self)
