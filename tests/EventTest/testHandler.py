from Py2D.Py2D import *
from Py2D.EventSubscribe import *
from Py2D.Events import *

INITIALIZATION_EVENT=CUSTOM_EVENT+1
SHUTDOWN_EVENT = CUSTOM_EVENT+2

class testHandler(object):
    @EventSubscribe(INITIALIZATION_EVENT)
    def onInitialization(self,event):
        print "onInitialization"
    @EventSubscribe(SHUTDOWN_EVENT)
    def onShutdown(self,event):
        print "The system is going down now!"

    @EventSubscribe(TICK_EVENT)
    def onTick(self,event):
        print "We have ticked again."
        if(event.tick >= 5):
            print "Ticked 5 times. We're done here."

