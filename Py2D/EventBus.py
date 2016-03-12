import pygame
from EventSubscribe import EventSubscribe

class EventBus(object):
    def Update(self):
        for event in pygame.event.get():
            for method in EventSubscribe.subscribes[event.type]:
                method.func(event)

    def post(self,eid,**kwargs):
        event = pygame.event.Event(eid,**kwargs)
        pygame.event.post(event)

