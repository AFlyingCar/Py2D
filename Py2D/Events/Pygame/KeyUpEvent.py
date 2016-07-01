from Py2D.Events.Pygame.PygameEvent import PygameEvent

class KeyUpEvent(PygameEvent):
    def __init__(self,event):
        PygameEvent.__init__(self,event)
        self.key = event.key
        self.mod = event.mod

