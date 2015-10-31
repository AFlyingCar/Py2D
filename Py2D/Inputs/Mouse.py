import pygame
from pygame.locals import *

class Mouse(object):
	def __init__(self):
		self.held = True

	def GetX(self):
		return GetRawPos()[0]

	def GetY(self):
		return GetRawPos()[1]

	def GetRawPos(self):
		return pygame.mouse.get_pos()

	def GetRawButton(self,button):
		for event in pygame.event.get():
			if event.type == MOUSEBUTTONDOWN or event.type == MOUSEBUTTONUP:
				if event.button == button:
					return event

		return pygame.event.Event(0,{})

	def GetHeld(self,button):
		event = self.GetRawButton(button)
		if event.type == MOUSEBUTTONDOWN:
			self.held.append(button)
			return True
		elif event.type == MOUSEBUTTONUP:
			self.held.remove(button)
			return False

		return button in self.held