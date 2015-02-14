import pygame.mixer, StringIO, zipfile

import Sound

class SoundManager(object):
	_instance = None
	def __init__(self):
		if SoundManager._instance != None:
			raise RuntimeError("Cannot have multiple instantiations of singleton class.")

		self.num_channels = 15
		self.max_volume = 1
		self.current = 0
		self.loaded = []

		pygame.mixer.set_num_channels(num_channels)

	def __str__(self):
		x = ""
		for i in self.loaded:
			x += i + ": " + self.loaded.index(i) + "\n"
		return x

	def loadFile(self,filename,archive=None):
		s = self.genSndObj(filename,archive)
		self.loaded.append(s)
		return True

	def loadArchive(self,archiveName):
		archive = zipfile.ZipFile(archiveName,'r')
		for f in archive.namelist():
			self.loadFile(f,archive)

		return True

	def genSndObj(self,filename,archive=None):
		if archive:
			byte = bytes(archive.read(filename))
			sndfile = StringIO.StringIO(byte)
			s = Sound.Sound(self.num_channels,
							file_obj=sndfile,
							channel_num=self.getNotBusyChannel() )
			sndfile.close()
			return s

		else:
			return Sound.Sound( self.num_channels,
								filename=filename,
								channel_num=self.getNotBusyChannel() )

	def getNotBusyChannel(self):
		for c in range(self.num_channels):
			chan = pygame.mixer.Channel(c)
			if not chan.get_busy():
				return c

		# If not enough channels are available, double the amount of available channels
		self.setNumChannels(self.num_channels*2)

		return self.getNotBusyChannel()

	def setNumChannels(self,channels):
		self.num_channels = channels
		pygame.mixer.set_num_channels(channels)

	def setMaxVolume(self,volume):
		self.max_volume = volume

	def setVolume(self,volume,index=None):
		'''Volume = 0% - 100%'''
		if index==None: index = self.current

		self.loaded[index].setVolume(volume/100)

	def stopAllSound(self):
		for s in self.loaded:
			s.stop()

		return True

	def unload(self,index):
		self.loaded.remove(index)
		return True

	def indexOf(self,snd):
		return self.loaded.index(snd)

	def getAllSounds(self):
		return self.loaded

	# def __new__(cls,*args,**kwargs):
	# 	if not cls._instance:
	# 		cls._instance = super(SoundManager,cls).__new__(cls,*args,**kwargs)
	# 	return cls._instance

	@classmethod
	def getInstance(cls):
		if cls._instance == None:
			cls._instance = SoundManager()
		return cls._instance