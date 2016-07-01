from Py2D.Events.Pygame.PygameEvent import PygameEvent

class VideoExposeEvent(PygameEvent):
    def __init__(self,event):
        PygameEvent.__init__(self,event)

