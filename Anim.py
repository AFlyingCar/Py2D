class Anim(object):
	def __init__(self,frames,pos):
		self.frames = frames
		self.currentIndex = 1
		self.pos = pos
		self.playing = False

	def isPlaying(self):
		return self.playing
	def start(self):
		self.playing = True
	def stop(self):
		self.playing = False

	def render(self,surf):
		if self.isPlaying():
			surf.blit(self.frames[self.currentIndex],self.pos)
			self.increment()

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
