
from pygame.event import Event
from pygame.locals import USEREVENT

# No members
SCREEN_UPDATE_EVENT = USEREVENT+1
# 1 member: sound of type Sound
PLAY_SOUND_EVENT = USEREVENT+2
# 2 members: file_or_archive of type int (1 for file, 2 for archive), filename of type str
SND_FILE_LOADED_EVENT = USEREVENT+3
# 1 member: thread of type KillableThread
THREAD_START_EVENT = USEREVENT+4

