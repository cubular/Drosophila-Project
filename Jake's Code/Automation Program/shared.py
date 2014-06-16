from threading import Condition
import Image
import time
import copy

##  This script contains objects shared by the threads.  Currently, only the frame buffer
##  and the global flags are shared.  The objects use condition variables to synchronize
##  and lock when called by threads, so simultaneous access of these objects by the
##  threads should be impossible


#~~~~~~~~~  Storage for global program flags for use in threading ~~~~~~~
#  Usage example
#flag_args = {'CLOSE':       False,
#             'ANESTH':      False,
#             'DEPOSIT':     False,
#             'VIEW':        False,
#             'LOAD':        False,
#             'SKIP':        False,
#             'FREEZE':      False}
#flags           =   Flags(flag_args)

class Flags:
    def __init__(self,flag_dict):
        self.flag_dict = flag_dict
        self.cv = Condition()

    def waitOn(self,label,wait_value=True):
        self.cv.acquire()
        try:
            while self.get(label) != wait_value:
                self.cv.wait()
        finally:
            self.cv.release()
        return True

    def set(self,label):
        self.cv.acquire()
        try:
            self.flag_dict[label] = 1
            self.cv.notifyAll()
        finally:
            self.cv.release()

    def reset(self,label):
        self.cv.acquire()
        try:
            self.flag_dict[label] = 0
            self.cv.notifyAll()
        finally:
            self.cv.release()

    def toggle(self,label):
        self.cv.acquire()
        try:
            self.flag_dict[label] = not self.flag_dict[label]
            self.cv.notifyAll()
        finally:
            self.cv.release()    

    def get(self,label):
        self.cv.acquire()
        value = self.flag_dict[label]
        self.cv.release()
        return value

    def setAll(self):
        for key in self.flag_dict.keys():
            self.set(key)

    def resetAll(self):
        for key in self.flag_dict.keys():
            self.reset(key)

        
#~~~~~~~~~~~~~~~~~~~~ Buffer for threads to store and retrieve frames~~~~~~~~~~~~~~~~~~~~~~        
        
class FrameBuffer:                              
    def __init__(self,calc_rate=True):   
        self.buffer = []
        self.size = 1
        self.__frame = Image.new('L',(640,480))   # hide frame data from direct access.  frame initialized in CamThread
        self.calc_rate = calc_rate
        self.frame_rate = None
        self.frame_count = 0
        self.cv = Condition()
        self.full = False
        self.empty = True

    def getFrameRate(self):
        if self.calc_rate:
            return self.frame_rate
        else:
            print "frame rate not calculated"
        
    def putFrame(self,im):
        if self.calc_rate:
            if self.frame_count == 125:
                record_time = time.clock()-self.start
                self.frame_rate = 125/record_time
                self.frame_count = 0
            if self.frame_count == 0:
                self.start = time.clock()
                
        self.cv.acquire() 
        try:
            self.__frame = im
            self.empty = False
            if self.size != 1:
                if len(self.buffer) < self.size or self.size==0:
                    self.buffer.append(im)
                else:
                    self.full = True
            self.cv.notifyAll()          
        finally:
            self.cv.release()
            if self.calc_rate: self.frame_count += 1

    def getFrame(self):
        self.cv.acquire()
        try:
            while self.empty:
               self.cv.wait()
            return_frame = self.__frame.copy()
        finally:
            self.cv.release()
        return return_frame

    def getFrames(self,rec_time=None,num_frames=None):
        if num_frames:  self.size = num_frames
        elif rec_time and self.calc_rate:  self.size = rec_time*self.getFrameRate()
        else: return []
        self.reset()
        self.cv.acquire()
        try:
            while not self.full:
                self.cv.wait()
            temp_buffer = self.buffer
            self.buffer = []
            self.full = False
            self.size = 1
        finally:
            self.cv.release()
        return temp_buffer

    def fillBuffer(self):
        self.cv.acquire()
        try:
            self.size = 0
            self.reset()
        finally:
            self.cv.release()

    def getBuffer(self):
        self.cv.acquire()
        try:
            temp_buffer = self.buffer
            self.buffer = []
            self.full = False
            self.size = 1
        finally:
            self.cv.release()
        return temp_buffer

    def reset(self):
        self.cv.acquire()
        try:
            self.buffer = []
            self.full = False
        finally:
            self.cv.release()            

            
