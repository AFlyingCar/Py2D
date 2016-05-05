import pygame

from Py2D.Managers import ScreenManager

class BaseSprite(pygame.sprite.Sprite):
    def __init__(self,x=0,y=0,z=0,death_lvl=0):
        pygame.sprite.Sprite.__init__(self)
        self.health = 1
        self.death_lvl = death_lvl
        self.position = [x,y,z]
        self.rect = pygame.Rect(1,1,1,1)
        self.surf = pygame.Surface((1,1))
        self.do_render = True

    def setSurf(self,newSurf=None,x=0,y=0):
        if newSurf:
            self.surf = newSurf
        else:
            self.surf = pygame.Surface(x,y)

    def getSurf(self):
        return self.surf

    def setRect(self,newRect=None,left=0,top=0,x=0,y=0):
        if newRect:
            self.rect = newRect
        else:
            self.rect = pygame.Rect(left,top,x,y)

    def getRect(self):
        return self.rect

    def getPosX(self):
        return self.position[0]
    def getPosY(self):
        return self.position[1]
    def getPosZ(self):
        return self.position[2]
    def getPosition(self):
        return self.position

    def setPosX(self,value):
        self.position[0] = value
        self.rect.x = value
    def setPosY(self,value):
        self.position[1] = value
        self.rect.y = value
    def setPosZ(self,value):
        self.position[2] = value
        self.rect.inflate(value,value)
    def setPosition(self,position):
        self.setPosX(position[0])
        self.setPosY(position[1])
        self.setPosZ(position[2])

    def getDeathLevel(self):
        return self.death_lvl

    def getHealth(self):
        return self.health

    def setHealth(self,hp):
        self.health = hp

    def addHealth(self,hp):
        self.health += hp

    def kill(self):
        self.health = self.death_lvl

    def isCollideRect(self,rect):
        return pygame.sprite.collide_rect(self,rect)

    def isCollideGroup(self,group):
        return pygame.sprite.spritecollide(self,group,False)

    def isCollideSprite(self,sprite):
        group = pygame.sprite.Group(sprite)
        return pygame.sprite.spritecollide(self,group,False)

    def isDead(self):
        return self.health <= self.death_lvl

    def updatePosition(self):
        if self.do_render:
            s = ScreenManager.getInstance()
            s.renderToMainSurface(self.surf,(self.position[0],self.position[1]))

    def render(self,surf):
        if self.do_render:
            surf.blit(self.surf,(self.position[:-1]))
    def isDoRender(self):
        return self.do_render

    def setDoRender(self,value):
        self.do_render=value

