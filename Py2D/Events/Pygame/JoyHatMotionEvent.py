from Py2D.Events.Pygame.PygameEvent import PygameEvent

class JoyHatMotionEvent(PygameEvent):
    def __init__(self,event):
        PygameEvent.__init__(self,event)
        self.joy = event.joy
        self.hat = event.hat
        self.value = event.value

