import pygame

class KeyboardButton(object):
	def __init__(self,button):
		self.button = button

	def Get(self):
		return pygame.key.get_pressed()[self.button]

	def GetButton(self):
		return self.button