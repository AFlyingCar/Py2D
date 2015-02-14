import pygame

import config

settings = config.configReader()[0]

class ScreenManager(object):
	_instance = None
	# def __init__(self,xsize,ysize,xscreensize,yscreensize,campos=[0,0],fps=60):
	# 	self.screen = pygame.display.set_mode((xscreensize,yscreensize))
	# 	self.cameraPosition = campos
	# 	self.fullSurface = pygame.Surface((xsize,ysize))
	# 	self.screensize = [xscreensize,yscreensize] #Size of the viewed surface (what can be seen)
	# 	self.cameraview = pygame.Surface(self.screensize)
	# 	self.fullSurfaceSize = [xsize,ysize] #Size of the entire surface
	# 	self.background = pygame.Surface(self.screensize)
	# 	self.fps = fps
	# 	self.queue = {}
	# 	self.clock = pygame.time.Clock()

	def __init__(self):
		self.Init()

	def Init(self):
		self.screen = pygame.display.set_mode((640,480))
		self.cameraPosition = [0,0]
		self.fullSurface = pygame.Surface((1000,1000))
		self.screensize = [640,480]
		self.cameraview = pygame.Surface(self.screensize)
		self.fullSurfaceSize = [1000,1000]
		self.background = pygame.Surface(self.screensize)
		self.fps = 60
		self.queue = {}
		self.clock = pygame.time.Clock()

	def addToQueue(self,surf,pos):
		self.queue[surf] = pos
		return True

	def renderQueue(self):
		for surf,pos in self.queue:
			self.renderToScreen(surf,pos)

		return True

	def getQueue(self):
		return self.queue

	def updatePeriodic(self):
		self.renderToScreen(self.fullSurface,(0-self.cameraPosition[0],0-self.cameraPosition[1]))
		self.renderQueue()
		self.clock.tick(self.fps)
		pygame.display.update()
		self.resetFullSurface()

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

	def getFPS(self):
		return self.fps

	def setFPS(self, fps):
		self.fps = fps

def getInstance():
	if ScreenManager._instance == None:
		# ScreenManager._instance = ScreenManager(settings["FullSurfaceSizeX"],
		# 						  settings["FullSurfaceSizeY"],
		# 						  settings["ScreenSizeX"],
		# 						  settings["ScreenSizeY"],
		# 						  [settings["CameraPositionX"],
		# 						   settings["CameraPositionY"]
		# 						  ],
		# 						  settings["MaximumFrameRate"])
		ScreenManager._instance = ScreenManager()
	return ScreenManager._instance

def subsurface(surf,topleft,botright):
	'''Get a subsurface of surf.
	surf = 		pygame.Surface
	topleft = 	(x,y)
	topright = 	(x,y)
	'''
	size = (botright[0]-topleft[0],
			botright[1]-topleft[1])
	newSurf = pygame.Surface(size)
	for x in range(topleft[0],botright[0]):
		for y in range(topleft[1],botright[1]):
			color = surf.get_at((x,y))
			newSurf.set_at((x,y),color)

	return newSurf