from Py2D.Events.Pygame.PygameEvent import PygameEvent

class JoyButtonDownEvent(PygameEvent):
    def __init__(self,event):
        PygameEvent.__init__(self,event)
        self.joy = event.joy
        self.button = event.button

