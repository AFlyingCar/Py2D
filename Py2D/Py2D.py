def START_WITH_ERROR_HANDLING(mclass):
    main_obj = mclass()
    try:
        main_obj.Init()
        main_obj.getScreen().startUpdatePeriodic()
        while True:
            main_obj.Execute()
            main_obj.getEVENT_BUS().Update()
            if main_obj.IsFinished():
                main_obj.getScreen().End()
                main_obj.End()
                return 0
            # main_obj.getScreen().updatePeriodic()
            pygame.event.pump()
    except BaseException as e:
        if not type(e) == SystemExit:
            main_obj.Interrupted(e)
        else:
            print "System Exit called!"

def START_WITHOUT_ERROR_HANDLING(mclass):
    main_obj = mclass()
    main_obj.Init()
    main_obj.getScreen().startUpdatePeriodic()
    while True:
        main_obj.Execute()
        main_obj.getEVENT_BUS().Update()
        if main_obj.IsFinished():
            main_obj.getScreen().End()
            main_obj.End()
            return 0
        # main_obj.getScreen().updatePeriodic()
        pygame.event.pump()

def main(mclass, debug_level=1):
    if debug_level:
        START_WITH_ERROR_HANDLING(mclass)
    else:
        START_WITHOUT_ERROR_HANDLING(mclass)

import pygame,sys
#from pygame.locals import *

import Sprites
import Managers
import Errors
import Inputs

from Events.Events import *
from Events.TickEvent import *
from Events.FinishedEvent import *
from Events.ShutdownEvents import *
from Events.InitializationEvent import *
from EventBus import *
from EventSubscribe import *

import IterativeLoop
import Sound
import Config
import Text
import Timer

def START_PROGRAM():
    tick = 0

    # This is done with the __DONE class so that the done variable can be globally mutated by any of the three following functions
    class __DONE:
        done = False

    # define these functions inside the START_PROGRAM function so they have access to done
    #  and because I don't want others to access them
    @EventSubscribe(FinishedEvent)
    def onFinishedMAIN(event):
        __DONE.done = True
        EVENT_BUS.post(PreShutdownEvent())

    @EventSubscribe(PreShutdownEvent)
    def onPreShutdownMAIN(event):
        EVENT_BUS.post(ShutdownEvent())

    @EventSubscribe(ShutdownEvent)
    def onShutdownMAIN(event):
        EVENT_BUS.post(PostShutdownEvent())

    @EventSubscribe(PostShutdownEvent)
    def onPostShutdownMAIN(event):
        pygame.quit()

    # Init pygame here because the Event system doesn't work otherwise
    pygame.init()

    EVENT_BUS.post(InitializationEvent())
    EVENT_BUS.Update()
    while not __DONE.done:
        tick+=1
        EVENT_BUS.post(TickEvent(tick))
        EVENT_BUS.Update()
    # Call it 2 more times so that Both Shutdown and post shutdown get called
    EVENT_BUS.Update()
    EVENT_BUS.Update()

