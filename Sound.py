import pygame.mixer, os

class Sound(object):
	def __init__(self,max_channels,file_obj=None,filename="",channel_num=0):
		if 0 > channel_num > max_channels:
			raise ValueError("channel_num must be greater than 0 and less than %d"%max_channels)

		if filename:
			self.loadFile(filename)
		else:
			if file_obj:
				self.loadObject(file_obj)
			else:
				self.sound = None

		self.channel_num = channel_num
		self.channel = pygame.mixer.Channel(channel_num)
		self.filename = filename

	def play(self):
		if self.sound:
			self.channel.play(self.sound)
			return True
		
		return False

	def stop(self):
		if self.channel.get_busy():
			self.channel.stop()
			return True

		return False

	def loadFile(self,filename):
		if os.path.exists(filename) or isinstance(filename,file):
			self.sound = pygame.mixer.Sound(filename)
			return True

		return False

	def loadObject(self,file_obj):
		self.sound = pygame.mixer.Sound(file_obj)
		return True

	def setChannel(self,channel):
		if 0 < channel < self.max_channels:
			return False

		self.stop()
		self.channel_num = channel

		self.channel = pygame.mixer.Channel(channel)
		return True

	def getChannelNum(self):
		return self.channel_num

	def getChannel(self):
		return self.channel

	def getFileName(self):
		return self.filename

	def isPlaying(self):
		return self.channel.get_busy()

	def setVolume(self,volume):
		self.sound.set_volume(volume)