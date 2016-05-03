import os
from datetime import datetime

class Logging(object):
    filename = "C:\\log_output - " + str(datetime.now().year)[2:] + ":" + str(datetime.now().month) + str(datetime.now().day)

    @classmethod
    def set_output_file(cls,filename):
        '''Set the write filename.'''
        Logging.filename = filename
    
    @classmethod
    def log_error(cls,msg,details=[],mode=0):
        '''Logging formatted for error codes.
           msg = message to write
           mode = write mode
                0 - Print to screen.
                1 - Write to file
                2 - Print to screen and write to file.
        '''
        now = datetime.now()
        formatted_msg = " - ERROR]: "
        msg_time = "[" + ":".join([str(now.hour), str(now.minute), str(now.second)])
        formatted_msg = msg_time + formatted_msg + msg

        for d in details:
            formatted_msg += "\n >"
            formatted_msg += d

        Logging.log(formatted_msg,mode)
    
    @classmethod
    def log_warn(cls,msg,details=[],mode=0):
        '''Logging formatted for warning codes.
           msg = message to write
           mode = write mode
                0 - Print to screen.
                1 - Write to file
                2 - Print to screen and write to file.
        '''
        now = datetime.now()
        formatted_msg = " - WARN]: "
        msg_time = "[" + ":".join([str(now.hour), str(now.minute), str(now.second)])
        formatted_msg = msg_time + formatted_msg + msg

        for d in details:
            formatted_msg += "\n >"
            formatted_msg += d

        Logging.log(formatted_msg,mode)

    @classmethod
    def log_test(cls,msg,details=[],mode=0):
        '''Logging formatted for error codes.
           msg = message to write
           mode = write mode
                0 - Print to screen.
                1 - Write to file
                2 - Print to screen and write to file.
        '''
        now = datetime.now()
        formatted_msg = " - TEST]: "
        msg_time = "[" + ":".join([str(now.hour), str(now.minute), str(now.second)])
        formatted_msg = msg_time + formatted_msg + msg

        for d in details:
            formatted_msg += "\n >"
            formatted_msg += d

        Logging.log(formatted_msg,mode)
    
    @classmethod
    def log_stdout(cls,msg,details=[],mode=0):
        '''Logging formatted for error codes.
           msg = message to write
           mode = write mode
                0 - Print to screen.
                1 - Write to file
                2 - Print to screen and write to file.
        '''
        now = datetime.now()
        formatted_msg = " - STDOUT]: "
        msg_time = "[" + ":".join([str(now.hour), str(now.minute), str(now.second)])
        formatted_msg = msg_time + formatted_msg + msg

        for d in details:
            formatted_msg += "\n >"
            formatted_msg += d

        Logging.log(formatted_msg,mode)
    
    @classmethod
    def log(cls,msg,mode):
        '''Log a message.
                msg = message to write
                mode = write mode
                 0 - Print to screen.
                 1 - Write to file.
                 2 - Print to screen and write to file.
        '''

        if mode == 0:
            print msg
            return

        if not os.path.exists(Logging.filename):
            f = open(Logging.filename,'a')
            f.write()
            f.close()

        if mode == 1:
            f = open(Logging.filename,'a')
            f.write(msg)
            f.write("\n")
            f.close()
            return

        if mode == 2:
            print msg
            f = open(Logging.filename,'a')
            f.write(msg)
            f.write("\n")
            f.close()
            return

