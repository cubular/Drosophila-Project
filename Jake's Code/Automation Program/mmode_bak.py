from threading import RLock
import copy
import Image
import ImageDraw
from time import clock

class MModeEngine:
    
    def __init__(self, frames, n_mmodes=5, length=160,num_frames = 256):
        """MMode is an object for obtaining and processing M-mode images.  length = length of
            M-mode line in pixels   """
        self.lock = RLock()
        self.frames = frames
        self.n_mmodes = n_mmodes
        self.length = length  # length of M-mode line
        self.num_frames = num_frames  #number of lines (each from a different frame) that comprise an M-mode image
        self.calcMasks()
        self.setLine(0) # start with vertical line (fly_slope = 0)
        self.reset()

    def setLine(self,fly_slope=0):
        """Sets slope of M-mode line approximately perpendicular to fly_slope"""
        #find slope of line perpendicular to long axis of fly
        if fly_slope > 2.4:                                 # numbers are calculated to give each direction 
            type = 2                                        #   equal range around unit circle
        if fly_slope <= 2.4 and fly_slope > .4:             # Type=1: vertical M-mode line
            type = 4                                        # Type=2: horizontal M-mode line
        if fly_slope <= .4 and fly_slope > -.4:             # Type=3: diagonal line w/negative slope
            type = 1                                        # Type=4: diagonal line w/positive slope    
        if fly_slope <= -.4 and fly_slope > -2.4:
            type = 3
        if fly_slope <= -2.4:
            type = 2

        self.mask = self.mask_lib[type-1]
        self.lock.acquire()
        self.draw_mask = self.draw_mask_lib[type-1]
        self.lock.release()
        
    def calcMasks(self):
        """ Calculates mask and draw_mask. Draw mask is set one pixel from mask so that they can be
        incorporated in the same image without the M-mode capturing pixels in the drawn line.  Masks
        are applied to image in FlywxFrame.DisplayCam"""

        self.mask_lib = {}                 # mask = pixels to read for M-mode
        self.draw_mask_lib = {}            # draw_mask = pixels to draw M-mode line
        
        x_mid = 320         # coordinates of image center, useful shorthand
        y_mid = 240
        
        # vert line
        self.mask_lib['vertical'] = []
        for i in range(self.n_mmodes):
            offset = 
            [(x_mid,y_mid-self.length/2+j) for j in range(self.length)]
            self.mask_lib['vertical'].append(mask)
        self.mask_lib.append()
        self.draw_mask_lib.append([(321,240-self.length/2+i) for i in range(self.length)])
        
        # horiz line
        self.mask_lib.append([(320-self.length/2+i,240) for i in range(self.length)])
        self.draw_mask_lib.append([(320-self.length/2+i,241) for i in range(self.length)])

        # diag line, neg slope
        self.mask_lib.append([(320-self.length/2+i,240-self.length/2+i) for i in range(self.length)])
        self.draw_mask_lib.append([(320-self.length/2+i,241-self.length/2+i) for i in range(self.length)])

        # diag line, pos slope        
        self.mask_lib.append([(320-self.length/2+i,240+self.length/2-i) for i in range(self.length)])
        self.draw_mask_lib.append([(320-self.length/2+i,241+self.length/2-i) for i in range(self.length)])

    def getDrawMask(self):
        self.lock.acquire()
        mask = self.draw_mask
        self.lock.release()
        return mask

    def record(self):
        """Record #number M-mode images"""
        start_time = clock()
        frame_list = self.frames.getFrames(num_frames = self.num_frames)
        duration = clock()-start_time
        
        for frame_count,frame in enumerate(frame_list):
            self.process(frame_count,frame)
        return self.mmode.copy(), duration  
                                                                                             
    def process(self,frame_count,frame):
        """Add line from frame to M-mode image. """
        image = frame.getdata()      # Add line to image. There should be a better, faster way to do this. 
        line = Image.new("L",(1,self.length))
        line.putdata([image[coord[0]+coord[1]*640] for coord in self.mask])
        self.mmode.paste(line,(frame_count,0,frame_count+1,self.length))
        
    def reset(self):
        """Erase the current M-mode and start over"""
        self.mmode = Image.new("L",(self.num_frames,self.length))
        self.frame_cnt = 0

