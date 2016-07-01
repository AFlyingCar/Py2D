from Py2D.Py2D import *
from Py2D.Timer import *
from Py2D.Events.TickEvent import *
from Py2D.Events.FinishedEvent import *
from Py2D.Events.InitializationEvent import *
from Py2D.Managers.Events.InitializeScreenManagerEvent import *
from Py2D.Managers.EventScreenManager import *

class main(object):
    _timer = None

    @staticmethod
    @EventSubscribe(InitializationEvent)
    def onInitialization(event):
        print "onInitialization(...)"
        EVENT_BUS.post(InitializeScreenManagerEvent())
        main._timer = Timer()
        main._timer.startTimer()

    @staticmethod
    @EventSubscribe(TickEvent)
    def onTick(event):
        if(main._timer.getTimePassed() > 5):
            EVENT_BUS.post(FinishedEvent())

#main()

START_PROGRAM()

