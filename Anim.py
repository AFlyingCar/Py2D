import pygame.transform as t

class Anim(object):
	def __init__(self,frames,pos):
		self.frames = frames
		self.currentIndex = 0
		self.pos = pos
		self.playing = False
		if len(self.frames) > 0:
			self.size = self.frames[0].get_size()
		else:
			self.size = (0,0)

		self.angle = 0.0
		self.timesToPlay=0

	def isPlaying(self):
		return self.playing
	def start(self):
		self.playing = True
	def stop(self):
		self.playing = False

	def render(self,surf):
		if self.isPlaying():
			s = t.scale(self.frames[self.currentIndex],self.size)
			s = t.rotate(s,self.angle)
			surf.blit(s,self.pos)
			self.increment()

	def renderUntilFinished(self,surf):
		self.render(surf)
		if self.currentIndex == 0 and self.isPlaying():
			self.stop()

	def increment(self):
		self.currentIndex += 1
		if self.currentIndex >= len(self.frames):
			self.currentIndex = 0

	def decrement(self):
		self.currentIndex -= 1
		if self.currentIndex <= 0:
			self.currentIndex = len(self.frames) - 1

	def getPos(self):
		return self.pos
	def setPos(self,pos):
		self.pos = pos

	def addFrame(self,frame):
		self.frames.append(frame)
	def addFrameList(self,frames):
		self.frames += frames
	def setFrames(self,frames):
		self.frames = frames

	def removeFrame(self,index):
		frame = self.frames[index]
		self.frames.remove(index)
		if index <= self.currentIndex:
			self.decrement()
		return frame

	def scale(self,size):
		self.size = size
	def resetScale(self):
		self.size = self.frames[0].get_size()

	def rotate(self,angle):
		self.angle = angle
	def resetRotation(self):
		self.angle = 0.0
	def setTimesToPlay(self,t):
		self.timesToPlay=t
	def getTimesToPlay(self):
		return self.timesToPlay
