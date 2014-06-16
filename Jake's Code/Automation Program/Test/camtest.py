from shared import *
from devices.camera import Camera
from threading import Thread
import Image
from devices.slide import Slide
import copy

class CamThread(Thread):
    def __init__(self, frames, cam, flags):
        " Frames grabbed using GetFrame are displayed in hDisplayWindow"
        Thread.__init__(self)
        self.counter = 0
        self.cam    =   cam
        self.frames =   frames
        self.flags = flags
        
    def run(self):
        while not self.flags.get('CLOSE'):
            frame_data = self.cam.getFrameData()
            frame = Image.new("L",(640,480))
            frame.fromstring(frame_data)
            self.frames.putFrame(frame)
        self.cam.close()
        
def emptyFrame(frame,intens_thresh=250,pix_thresh=.95):
        hist = frame.histogram()
        num_pixels = frame.size[0]*frame.size[1]
        if sum(hist[intens_thresh:]) > pix_thresh*num_pixels:  return True
        else:  return False
        
def scan(frames,slide,slide_pic):
        n_rows = 20
        #start_time = time.clock()
        row_height = 750
        x_size,y_size = (40,30)     # size frames are shrunk to
        filter = Image.NEAREST # shrinking filter can also be BILINEAR, BICUBIC, or ANTIALIAS
        skip_rate = 5
        rows = []    
        dir = 'RIGHT'
        slide_pic = Image.new('L',(x_size,y_size*n_rows),255)
        for i in range(n_rows):
            if dir == 'RIGHT':  position = 67700+5000
            else:               position = 0
            frames.fillBuffer()
            slide.moveX(position)
            f = frames.getBuffer()
            #print 'Rate = ',frames.getFrameRate()
            slide.displaceY(row_height) 
            if dir == 'RIGHT':
                dir = 'LEFT'
            elif dir == 'LEFT':
                f.reverse()
                dir = 'RIGHT'
            while not emptyFrame(f[0]):  # trim black frames at edge
                f.pop(0)
            while not emptyFrame(f[-1]):
                f.pop(-1)
            f = [frame.resize((x_size,y_size),filter) for frame in f]      
            sample_indices = [ind*skip_rate for ind in range(len(f)/skip_rate)]
            f = [f[ind] for ind in sample_indices]
            print (f[-1])
            rows.append(f)
            x_size,y_size = rows[0][0].size
    
            max_frames = max([len(r) for r in rows])
            if max_frames*x_size > slide_pic.size[0]:
                slide_pic = Image.new('L',(x_size*max_frames,y_size*n_rows),255)
            for i,row in enumerate(rows):
                for j,frame in enumerate(row):
                    slide_pic.paste(frame,(x_size*j,y_size*i))
            #if.flags.get('CLOSE'): return                  # good spot to check for closed window
        #self.slide_pic.save(r'c:\\Documents and Settings\\Jake F\\My Documents\\frames\\slide.bmp')
            #print "took ",time.clock()-start_time," seconds"
slide_pic = None
cam = Camera()
slide = Slide()
flags = Flags({'CLOSE':False})
frames = FrameBuffer()
ct = CamThread(frames,cam,flags)
ct.start()
#scan(frames,slide,slide_pic)
