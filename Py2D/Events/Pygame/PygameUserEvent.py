from Py2D.Events.Pygame.PygameEvent import PygameEvent

'''
WARNING! This class is only here for completions sake! DO NOT USE THIS CLASS. Write your own Event class instead
'''

class PygameUserEvent(PygameEvent):
    def __init__(self,event):
        PygameEvent.__init__(self,event)
        self.code = event.code

