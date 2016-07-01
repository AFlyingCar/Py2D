from Py2D.Py2D import *
from Py2D.EventBus import *
from Py2D.EventSubscribe import *
from Py2D.Events import *
from Py2D.Events.TickEvent import *
from Py2D.Events.FinishedEvent import *
from Py2D.Events.InitializationEvent import *
from Py2D.Managers.EventScreenManager import *
from Py2D.Managers.Events.InitializeScreenManagerEvent import *

@EventSubscribe(InitializationEvent)
def onInitialization(event):
    print "onInitialization(...)"
    #esm = EventScreenManager.getInstance()
    #EVENT_BUS.post(InitializeScreenManagerEvent())

@EventSubscribe(TickEvent)
def onTick(event):
    if(event.ticks == 60):
        print event.ticks," ticks have passed."
        EVENT_BUS.post(FinishedEvent())

START_PROGRAM()

