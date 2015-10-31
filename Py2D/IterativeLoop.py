import pygame

# from Managers import *
from Managers import ScreenManager,InputManager,SoundManager

# print dir(ScreenManager)

class IterativeLoop(object):
	def __init__(self,name="Default Name"):
		self.name = name
		self.screenManager = ScreenManager.ScreenManager.getInstance()
		self.soundManager = SoundManager.SoundManager.getInstance()
		# self.smanager = ScreenManager.getInstance()
		# self.smanager.setCameraPosition(500-320,500-240)
		# self.smanager = ScreenManager.ScreenManager(1000,1000,640,480,campos=[500-320,500-240])

		pygame.display.set_caption(name)

	def Init(self):
		print "Default Init method. Override me!"

	def Execute(self):
		print "Default Execute method. Override me!"

	def IsFinished(self):
		print "Default IsFinished method. Override me!"

	def End(self):
		print "Default End method. Override me!"

	def Interrupted(self,error):
		print "Default Interrupted method. Override me!"

	def getScreen(self):
		return self.screenManager

	def getSound(self):
		return self.soundManager