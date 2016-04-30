import pygame
from EventSubscribe import *
from Events import *

'''

Image     Image
  \        /
  foreground    background
           \      /
            screen

'''

class EventScreenManager(object):
    _instance = None
    def __init__(self):
        self.started = False
        self.screenSize = (0,0)
        self.fps = 0

        self.screen = None
        self.background = None
        self.foreground = None

        self.queue = []
        self.clock = None

    def Init(self):
        pygame.display.init()
        self.screen = pygame.display.set_mode(self.screenSize)
        self.background = pygame.Surface(self.screenSize)
        self.foreground = pygame.Surface(self.screenSize)
        self.clock = pygame.clock.Clock()
        self.started = True

    def isStarted():
        return self.started

    def getQueue(self):
        return self.queue

    def End(self):
        pygame.display.quit()

    def addToQueue(self,renderabl):
        EVENT_BUS.post(SCREEN_MANAGER_ADD_TO_QUEUE_EVENT,renderable=renderabl)

    def removeFromQueue(self,index):
        r = self.queue.pop(index)
        EVENT_BUS.post(SCREEN_MANAGER_RENDERABLE_REMOVED_FROM_QUEUE_EVENT,renderable=r,oldIndex=index)

    def blitSurfaceOnScreen(self,surf,x,y):
        self.screen.blit(surf,(x,y))

    def resetForeground(self):
        self.foreground = pygame.Surface(self.screenSize)

    def setBackground(self,surface):
        self.background = surface

    def getScreenSize(self):
        return self.screenSize

    def setScreenSize(self,width,height):
        self.screenSize = (width,height)

    def getScreenCenter(self):
        return (self.screenSize[0]/2,self.screenSize[1]/2)

    def getFPS(self):
        return self.fps

    def setFPS(self,fps):
        self.fps = fps

    @EventSubscribe(SCREEN_MANAGER_ADD_TO_QUEUE_EVENT)
    def onQueueAdd(self,event):
        self.queue.append(event.renderable)

    @EventSubscribe(TICK_EVENT)
    def onTick(self,event):
        if(self.isStarted()):
            EVENT_BUS.post(PRE_SCREEN_UPDATE_EVENT)
            EVENT_BUS.post(RENDER_QUEUE_EVENT)
            EVENT_BUS.post(SCREEN_UPDATE_EVENT)
            EVENT_BUS.post(POST_SCREEN_UPDATE_EVENT)

    @EventSubscribe(RENDER_QUEUE_EVENT)
    def onRenderQueue(self,event):
        try:
            for s in self.queue:
                # Render each item on the foreground
                s.render(self.foreground)
            return True
        except Exception as e:
            return False

    @EventSubscribe(PRE_SCREEN_UPDATE_EVENT)
    def onPreScreenUpdate(self,event):
        self.resetForeground()

    @EventSubscribe(SCREEN_UPDATE_EVENT)
    def onScreenUpdate(self,event):
        # Render background, then foreground on the surface
        self.blitSurfaceOnScreen(self.background,0,0)
        self.blitSurfaceOnScreen(self.foreground,0,0)

    @EventSubscribe(POST_SCREEN_UPDATE_EVENT)
    def onPostScreenUpdate(self,event):
        self.clock.tick(self.fps)
        pygame.display.update()


    @classmethod
    def getInstance(cls):
        if cls._instance == None:
            cls._instance = EventScreenManager()

        return cls._instance

