import pygame
from Py2D.EventSubscribe import *
from Py2D.Events.Events import *
from Py2D.Managers.Events import *

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

    def isStarted(self):
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

    @staticmethod
    @EventSubscribe(INITIALIZE_SCREEN_MANAGER_EVENT)
    def onStartScreenManager(event):
        self.Init()

    @staticmethod
    @EventSubscribe(SCREEN_MANAGER_ADD_TO_QUEUE_EVENT)
    def onQueueAdd(event):
        self.queue.append(event.renderable)

    @staticmethod
    @EventSubscribe(TICK_EVENT)
    def onTick(event):
        # NOTE: We have to do this, because otherwise we have trouble with EventBus not calling the method properly (missing self)
        self = EventScreenManager.getInstance()
        if(self.isStarted()):
            EVENT_BUS.post(PRE_SCREEN_UPDATE_EVENT)
            EVENT_BUS.post(RENDER_QUEUE_EVENT)
            EVENT_BUS.post(SCREEN_UPDATE_EVENT)
            EVENT_BUS.post(POST_SCREEN_UPDATE_EVENT)

    @staticmethod
    @EventSubscribe(RENDER_QUEUE_EVENT)
    def onRenderQueue(event):
        try:
            for s in self.queue:
                # Render each item on the foreground
                s.render(self.foreground)
            return True
        except Exception as e:
            return False

    @staticmethod
    @EventSubscribe(PRE_SCREEN_UPDATE_EVENT)
    def onPreScreenUpdate(event):
        self.resetForeground()

    @staticmethod
    @EventSubscribe(SCREEN_UPDATE_EVENT)
    def onScreenUpdate(event):
        # Render background, then foreground on the surface
        self.blitSurfaceOnScreen(self.background,0,0)
        self.blitSurfaceOnScreen(self.foreground,0,0)

    @staticmethod
    @EventSubscribe(POST_SCREEN_UPDATE_EVENT)
    def onPostScreenUpdate(event):
        self.clock.tick(self.fps)
        pygame.display.update()


    @classmethod
    def getInstance(cls):
        if cls._instance == None:
            cls._instance = EventScreenManager()

        return cls._instance

