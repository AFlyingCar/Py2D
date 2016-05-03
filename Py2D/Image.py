#Image class to work with the Surface manager

import pygame,os
import pygame.transform as t

class Image(object):
    def __init__(self,filename="",surface=None,x=0,y=0):
        self.filename=filename
        self.surf=surface
        if not surface:
            self.loadImage()

        self.pos=[x,y]
        if self.surf != None:
            self.size = self.surf.get_size()
        else:
            self.size = [0,0]
        self.angle = 0.0
        self.do_render = True
    def getDoRender(self):
        return self.do_render
    def setDoRender(self,value):
        self.do_render = value
    def render(self,surf):
        if self.do_render:
            s = t.scale(self.surf,self.size)
            s = t.rotate(s,self.angle)
            surf.blit(s,self.pos)
    def getPosition(self):
        return self.pos
    def getPosX(self):
        return self.pos[0]
    def getPosY(self):
        return self.pos[1]

    def setPos(self,pos):
        self.pos = pos
    def setPosX(self,x):
        self.pos[0] = x
    def setPosY(self,y):
        self.pos[1] = y

    def getSize(self):
        return self.size
    def getAngle(self):
        return self.angle

    def scale(self,size):
        self.size = size
    def resetScale(self):
        self.size = self.surf.get_size()
    def rotate(self,angle):
        self.angle = angle
    def resetRotation(self):
        self.angle=0.0
    def blit(self,surf,pos):
        self.surf.blit(surf,pos)
    def loadImage(self):
        if os.path.exists(self.filename):
            self.surf = pygame.image.load(self.filename)
        else:
            print "Unable to find image: " + self.filename
            # Create a blank purple surface if the image is not found
            self.surf = pygame.Surface((10,10))
            self.surf.fill((255,0,255))
    def getFilename(self):
        return self.filename
    def setFilename(self,filename,reLoad=True):
        self.filename = filename
        if reLoad:
            self.loadImage()
    def save(self,filename=""):
        fname = (filename if filename != "" else self.filename)
        s = t.scale(self.surf,self.size)
        s = t.rotate(s,self.angle)
        pygame.image.save(s,filename)

    def getSurf(self):
        return self.surf

