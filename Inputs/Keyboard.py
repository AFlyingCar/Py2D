import pygame
from pygame.locals import *

NULLEVENT = 0

class Keyboard(object):
	def __init__(self):
		self.held = []

	def GetRawKey(self,key):
		for event in pygame.event.get():
			if event.type == KEYDOWN or event.type == KEYUP:
				if event.key == key:
					return event

		return pygame.event.Event(NULLEVENT,{})

	def GetHeld(self,key):
		event = self.GetRawKey(key)
		if event.type == KEYDOWN:
			self.held.append(key)
			return True
		elif event.type == KEYUP:
			self.held.remove(key)
			return False

		return key in self.held