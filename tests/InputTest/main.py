from Py2D.Py2D import *
from Py2D.Timer import *
from Py2D.Events.TickEvent import *
from Py2D.Events.FinishedEvent import *
from Py2D.Events.InitializationEvent import *
from Py2D.Events.Pygame.KeyDownEvent import KeyDownEvent
from Py2D.Events.Pygame.QuitEvent import QuitEvent
from Py2D.Events.Pygame.PygameEvent import *
from Py2D.Managers.Events.InitializeScreenManagerEvent import *
from Py2D.Managers.EventScreenManager import *

import inspect

class main(object):
    _timer = None

    #def __init__(self):
        #print EventSubscribe.subscribes
        #print inspect.getargspec(EventSubscribe.subscribes[KeyDownEvent][0].func)

    @staticmethod
    @EventSubscribe(InitializationEvent)
    def onInitialization(event):
        print "onInitialization(...)"
        EVENT_BUS.post(InitializeScreenManagerEvent())
        main._timer = Timer()
        main._timer.startTimer()

    @staticmethod
    @EventSubscribe(QuitEvent)
    def onQuit(event):
        print "Quit button pressed!"
        EVENT_BUS.post(FinishedEvent())
    
    @staticmethod
    @EventSubscribe(KeyDownEvent)
    def onKeyDown(event):
        if(event.key == K_ESCAPE):
            print "Key Escape"
            EVENT_BUS.post(FinishedEvent())

main()

START_PROGRAM()

