from Py2D.Events.Pygame.PygameEvent import PygameEvent

class KeyDownEvent(PygameEvent):
    def __init__(self,event):
        PygameEvent.__init__(self,event)
        self.unicode = event.unicode
        self.key = event.key
        self.mod = event.mod

