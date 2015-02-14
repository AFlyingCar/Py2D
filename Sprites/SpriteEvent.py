import EventBase

class SpriteEvent(EventBase.EventBase):
	def __init__(self,x=0,y=0,z=0):
		EventBase.EventBase.__init__(self,x,y,z)

	def Execute(self,sprite):
		print "Default Execute method. Overload me!"