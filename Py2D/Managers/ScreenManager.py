import pygame,threading

import KillableThread
import Config

def _repeatUpdatePeriodic(self):
        while True:
                self.updatePeriodic()

class ScreenManager(object):
        _instance = None
        def __init__(self):
                # self.Init()
                self.settings = Config.Config()

        def Init(self,filename):
                pygame.display.init()
                # settings = Config.Config("./bin/Py2D/Settings/Window.cfg")
                if(type(filename) == Config.Config):
                    self.settings = filename
                elif(type(filename) == str):
                    self.settings.setFilename(filename)
                else:
                    print "Invalid type. `filename` must be either `str` or `Config`"

                self.screensize =                       self.settings.getOption("ScreenSize")
                self.cameraPosition =           self.settings.getOption("CameraPosition")
                self.fullSurfaceSize =          self.settings.getOption("FullSurfaceSize")
                self.fps =                                      self.settings.getOption("MaximumFrameRate")

                self.screen =           pygame.display.set_mode(self.screensize)
                self.cameraview =       pygame.Surface(self.screensize)
                self.background =       pygame.Surface(self.screensize)
                self.fullSurface =      pygame.Surface(self.fullSurfaceSize)

                # self.queue = {}
                self.queue = []
                self.clock = pygame.time.Clock()

                self.tupdatePeriodic = KillableThread.KillableThread(target=_repeatUpdatePeriodic,args=(self,))
                self.tupdatePeriodic.daemon = True
                # self.tupdatePeriodic.start()

        def canStart(self):
                return self.settings.isReady()

        def End(self):
                self.tupdatePeriodic.kill()
                pygame.display.quit()

        def startUpdatePeriodic(self):
                if self.canStart():
                        self.tupdatePeriodic.start()
                else:
                        raise RuntimeError("Unable to start: No settings file has been established.")

        def addToQueue(self,item):
                '''item can be either a list or an object, so long as the object has a one parameter render method.
                Possibilities: 
                item = [pygame.Surface,(x,y)]
                or
                item = 
                class ClassName:
                        def render(self,surf):
                                pass
                '''
                # self.queue[surf] = pos
                self.queue.append(item)
                return True
        def removeFromQueue(self,index):
                '''Index <- Integer. 0 < index < len(queue)
                Remove an element from the queue and return it.'''
                return self.queue.pop(index)

        # def renderQueue(self):
        #       for surf,pos in self.queue:
        #               self.renderToScreen(surf,pos)

        #       return True

        def renderQueue(self):
                try:
                        for s in self.queue:
                                if type(s) == list:
                                        self.fullSurface.blit(s[0],s[1])
                                else:
                                        s.render(self.fullSurface);
                        return True
                except Exception as e:
                        return False

        def getQueue(self):
                return self.queue

        def updatePeriodic(self):
                self.resetFullSurface()
                self.renderQueue()
                self.renderToScreen(self.fullSurface,(0-self.cameraPosition[0],0-self.cameraPosition[1]))
                self.clock.tick(self.fps)
                pygame.display.update()

        def resetFullSurface(self):
                self.fullSurface = pygame.Surface(self.fullSurfaceSize)

        def CameraSee(self):
                self.cameraview = subsurface(self.fullSurface,self.cameraPosition,self.screensize)

        def renderBKG(self):
                self.renderToScreen(self.background,(0,0))

        def setBKG(self,surf):
                self.background = surf

        def getBKG(self):
                return self.background

        def renderToScreen(self,surf,position):
                self.screen.blit(surf,position)
                pygame.display.update()

        def setCameraPosition(self,x,y):
                self.cameraPosition = [x,y]

        def getCameraPosition(self):
                return self.cameraPosition

        def addCameraPosition(self,x=0,y=0):
                self.cameraPosition = [self.cameraPosition[0]+x,
                                                           self.cameraPosition[1]+y]
        def renderToMainSurface(self,surf,position):
                self.fullSurface.blit(surf,position)

        def getScreenSize(self):
                return self.screensize

        def getFullSurfaceSize(self):
                return self.fullSurfaceSize

        def getScreenCenter(self):
                x = self.screensize[0]/2
                y = self.screensize[1]/2

                return [x,y]

        def getFullSurfaceCener(self):
                x = self.fullSurfaceSize[0]/2
                y = self.fullSurfaceSize[1]/2

                return [x,y]

        def getFPS(self):
                return self.fps

        def setFPS(self, fps):
                self.fps = fps

        @classmethod
        def getInstance(cls):
                if cls._instance == None:
                        cls._instance = ScreenManager()

                return cls._instance

def subsurface(surf,topleft,botright):
        '''Get a subsurface of surf.
        surf =          pygame.Surface
        topleft =       (x,y)
        topright =      (x,y)
        '''
        size = (botright[0]-topleft[0],
                        botright[1]-topleft[1])
        newSurf = pygame.Surface(size)
        for x in range(topleft[0],botright[0]):
                for y in range(topleft[1],botright[1]):
                        color = surf.get_at((x,y))
                        newSurf.set_at((x,y),color)

        return newSurf
