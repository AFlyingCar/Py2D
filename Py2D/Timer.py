import pygame,threading
from pygame.locals import *

class Timer(object):
    def __init__(self,maxTime=-1):
        self.timed=0.0
        self.maxTime=maxTime
        self.timing=False
        self.finished=False
        self.lastTime=0.0
        self.ctime=pygame.time.get_ticks()
        self.time_thread = threading.Thread(target=self._timer)
        self.time_thread.daemon=True
        self.time_thread.start()
    def _timer(self):
        while True:
            self.ctime=pygame.time.get_ticks()
            if self.timing:
                if self.ctime-self.lastTime>=1:
                    self.timed+=1
                    self.lastTime=self.ctime
            if self.maxTime != -1 and self.timed >= self.maxTime:
                self.finished=True

    def startTimer(self,reset=True):
        if reset: self.reset()
        self.timing=True

    def reset(self):
        self.timed=0
        self.timing=False
        self.ctime=pygame.time.get_ticks()

    def stopTimer(self):
        if self.finished:
            self.finished = False

    def setMax(self,newMax):
        '''Set a new maximum time limit.'''
        self.maxTime = newMax

    def getTimePassed(self):
        '''Get how much time has passed. (Used for counting up).'''
        return float(self.timed)

    def getTimeLeft(self):
        '''Get how much time is left. (Used for counting down).'''
        passed = self.maxTime - self.timed
        return float(passed)

    def isFinished(self):
        '''Return whether the timer has finished counting.'''
        return self.finished

    def pauseTimer(self):
        '''Pause the timer temporarily, without resetting it.'''
        self.timing = False
        self.pause = True

    def forceStop(self):
        '''Force the timer to stop if it is currently counting.'''
        if self.timing:
            self.finished = True
            self.reset()

