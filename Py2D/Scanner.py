import pygame
from pygame.locals import *

import Text

# IMPORTANT NOTE!
# Scanner(c) uses pygame.event.get() to get input, since Keyboard doesn't use events.
# This can cause a problem with other code that does use events (like checking for Mouse,Joystick,or QUIT calls)
# If you use other code that uses events, make absolutely sure that they are called before Scanner, since when pygame.event.get is called all events in the queue are removed.
# Remember, it's not me, it's pygame

class Scanner():
    # oix_offset: How much to offset the input from the right-most end of the prompt
    def __init__(self,prompt="",fontname="freesansbold.ttf",color=(0,0,0,255),size=16,x=0,y=0,oix_offset=0):
        self.prompt = Text.Text(prompt,fontname,color,size,x,y)
        oix = self.prompt.surf.get_width() + oix_offset # Make sure that the outputted stuff doesn't overlap with the user prompt. 
        self.oinput = Text.Text("",fontname,color,size,oix,y) # So we can display the input

        self.input_string = ""
        self.done = False

    def setPrompt(self,prompt):
        self.prompt.setString(prompt)

    # This method must be called every iteration of your main loop, otherwise it won't be able to recieve any input.
    def Execute(self):
        if not self.done:
            c = ""
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        continue

                    c = event.unicode # Only care about the first character that gets inputted
                    break

            if c == "\n" or c == "\r": # Wait for newline character before we're done (Either \r or \n, idgaf)
                self.done = True
                c=""
            elif c == "\b": # Backtrack backtrack mollify mollify!
                c=""
                self.input_string = self.input_string[:-1]
            elif c == "\t": # Tabs are 4 spaces. Fight me
                c="    "
            # elif pygame.key.get_pressed()[K_LCTRL] and c=='c': # It's a keyboard interrupt. what else were you expecting?
            #     raise KeyboardInterrupt("")

            self.input_string += c
            self.oinput.setString(self.input_string) 

    def render(self,surf):
        self.prompt.render(surf)
        self.oinput.render(surf)

    def getInput(self):
        s=""
        if self.isDone():
            s = self.input_string
            self.input_string = "" # If they want it, then give it to them, but we aren't going to hold onto it anymore. HOT POTATO HOT POTATO
        self.done = False
        return s

    # Cave Johson, signing out
    def isDone(self):
        return self.done

    # Almost all of these methods just calls from either prompt or oinput. They know what's up.
    def setColor(self,color,reRender=True):
        self.prompt.setColor(color,reRender)
        self.oinput.setColor(color,reRender)
    def setFont(self,fontname,reRender=True):
        self.prompt.setFont(fontname,reRender)
        self.oinput.setFont(fontname,reRender)
    def setSize(self,size,reRender=True):
        self.prompt.setSize(size,reRender)
        self.oinput.setSize(size,reRender)

    def setPosX(self,x):
        opx = self.prompt.getPosX()
        self.prompt.setPosX(x)
        self.oinput.setPosX(x+(opx-self.oinput.getPosX())) #Gotta get the offset first
    def setPosY(self,y):
        self.prompt.setPosY(y)
        self.oinput.setPosY(y)
    def setPosition(self,position):
        self.prompt.setPosition(position)
        self.oinput.setPosition(position)

    def getColor(self):
        return self.prompt.getColor()
    def getFont(self):
        return self.prompt.getFont()
    def getFontName(self):
        return self.prompt.getFontName()
    def getSize(self):
        return self.prompt.getSize()
    def getPosX(self):
        return self.prompt.getPosX()
    def getPosY(self):
        return self.prompt.getPosY()
    def getPosition(self):
        return self.prompt.getPosition()
