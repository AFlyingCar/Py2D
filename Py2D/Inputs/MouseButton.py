import Mouse

class MouseButton(object):
	def __init__(self,mouse,button):
		self.mouse = mouse
		self.button = button

	def Get(self):
		return self.mouse.GetHeld(self.button)