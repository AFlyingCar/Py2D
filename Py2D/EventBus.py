import pygame
from pygame.locals import *
from EventSubscribe import EventSubscribe
from Events.EventBase import EventBase
#from Events.Pygame import *
# Import every pygame event
from Events.Pygame.QuitEvent import QuitEvent 
from Events.Pygame.ActiveEvent import ActiveEvent 
from Events.Pygame.KeyDownEvent import KeyDownEvent 
from Events.Pygame.KeyUpEvent import KeyUpEvent 
from Events.Pygame.MouseMotionEvent import MouseMotionEvent 
from Events.Pygame.MouseButtonUpEvent import MouseButtonUpEvent 
from Events.Pygame.MouseButtonDownEvent import MouseButtonDownEvent 
from Events.Pygame.JoyAxisMotionEvent import JoyAxisMotionEvent 
from Events.Pygame.JoyBallMotionEvent import JoyBallMotionEvent 
from Events.Pygame.JoyHatMotionEvent import JoyHatMotionEvent 
from Events.Pygame.JoyButtonUpEvent import JoyButtonUpEvent 
from Events.Pygame.JoyButtonDownEvent import JoyButtonDownEvent 
from Events.Pygame.VideoResizeEvent import VideoResizeEvent 
from Events.Pygame.VideoExposeEvent import VideoExposeEvent 
from Events.Pygame.PygameUserEvent import PygameUserEvent 

class EventBus(object):
    def __init__(self):
        self.cevents = [] 

    def Update(self):
        # Get the pygame events
        pygame_events = pygame.event.get()
        # I would optimize this, but the truth of the matter is that there are rarely more than 2 or 3 pygame events in the queue at once
        # If I think it is really bad, then I'll probably do something to check if there are even any events in the queue.
        # But for now it is on the bottom of my priority list
        for event in pygame_events:
            self.cevents.append(self.convertPygameEventToClassEvent(event))

        # Add it so that we APPEND the two lists, not overwrite it
        #self.cevents += pygame_events

        for event in self.cevents:
            if(type(event) == pygame.event.Event):
                eid = event.type
            else:
                # Use the type of event.
                # We assume here that the event extends EventBase
                eid = type(event)

            # If the event isn't requested by anything, then skip it
            # We do this because if an unhandled event is posted, then a KeyError is thrown
            if(eid not in EventSubscribe.subscribes):
                continue

            for method in EventSubscribe.subscribes[eid]:
                method.func(event)

            if(type(event) == EventBase):
                event.lifecycle+=1
                if(event.lifecycle > event.MAX_LIFECYCLE):
                    event.canceled = True

                if(event.canceled):
                    self.cevents.remove(event)
            else:
                self.cevents.remove(event)
            # TODO: Do we need an else here? What if they don't put in an EventBase

    def post(self,eid,**kwargs):
        # This weird type-check is here to ensure backwards compatability
        if(type(eid) == int):
            print "Posting old pygame-style event."
            print "Please note that this way is deprecated. Use the new class way instead."
            event = pygame.event.Event(eid,**kwargs)
            pygame.event.post(event)
        else:
            # Hopefully use our own event system
            self.cevents.append(eid)

    def convertPygameEventToClassEvent(self,event):
        if(event.type == QUIT):
            return QuitEvent(event)
        elif(event.type == ACTIVEEVENT):
            return ActiveEvent(event)
        elif(event.type == KEYDOWN):
            return KeyDownEvent(event)
        elif(event.type == KEYUP):
            return KeyUpEvent(event)
        elif(event.type == MOUSEMOTION):
            return MouseMotionEvent(event)
        elif(event.type == MOUSEBUTTONUP):
            return MouseButtonUpEvent(event)
        elif(event.type == MOUSEBUTTONDOWN):
            return MouseButtonDownEvent(event)
        elif(event.type == JOYAXISMOTION):
            return JoyAxisMotionEvent(event)
        elif(event.type == JOYBALLMOTION):
            return JoyBallMotionEvent(event)
        elif(event.type == JOYHATMOTION):
            return JoyHatMotionEvent(event)
        elif(event.type == JOYBUTTONUP):
            return JoyButtonUpEvent(event)
        elif(event.type == JOYBUTTONDOWN):
            return JoyButtonDownEvent(event)
        elif(event.type == VIDEORESIZE):
            return VideoResizeEvent(event)
        elif(event.type == VIDEOEXPOSE):
            return VideoExposeEvent(event)
        elif(event.type == USEREVENT):
            return PygameUserEvent(event)
        else:
            return event.type

EVENT_BUS = EventBus()

