from Py2D.Events.Pygame.PygameEvent import PygameEvent

class VideoResizeEvent(PygameEvent):
    def __init__(self,event):
        PygameEvent.__init__(self,event)
        self.size = event.size
        self.w = event.w
        self.h = event.h

