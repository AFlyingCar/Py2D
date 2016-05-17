import pygame.mixer, StringIO, zipfile

import Py2D.Sound

class SoundManager(object):
    _instance = None
    def __init__(self):
        '''Singleton class, raises a RuntimeError if instantiated.

        num_channels = Number of available channels.
        max_volume   = Maximum volume. Decimal value of 0-1.
        current		 = Current playing sound.
        loaded		 = List of all sounds in memory.
        '''

        if SoundManager._instance != None:
            raise RuntimeError("Cannot have multiple instantiations of singleton class.")

        self.num_channels = 15
        self.max_volume = 1
        self.current = 0
        self.loaded = []

        if not pygame.mixer.get_init():
            pygame.mixer.init()

        pygame.mixer.set_num_channels(self.num_channels)

    def __str__(self):
        x = ""
        for i in self.loaded:
            x += i + ": " + self.loaded.index(i) + "\n"
        return x

    def playAllSoundsAtOnce(self):
        for sound in self.loaded:
            sound.play()

    def isAnySoundPlaying(self):
        playing = True

        for sound in self.loaded:
            playing = playing and sound.isPlaying()

        return playing

    def loadFile(self,filename,archive=None):
        '''Load sound from a file or archive.'''

        s = self.genSndObj(filename,archive)
        self.loaded.append(s)
        return True

    def loadArchive(self,archiveName):
        '''Load all sound files in an archive.'''

        archive = zipfile.ZipFile(archiveName,'r')
        for f in archive.namelist():
            self.loadFile(f,archive)

        return True

    def genSndObj(self,filename,archive=None):
        '''Generate a sound object from either a file or archive.'''

        if archive:
            byte = bytes(archive.read(filename))
            sndfile = StringIO.StringIO(byte)
            s = Sound.Sound( self.num_channels,
                             file_obj=sndfile,
                             channel_num=self.getNotBusyChannel() )
            sndfile.close()
            return s
        else:
            return Sound.Sound( self.num_channels,
                                filename=filename,
                                channel_num=self.getNotBusyChannel() )

    def getNotBusyChannel(self):
        '''Return the channel id for an available sound. If no sounds are available, double the amount of available channels and search again.'''
        for c in range(self.num_channels):
            chan = pygame.mixer.Channel(c)
            if not chan.get_busy():
                return c

        self.setNumChannels(self.num_channels*2)
        return self.getNotBusyChannel()

    def setNumChannels(self,channels):
        '''Set the number of available channels. Return False if the number of channels is less than 0, False otherwise.'''
        if channels < 0:
            return False

        self.num_channels = channels
        pygame.mixer.set_num_channels(channels)

        for i in self.loaded:
            sound.setMaxChannelNums(channels)

        return True

    def setMaxVolume(self,volume):
        '''Set the max volume allowed.'''
        self.max_volume = volume

    def setVolume(self,volume,index=None):
        '''Set the volume of a certain sound. If no index is given, the current sound's volume is set.
        Volume = 0% - 100%'''

        if index==None: index = self.current

        self.loaded[index].setVolume(volume/100)

    def stopAllSound(self):
        '''Stop playing all sounds.'''
        for s in self.loaded:
            s.stop()

        return True

    def unload(self,index):
        '''Unload a sound from memory.'''
        self.loaded.remove(index)
        return True

    def indexOf(self,snd):
        '''Returns the index of a sound object.'''
        return self.loaded.index(snd)

    def getAllSounds(self):
        '''Returns the entire list of sound objects.'''
        return self.loaded

    @classmethod
    def getInstance(cls):
        if cls._instance == None:
            cls._instance = SoundManager()
        return cls._instance

