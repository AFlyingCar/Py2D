import EventBase
import SpriteEvent

import pygame

class Checkpoint(EventBase.EventBase):
	def __init__(self,x=0,y=0,size=(1,1),event=None,sprite=None,spriteGroup=None):
		EventBase.EventBase.__init__(self,x,y,0)
		self.event = event
		self.sprite = sprite
		self.spriteGroup = pygame.sprite.Group()
		self.setRect(left=x,top=y,x=size[0],y=size[1])
		self.hasBeenExecuted = False

		if spriteGroup:
			for s in spriteGroup.sprites():
				self.spriteGroup.add(s)

		if sprite:
			self.spriteGroup.add(sprite)

		print self.spriteGroup.sprites()
		print self.sprite

	def Execute(self):
		assert isinstance(self.event,SpriteEvent.SpriteEvent)
		if self.isCollideRect(self.sprite):
			self.event.Execute(self.sprite)
			self.hasBeenExecuted = True

	def IsFinished(self):
		return False

	def Interrupted(self,error):
		print "[ERROR]:%s\n",error
		yn = (raw_input("Ignore (y/n): ").lower() == "y")
		if yn:
			return
		else:
			raise error

	def End(self): pass

	def hasExecuted(self):
		return self.hasBeenExecuted