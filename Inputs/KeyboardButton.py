import Keyboard

class KeyboardButton(object):
	def __init__(self,keyboard,button):
		self.keyboard = keyboard
		self.button = button

	def Get(self):
		return self.keyboard.GetHeld(self.button)