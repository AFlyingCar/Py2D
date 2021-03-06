import sys,trace,threading

class KillableThread(threading.Thread):
    def __init__(self,*args,**kwargs):
        threading.Thread.__init__(self,*args,**kwargs)
        self.killed = False

    def start(self):
        self.__run_backup = self.run
        self.run = self.__run
        threading.Thread.start(self)

    def __run(self):
        sys.settrace(self.globaltrace)
        self.__run_backup()
        self.run = self.__run_backup

    def localtrace(self,frame,why,arg):
        if self.killed:
                if why == 'line':
                        raise SystemExit()
        return self.localtrace

    def globaltrace(self,frame,why,arg):
        if why == 'call':
            return self.localtrace
        else:
            return None

    def kill(self):
        self.killed = True

