import pygame

import Anim
import Image

class SpriteSheetAnim(Anim.Anim):
	def __init__(self,filename,pos,spriteSize,spriteStartPos=(0,0)):
		Anim.Anim.__init__(self,[],pos)

		self.filename = filename
		self.spriteSize = spriteSize
		self.spriteStartPos = spriteStartPos
		self.setFrames(self.loadSpriteSheet(filename))
		self.resetScale()

	def getFilename(self):
		return self.filename

	def loadSpriteSheet(self,filename):
		# image = pygame.image.load(filename)
		image = Image.Image(filename)
		
		len_sprt_x,len_sprt_y = self.spriteSize
		sprt_rect_x,sprt_rect_y = self.spriteStartPos

		sheet_rect = image.getSurf().get_rect()
		sheet = []

		for row in range(0,sheet_rect.height-len_sprt_y,self.spriteSize[1]):
			for col in range(0,sheet_rect.width-len_sprt_x,self.spriteSize[0]):
				image.getSurf().set_clip(pygame.Rect(sprt_rect_x,sprt_rect_y,len_sprt_x,len_sprt_y))
				sprite = image.getSurf().subsurface(image.getSurf().get_clip())
				sheet.append(sprite)
				sprt_rect_x += len_sprt_x

			sprt_rect_y += len_sprt_y
			sprt_rect_x = 0

		return sheet
