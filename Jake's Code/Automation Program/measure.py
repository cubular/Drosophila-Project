import time
import Image, ImageDraw

class Measure:

    def __init__(self, slide, mmode, frames, flags, window):
        self.slide = slide
        self.mmode = mmode
        self.frames = frames
        self.flags = flags
        self.window = window

    def measureBaseline(self,flies,n_mmodes,adjust_time=None):
        if flies is None:  return 0
        start_time = time.clock()
        keep = []
        for fly in flies:   # Record MMode for each fly
            self.flags.reset('SKIP')
            self.mmode.setLine(fly.slope)
            self.slide.move(fly.position)
            
            # Time to allow adjustments
            if adjust_time:
                for j in range(adjust_time): self.acquireMMode(fly,start_time,save=False)  
                if self.flags.get('SKIP'):  return 0
        
            # Acquire normal M-mode
            for j in range(n_mmodes):  self.acquireMMode(fly,start_time,save=True,label='baseline')
            if self.flags.get('SKIP'):
                keep.append(0)
            else:
                keep.append(1)
            heart_frame = self.frames.getFrame()
            frameDraw = ImageDraw.Draw(heart_frame)
            for mask in self.mmode.getDrawMask():
                frameDraw.point(mask,fill=128)  #draws MMode line on frame
            fly.position = self.slide.pos
            fly.heart_frame = heart_frame
            fly.saveMetaData()
            if self.flags.get('SKIP'):  return 0
        new_flies = []
        for i,fly in enumerate(flies):
            if keep[i]:
                new_flies.append(fly)
        flies = new_flies
            
    def measureSequential(self, flies, duration, start_time):
        for fly in flies:    # Record MMode for each fly
            self.flags.reset('SKIP')
            self.mmode.setLine(fly.slope)
            self.slide.move(fly.position)

            # Acquire under hypoxic stress
            ##save_pos = self.slide.pos
            ##self.slide.moveY(-10000)
            ##self.flags.set('GAS')
            ##time.sleep(1)
            ##self.slide.move(save_pos)   
            self.flags.set('GAS')
            for j in range(duration/2):  self.acquireMMode(fly,start_time,label='hypoxia')
            self.flags.reset('GAS')
            if self.flags.get('SKIP'):  return 0
        
            # Get recovery
            # (since mmodes are 2 seconds, duration/8 is one-fourth of the time under hypoxia)
            # (also we want at least 20s recovery)
            for j in range(max([duration/4,10])):  self.acquireMMode(fly,start_time,label='recovery')
            if self.flags.get('SKIP'):  return 0
            # Save heart rate, MMode image, and heart snapshot to file

        return 1

    def measureMultiplex(self, flies, n_mmodes, start_time, measure_time, label):
        if not measure_time:
            measure_time = 600
        while time.clock() - start_time < measure_time:
            keep = []
            for i,fly in enumerate(flies):    # Record MMode for each fly
                self.flags.reset('SKIP')
                self.mmode.setLine(fly.slope)
                self.slide.move(fly.position)
                for j in range(n_mmodes):
                    if j == n_mmodes-1:  self.flags.set('FREEZE')
                    self.acquireMMode(fly,start_time,label=label)
                    self.flags.reset('FREEZE')
                if self.flags.get('SKIP'):  keep.append(0)
                else:  keep.append(1)
                if not fly.heart_frame:
                    fly.heart_frame = self.frames.getFrame()
                    fly.saveMetaData()
                
                fly.position = self.slide.pos
            new_flies = []
            for i,fly in enumerate(flies):
                if keep[i]:
                    new_flies.append(fly)
            flies = new_flies

    def acquireMMode(self, fly, start_time, save=True, label='baseline'):
        if self.flags.get('SKIP'):  
            return 0
        mmodes,duration = self.mmode.record()
        mid = int(self.mmode.n_mmodes/2)
        if self.emptyFrame(mmodes[mid]):
            self.flags.set('SKIP')
            return 0
        rec_time = time.clock()-start_time
        if save:
            fly.addMMode(mmodes,duration,rec_time,save_dir=self.slide.dir,label=label)
        if self.window and not self.flags.get('CLOSE'):  # Check to see window is still there
            # find middle of mmode array
            self.window.displayMMode(mmodes[mid])          # Display in main window
        return 1

    def emptyFrame(self,frame,intens_thresh=250,pix_thresh=.95):
        hist = frame.histogram()
        num_pixels = frame.size[0]*frame.size[1]
        if sum(hist[intens_thresh:]) > pix_thresh*num_pixels:  return True
        else:  return False        