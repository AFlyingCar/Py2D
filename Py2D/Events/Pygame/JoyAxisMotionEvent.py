from Py2D.Events.Pygame.PygameEvent import PygameEvent

class JoyAxisMotionEvent(PygameEvent):
    def __init__(self,event):
        PygameEvent.__init__(self,event)
        self.joy = event.joy
        self.axis = event.axis
        self.value = event.value

