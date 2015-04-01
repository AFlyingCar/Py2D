import pygame.mixer, os

class Sound(object):
	def __init__(self,max_channels,file_obj=None,filename="",channel_num=0):
		'''Improved sound object that stores much more information.
		max_channels = Maximum amount of allowed channels.
		file_obj	 = File object to load sound from.
		filename 	 = Name of a file to load a sound from.
		channel_num	 = Channel number.

		channel 	 = Channel to use.'''

		if 0 > channel_num > max_channels:
			raise ValueError("channel_num must be greater than 0 and less than %d"%max_channels)

		self.sound = None #Forward declaration

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
		'''Play the current loaded sound and return True if successful. If no sound is loaded, return False.'''

		if self.sound:
			self.channel.play(self.sound)
			return True
		
		return False

	def isFinished(self):
		'''Return True if the sound has finished playing. False otherwise.'''
		
		return not self.channel.get_busy()

	def stop(self):
		'''Stop playing the sound on the current channel.'''

		if self.channel.get_busy():
			self.channel.stop()
			return True

		return False

	def loadFile(self,filename):
		'''Load a sound from a file.'''

		if os.path.exists(filename) or isinstance(filename,file):
			self.sound = pygame.mixer.Sound(filename)
			return True

		return False

	def loadObject(self,file_obj):
		'''Load a sound object from a file object.'''

		self.sound = pygame.mixer.Sound(file_obj)
		return True

	def setChannel(self,channel):
		'''Set the channel to play sound on. Return False if channel is not legal, True otherwise.'''

		if 0 < channel < self.max_channels:
			return False

		self.stop()
		self.channel_num = channel

		self.channel = pygame.mixer.Channel(channel)
		return True

	def getChannelNum(self):
		'''Return the channel number.'''

		return self.channel_num

	def getChannel(self):
		'''Return the channel.'''

		return self.channel

	def getFileName(self):
		'''Return the filename.'''

		return self.filename

	def isPlaying(self):
		'''Return True if the sound is currently playing, False otherwise.'''

		return self.channel.get_busy()

	def setVolume(self,volume):
		'''Set the volume of the sound.'''

		self.sound.set_volume(volume)

	def setMaxChannelNums(self,channel):
		if channel < 0:
			return False

		self.max_channels = channel
		return True
