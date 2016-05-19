import Py2D.Events.EventBase import *

class ScreenManagerRemovedFromQueueEvent(EventBase):
    def __init__(self,renderable,oldIndex):
        self.renderable = renderable
        self.oldIndex=oldIndex

