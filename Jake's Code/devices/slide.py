#.\\Program Files\\Python23

from threading import RLock
import copy
import stage

class Slide:
    
    def __init__(self):
        """SlideObj is a higher abstraction of stage movement methods, geared toward a microscope slide with flies."""

        self.scales = { 'XPIX2MICR':          0.97,       # Scale relating pixels to microns on the stage.  Might 
                        'YPIX2MICR':          0.93,       #  need re-calibration from time to time
                        'FOCUS_STEP_COARSE':  500,
                        'FOCUS_STEP_FINE':    100}
        self.move_step = 1000
        
        self.load_pos = [50000,-17000,0]
        self.deposit_pos = [10000,23000,0]
        
        self.stage = stage.StageDriver()  
        self.lock = RLock()
        self.dir = None
        self.flies = []               # List of fly objects
        self.current_fly_num = None     # Number of current fly (index into self.flies)  
        self.num_flies = 0      # Number of flies on the slide (also number to look for in findFlies)
        self._pos = None
        self.reset()

    def getPos(self):
        self.lock.acquire()
        pos = copy.copy(self._pos)
        self.lock.release()
        return pos
    pos = property(getPos)      # Hide real position list obj and only return copies

    def refresh(self):
        self.lock.acquire()
        pos = self.stage.where()
        self._pos = copy.copy(pos)
        self.lock.release()

    def close(self):
        self.moveToStart()
        self.stage.close()

    def reset(self):
        """Reset stage coordinates to 0,"""
        self.stage.reset()
        self.flies = []
        self.current_fly_num = None
        self.num_flies = 0
        self._pos = [0,0,0]      # always keep track of current position with self.pos

    def resetFocus(self):
        self.stage.resetFocus()
        self._pos[2] = 0

    def move(self,pos):
        self.lock.acquire()
        if len(pos) == 2: pos.append(self._pos[2])
        self._pos = copy.copy(pos)
        self.stage.moveTo(self._pos)
        self.lock.release()
        
    def moveX(self,xpos):
        pos = self.pos
        pos[0] = xpos
        self.move(pos)
        
    def moveY(self,ypos):
        pos = self.pos
        pos[1] = ypos
        self.move(pos)

    def moveZ(self,zpos):
        pos = self.pos
        pos[2] = zpos
        self.move(pos)

    def displace(self,disp_pos):        # use stage's moveTo routine, it's faster than displace()
        pos = [pos+displace for pos,displace in zip(self._pos,disp_pos)]
        self.move(pos)

    def displaceX(self,disp_x):
        self.displace([disp_x,0,0])

    def displaceY(self,disp_y):
        self.displace([0,disp_y,0])
        
    def displaceZ(self,disp_z):
        self.displace([0,0,disp_z])

    def moveLeft(self):
        self.displace([-self.move_step,0,0])

    def moveRight(self):
        self.displace([self.move_step,0,0])

    def moveUp(self):
        self.displace([0,-self.move_step,0])

    def moveDown(self):
        self.displace([0,self.move_step,0])

    def moveToStart(self):
        """Move stage and focus back to [0,0,0] coordinates"""
        pos = [0,0,0]
        self.move(pos)

    def loadSlide(self):
        self.move(self.load_pos)

    def deposit(self):
        self.move(self.deposit_pos)
