def START_WITH_ERROR_HANDLING(mclass):
	main_obj = mclass()
	try:
		main_obj.Init()
		while True:
			main_obj.Execute()
			if main_obj.IsFinished():
				main_obj.End()
				return 0
			# main_obj.getScreen().updatePeriodic()
			pygame.event.pump()
	except BaseException as e:
		if not type(e) != SystemExit:
			main_obj.Interrupted(e)
		else:
			print "System Exit called!"

def START_WITHOUT_ERROR_HANDLING(mclass):
	main_obj = mclass()
	main_obj.Init()
	while True:
		main_obj.Execute()
		if main_obj.IsFinished():
			main_obj.End()
			return 0
		# main_obj.getScreen().updatePeriodic()
		pygame.event.pump()

def main(mclass, debug_level=1):
	if debug_level:
		START_WITH_ERROR_HANDLING(mclass)
	else:
		START_WITHOUT_ERROR_HANDLING(mclass)

import pygame,sys
from pygame.locals import *

import Sprites
import Managers
import Errors
import Inputs

import IterativeLoop
import Sound
import Config
