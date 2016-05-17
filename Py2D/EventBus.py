import pygame
from EventSubscribe import EventSubscribe
from Events.EventBase import EventBase

class EventBus(object):
    def __init__(self):
        self.cevents = [] 

    def Update(self):
        # Get the pygame events
        # Add it so that we APPEND the two lists, not overwrite it
        self.cevents += pygame.event.get()

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

EVENT_BUS = EventBus()

