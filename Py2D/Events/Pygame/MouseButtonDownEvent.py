from Py2D.Events.Pygame.PygameEvent import PygameEvent

class MouseButtonDownEvent(PygameEvent):
    def __init__(self,event):
        PygameEvent.__init__(self,event)
        self.pos = event.pos
        self.button = event.button

