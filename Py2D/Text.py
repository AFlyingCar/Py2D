import pygame

if not pygame.font.get_init(): pygame.font.init()

class Text(object):
    def __init__(self,string="",fontname="freesansbold.ttf",color=(0,0,0,255),size=16,x=0,y=0):
        self.string=string
        self.font=None
        self.fontname=fontname
        self.color=color
        self.size=size
        self.pos=[x,y]
        self.surf=None
        self.buildFont()
        self.clearSurf()
        self.buildSurf()

    def render(self,surf):
        surf.blit(self.surf,self.pos)
    def buildFont(self):
        self.font = pygame.font.Font(self.fontname,self.size)

    def buildSurf(self):
        p=[0,0]
        strs=self.string.split("\n")
        #s = self.font.render(self.string,True,self.color)
        for s in strs:
            text=self.font.render(s,True,self.color)
            self.surf.blit(text,p)
            p[1] += text.get_height()+5
        #self.surf.blit(s,(0,0))

    def setString(self,string,reRender=True):
        self.string=string
        if reRender:
            self.clearSurf()
            self.buildSurf()

    def setColor(self,color,reRender=True):
        self.color=color
        if reRender:
            self.clearSurf()
            self.buildSurf()

    def setFont(self,fontname,reRender=True):
        self.fontname=fontname
        self.buildFont()
        if reRender:
            self.clearSurf()
            self.buildSurf()

    def setSize(self,size,reRender=True):
        self.size=size
        self.buildFont()
        if reRender:
            self.clearSurf()
            self.buildSurf()

    def setPosX(self,x):
        self.pos[0]=x
    def setPosY(self,y):
        self.pos[1]=y
    def setPosition(self,position):
        self.pos=position

    def clearSurf(self):
        self.surf=pygame.Surface(self.font.size(self.string),pygame.SRCALPHA,32)

    def getString(self):
        return self.string
    def getColor(self):
        return self.color
    def getFont(self):
        return self.font
    def getFontName(self):
        return self.fontname
    def getSize(self):
        return self.size
    def getPosX(self):
        return self.pos[0]
    def getPosY(self):
        return self.pos[1]
    def getPosition(self):
        return self.pos
    def getSurf(self):
        return self.surf

