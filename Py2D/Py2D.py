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
from pygame.locals import *

import Sprites
import Managers
import Errors
import Inputs

import Events
import EventBus
import EventSubscribe
import IterativeLoop
import Sound
import Config
import Text
import Timer

def START_PROGRAM():
    tick = 0
    done = False

    @EventSubscribe(FINISHED_EVENT)
    def onFinished(event):
        EVENT_BUS.post(PRE_SHUTDOWN_EVENT)

    # define these functions inside the START_PROGRAM function so they have access to done
    #  and because I don't want others to access them
    @EventSubscribe(PRE_SHUDOWN_EVENT)
    def onPreShutdown(event):
        done = True
        EVENT_BUS.post(SHUTDOWN_EVENT)

    EVENT_BUS.post(INITIALIZATION_EVENT)
    EVENT_BUS.Update()
    while not done:
        tick+=1
        EVENT_BUS.post(TICK_EVENT,ticks=tick)
        EVENT_BUS.Update()
    EVENT_BUS.post(POST_SHUTDOWN_EVENT)
    EVENT_BUS.Update()

