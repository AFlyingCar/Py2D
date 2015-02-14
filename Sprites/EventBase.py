import BaseSprite

class EventBase(BaseSprite.BaseSprite):
	def __init__(self,x=0,y=0,z=0):
		BaseSprite.BaseSprite.__init__(self,x,y,z)

	def Execute(self):
		print "Default Execute method. Overload me!"

	def Interrupted(self,error):
		print "Default Interrupted method. Overload me!"

	def IsFinished(self):
		print "Default IsFinished method. Overload me!"

	def End(self):
		print "Default End method. Overload me!"