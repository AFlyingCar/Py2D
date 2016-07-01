from Py2D.Events.Pygame.PygameEvent import PygameEvent

class MouseMotionEvent(PygameEvent):
    def __init__(self,event):
        PygameEvent.__init__(self,event)
        self.pos = event.pos
        self.rel = event.rel
        self.buttons = event.buttons

