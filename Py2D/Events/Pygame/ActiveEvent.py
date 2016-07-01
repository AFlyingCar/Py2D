from Py2D.Events.Pygame.PygameEvent import PygameEvent

class ActiveEvent(PygameEvent):
    def __init__(self,event):
        PygameEvent.__init__(self,event)
        self.gain = event.gain
        self.state = event.state


