
class EventSubscribe(object):
    subscribes = {}
    def __init__(self,event_type):
        self.event_type = event_type
        self.func = None
        # Create a new list if event_type has not been registered before
        if(event_type not in EventSubscribe.subscribes):
            EventSubscribe.subscribes[event_type] = []
        EventSubscribe.subscribes[event_type].append(self)
    def __call__(self,f):
        def wrapped(*args):
            return f(*args)
        self.func = wrapped
        return wrapped

# @EventSubscribe(/*Event Type*/)
# def onEvent(event):
#     do stuff


# EventBus.Update():
#     for(event in pygame.event.get()):
#         for(EventSubscribe.subscribes[type(event)]):
#             EventSubscribe.subscribes[type(event)].func(event)
#

