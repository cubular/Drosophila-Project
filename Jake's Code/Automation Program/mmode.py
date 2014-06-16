from threading import RLock
import copy, math
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

    def setLine(self,fly_slope=5):
        """Sets slope of M-mode line approximately perpendicular to fly_slope"""
        #find slope of line perpendicular to long axis of fly
        if fly_slope > 2.4:                                 # numbers are calculated to give each direction 
            type = 'horizontal'                             #   equal range around unit circle
        if fly_slope <= 2.4 and fly_slope > .4:            
            type = 'diag-forward'                              
        if fly_slope <= .4 and fly_slope > -.4:             
            type = 'vertical'                                          
        if fly_slope <= -.4 and fly_slope > -2.4:
            type = 'diag-back'
        if fly_slope <= -2.4:
            type = 'horizontal'

        self.mask = self.mask_lib[type]
        self.lock.acquire()
        self.draw_mask = self.draw_mask_lib[type]
        self.lock.release()
        
    def calcMasks(self):
        """ Calculates mask and draw_mask. Draw mask is set one pixel from mask so that they can be
        incorporated in the same image without the M-mode capturing pixels in the drawn line.  Masks
        are applied to image in FlywxFrame.DisplayCam"""

        self.mask_lib = {}                 # mask = pixels to read for M-mode
        self.draw_mask_lib = {}            # draw_mask = pixels to draw M-mode line
        
        x_mid = 320         # coordinates of image center, useful shorthand
        y_mid = 240
        spacing = 20
        
        # vertical line
        self.mask_lib['vertical'] = []
        self.draw_mask_lib['vertical'] = []
        for i in range(self.n_mmodes):
            offset = math.floor(self.n_mmodes/2)*spacing
            step = int(i*spacing)
            # line_mask is vector of x,y coordinates representing M-mode line
            line_mask = [(x_mid-offset+step,y_mid-self.length/2+j) for j in range(self.length)]
            self.mask_lib['vertical'].append(line_mask)
            # draw_mask is same as line_mask but offset by 1 for drawing gray line on image that is not recorded
            draw_mask = [(x_mid-offset+step+1,y_mid-self.length/2+j) for j in range(self.length)]
            self.draw_mask_lib['vertical'].append(draw_mask)
        
        # horizontal line
        self.mask_lib['horizontal'] = []
        self.draw_mask_lib['horizontal'] = []
        for i in range(self.n_mmodes):
            offset = math.floor(self.n_mmodes/2)*spacing
            step = int(i*spacing)
            # line_mask is vector of x,y coordinates representing M-mode line
            line_mask = [(x_mid-self.length/2+j,y_mid-offset+step) for j in range(self.length)]
            self.mask_lib['horizontal'].append(line_mask)
            # draw_mask is same as line_mask but offset by 1 for drawing gray line on image that is not recorded
            draw_mask = [(x_mid-self.length/2+j,y_mid-offset+step+1) for j in range(self.length)]
            self.draw_mask_lib['horizontal'].append(draw_mask)

        # diag line, neg slope
        self.mask_lib['diag-back'] = []
        self.draw_mask_lib['diag-back'] = []
        for i in range(self.n_mmodes):
            offset = math.floor(self.n_mmodes/2)*spacing
            step = int(i*spacing)
            # line_mask is vector of x,y coordinates representing M-mode line
            line_mask = [(x_mid-self.length/2-offset+step+j,y_mid-self.length/2+offset-step+j) for j in range(self.length)]
            self.mask_lib['diag-back'].append(line_mask)
            # draw_mask is same as line_mask but offset by 1 for drawing gray line on image that is not recorded
            draw_mask = [(x_mid-self.length/2-offset+step+j,y_mid-self.length/2+offset-step+j+1) for j in range(self.length)]
            self.draw_mask_lib['diag-back'].append(draw_mask)
            
        # diag line, pos slope
        self.mask_lib['diag-forward'] = []
        self.draw_mask_lib['diag-forward'] = []
        for i in range(self.n_mmodes):
            offset = math.floor(self.n_mmodes/2)*spacing
            step = int(i*spacing)
            # line_mask is vector of x,y coordinates representing M-mode line
            line_mask = [(x_mid-self.length/2-offset+step+j,y_mid+self.length/2-offset+step-j) for j in range(self.length)]
            self.mask_lib['diag-forward'].append(line_mask)
            # draw_mask is same as line_mask but offset by 1 for drawing gray line on image that is not recorded
            draw_mask = [(x_mid-self.length/2-offset+step+j,y_mid+self.length/2-offset+step-j+1) for j in range(self.length)]
            self.draw_mask_lib['diag-forward'].append(draw_mask)

    def getDrawMask(self):
        self.lock.acquire()
        mask = self.draw_mask
        self.lock.release()
        return mask

    def record(self):
        """Record #num_frames M-mode images"""
        start_time = clock()
        frame_list = self.frames.getFrames(num_frames = self.num_frames)
        duration = clock()-start_time
        
        for frame_count,frame in enumerate(frame_list):
            self.process(frame_count,frame)

        mmodes = []        
        for mmode in self.mmode:
            mmodes.append(mmode.copy())
        return mmodes, duration  
                                                                                             
    def process(self,frame_count,frame):
        """Add line from frame to M-mode image. """
        imdata = frame.getdata()      # Add line to image. There should be a better, faster way to do this.
        for i in range(self.n_mmodes):
            line = Image.new("L",(1,self.length))
            # imdata is image data reshaped into vector, so (x,y) is x+y*xsize
            line.putdata([imdata[int(coord[0]+coord[1]*640)] for coord in self.mask[i]])  
            self.mmode[i].paste(line,(frame_count,0,frame_count+1,self.length))
        
    def reset(self):
        """Erase the current M-mode and start over"""
        self.mmode = []
        for i in range(self.n_mmodes):
            self.mmode.append(Image.new("L",(self.num_frames,self.length)))
        self.frame_cnt = 0

