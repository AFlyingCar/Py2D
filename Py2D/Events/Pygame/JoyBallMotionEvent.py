from Py2D.Events.Pygame.PygameEvent import PygameEvent

class JoyBallMotionEvent(PygameEvent):
    def __init__(self,event):
        PygameEvent.__init__(self,event)
        self.joy = event.joy
        self.ball = event.ball
        self.value = event.value

