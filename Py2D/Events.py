
from pygame.event import Event
from pygame.locals import USEREVENT

##################
# Generic Events #
##################

# No members
SCREEN_UPDATE_EVENT = USEREVENT+1
# 1 member: sound of type Sound
PLAY_SOUND_EVENT = USEREVENT+2
# 2 members: file_or_archive of type int (1 for file, 2 for archive), filename of type str
SND_FILE_LOADED_EVENT = USEREVENT+3
# 1 member: thread of type KillableThread
THREAD_START_EVENT = USEREVENT+4
# 1 member: current tick number
TICK_EVENT = USEREVENT+5

#########################
# Screen Manager Events #
#########################

# 1 member: renderable of type Image
SCREEN_MANAGER_ADD_TO_QUEUE_EVENT = USEREVENT+6
# 2 members: renderable of type Image, oldIndex of type int
SCREEN_MANAGER_RENDERABLE_REMOVED_FROM_QUEUE_EVENT = USEREVENT+7
# No members
PRE_SCREEN_UPDATE_EVENT = USEREVENT+8
# No members
RENDER_QUEUE_EVENT = USEREVENT+9
# No members
POST_SCREEN_UPDATE_EVENT = USEREVENT+10

# A special base event. Should never be thrown. 255 possible events are allowed after USEREVENT
CUSTOM_EVENT = USEREVENT+255

