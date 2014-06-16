from threading import Thread
import win32gui, winsound
import time, os, string, copy, pickle
import detect, measure
import Image

class MountThread(Thread):
    def __init__(self, flags, device_list, window=None):
        Thread.__init__(self)
        self.flags  =   flags
        self.slide  =   device_list['SLIDE']
        self.mount  =   device_list['MOUNT']
        self.window =   window
        self.begin_anesth = 1
        self.anesth_time = 300
        self.bubble_duration = 3

    def run(self):
        if not self.slide:
            print "No slide loaded"
            return
        while not self.flags.get('CLOSE'):
            time.sleep(.1)
            if self.flags.get('ANESTH'):
                now = time.clock()
                if self.begin_anesth == 1:  #first loop only
                    self.flags.waitOn('SCANNING',False)  # wait for sensitive slide scan to finish first
                    ## Anesthetize with short bursts of air with FlyNap
                    self.window.deposit.Enable(False)
                    self.window.anesth.Enable(False)
                    start_time = now
                    bubble_time = now
                    stop_time = now + self.anesth_time
                    self.mount.anesth(1)
                    self.begin_anesth = 0
                if now >= bubble_time and now < (bubble_time + self.bubble_duration) :
                    self.mount.vac(1)      #pull on anesthesia for 3 seconds
                if now > bubble_time + self.bubble_duration:
                    self.mount.vac(0)
                    bubble_time += 45
                if now > stop_time:
                    self.mount.anesth(0)
                    self.begin_anesth = 1
                    winsound.MessageBeep()
                    self.flags.reset('ANESTH')
                    self.window.deposit.Enable(True)
                    self.window.anesth.Enable(True)
            if self.flags.get('GAS'): self.mount.gas(1)
            else: self.mount.gas(0)
            if self.flags.get('O2'): self.mount.o2(1)
            else: self.mount.o2(0)
            if self.flags.get('DEPOSIT'):
                self.flags.waitOn('LOAD',False)
                self.flags.waitOn('FIND FLIES',False)
                self.deposit()
                self.flags.set('LOAD')
                self.slide.loadSlide()
                self.flags.reset('DEPOSIT')

            O2 = self.mount.getO2()
            targetO2 = self.mount.getTargetO2()
            if self.window:
                self.window.displayO2(O2)
                if targetO2:
                    alert = abs(self.mount.getO2() - targetO2) > 0.3
                    self.window.warnO2(targetO2, alert)

        self.mount.air(0)
        self.mount.anesth(0)
        self.mount.o2(0)
        self.mount.gas(0)
        self.mount.close()
        
    def deposit(self):
        self.slide.deposit()    #move slide in position for deposit

        #self.mount.vac(1,on_time=.25)       
        ## Deposit flies onto slide   
        self.mount.air(1,on_time=1)         
        for i in range(3):                   # push flies out with a short burst of air
            self.slide.displaceX(12000)     # adjust the slide for the next burst
            self.mount.air(1,on_time=1)
                 

    
class CameraThread(Thread):
    def __init__(self, flags, frames, device_list, mmode=None, window=None):
        " Frames grabbed using GetFrame are displayed in hDisplayWindow"
        Thread.__init__(self)
        self.counter = 0
        self.cam    =   device_list['CAM']
        self.frames =   frames
        self.mmode  =   mmode
        self.flags  =   flags
        self.window =   window
        self.displayFrame = Image.new("L",(640,480))

    def run(self):
        while not self.flags.get('CLOSE'):
            frame_data = self.cam.getFrameData()
            self.counter += 1
            if self.counter == 5:
                self.counter = 0
                mask  = self.mmode.getDrawMask()
                self.displayFrame.fromstring(frame_data)
                if self.window: self.window.displayCam(self.displayFrame,mask)
            frame = Image.new("L",(640,480))
            frame.fromstring(frame_data)
            self.frames.putFrame(frame)
        self.cam.close()        
    

class EngineThread(Thread):
    def __init__(self, flags, frames, device_list, mmode, window=None):
        Thread.__init__(self)
        self.save_dir="c:\\Documents and Settings\\Jake\\My Documents\\Data\\M-mode\\Raw\\"
        
        self.slide      =   device_list['SLIDE']
        self.mount      =   device_list['MOUNT']
        self.cam        =   device_list['CAM']
        self.frames     =   frames
        self.mmode      =   mmode
        self.flags      =   flags
        self.window     =   window
        self.detect_algs  = detect.DetectAlgorithms(self.slide, self.frames, self.flags, self.window)
        self.measure    =   measure.Measure(self.slide, self.mmode, self.frames, self.flags, self.window)
        #self.analyze_algs = analyze.AnalyzeAlgorithms(self.window,view=0)
        self.mmode_cnt  =   3
        self.num = 0
        self.testID = 0
        self.flies = None
        self.current_fly = 0
        self.duration = 0
        self.auto = True
##        self.pid = PIDController(20,.5,100)
##        self.o2pulse = Pulse(period=10)
##        self.max_control = 50
##        self.min_control = -50
##        self.ave_control = [0]
        
    def run(self):
        """Loops and performs actions based on Flags, which are activated by FlyGUI buttons"""
        while not self.flags.get('CLOSE') :
            time.sleep(.1)
            
            if self.flags.get('FIND FLIES'):
                if self.flags.get('LOAD'):
                    self.slide.moveToStart()
                    self.flags.reset('LOAD')       
                self.measureFlies()
                self.flags.reset('FIND FLIES')
            if self.flags.get('NEW'):
                self.newSlide()
                self.flags.reset('NEW')
            if self.flags.get('GAS'): self.mount.gas(1)
            else: self.mount.gas(0)
            if self.flags.get('ADD'):
                self.addFly()
                self.flags.reset('ADD')
            if self.flags.get('MEASURE FLY'):
                self.measureFly()
                self.flags.reset('MEASURE FLY')
            if self.flags.get('AUTO'):
                self.flags.set('ANESTH')
                while self.flags.get('AUTO') and not self.flags.get('CLOSE') and not self.flags.get('STOP'):
                    self.flags.waitOn('ANESTH',False)
                    if self.flags.get('STOP') or self.flags.get('CLOSE'): break
                    self.flags.set('DEPOSIT')
                    self.flags.waitOn('DEPOSIT',False)
                    if self.flags.get('STOP') or self.flags.get('CLOSE'): break# check if user exited
                    self.flags.set('SCANNING') # scanning is reset within detect_algs
                    self.flags.set('ANESTH')
                    if self.flags.get('STOP') or self.flags.get('CLOSE'): break
                    self.measureFlies()
                    if self.flags.get('STOP') or self.flags.get('CLOSE'): break
                    self.flags.set('LOAD')
                    self.slide.loadSlide()
                    reply = win32gui.MessageBox(0,'Replace slide and click OK to continue, or Cancel to quit',
                                        'User Checkpoint:  New slide',1)
                    self.slide.moveToStart()
                    self.flags.reset('LOAD')
                    if reply == 2:  break
                self.flags.resetAll()
            if self.flags.get('MOVIE'):
                self.captureMovie()
                self.flags.reset('MOVIE')
        self.slide.close()

    def newSlide(self):
        stock = raw_input("Enter stock ID for new slide")
##        age = raw_input("Enter age of flies (days)")
##        targetO2 = raw_input("Enter target oxygen percentage (number between 0 and 100)")
##        duration = raw_input("Enter hypoxia duration (seconds)")
##        auto = raw_input('Use full automation?')
##        if auto.lower() == 'no' or auto.lower() == 'n': self.auto=False
##        else: self.auto=True
        auto = True
        label = stock
        
        if label not in os.listdir(self.save_dir): os.mkdir(self.save_dir+label)
        n_slides = len(os.listdir(self.save_dir + label))
        slide_dir = self.save_dir+label+'\\slide_'+str(n_slides) + '\\'
        if not os.path.exists(slide_dir):  os.mkdir(slide_dir)
        self.slide.dir = slide_dir

##        try:
##            self.duration = int(duration)
##        except:
        self.duration = 600
##        try:
##            targetO2 = float(targetO2)
##            self.mount.setTargetO2(targetO2)
##        except:
        self.mount.setTargetO2(None)
            
        self.flies = []
        self.current_fly = 0

    def measureFly(self):
        self.flags.reset('GAS')
        if not self.flies:
            return 0
        single_fly = [self.flies[self.current_fly]]
        single_fly[0].position = self.slide.pos
        self.measure.measureBaseline(single_fly,10)
        self.measure.measureSequential(single_fly, self.duration,time.clock())

    def measureFlies(self):
        self.flags.reset('GAS')
        n_mmodes = 2
        measure_time = 10
        reply = win32gui.MessageBox(0,'Start new slide? Click "No" to choose from previous slides.',
                                        'User Checkpoint:  New slide',4)
        if reply == 7: # no, choose from previous
            code_dir = os.getcwd()
            flies_file = str(win32gui.GetOpenFileNameW(
                InitialDir=self.save_dir,
                Filter='Python pickle files\0*.pik\0',
                File='*.pik')[0])
            f = open(flies_file)
            slide_data = pickle.load(f)
            self.flies = slide_data['flies']
            self.duration = slide_data['duration']
            self.slide.dir = slide_data['dir']  #same thing as below?
            f.close()
            os.chdir(code_dir)
            self.slide.dir = os.path.dirname(flies_file)
            # then skip to measuring recovery
            self.measure.measureMultiplex(self.flies,n_mmodes,time.clock(),self.duration,'recovery')
            
        else:
            if not self.flies:
                #if not self.current_fly:  # have flies already been measured?
                self.newSlide()
                self.flies = self.detect_algs.findFlies(15,self.auto)   # Detects flies, focuses, and centers on the heart
            reply = win32gui.MessageBox(0,str(len(self.flies))+' flies found. Click OK to check heart detection',
                    'User Checkpoint:  Refine position',1)
            if reply == 1:  self.refine()
            if not self.flies:  return
            
##                
##            reply = win32gui.MessageBox(0,str(len(self.flies))+' flies saved.  Anesthetize next batch?  If yes, load vial and click OK',
##                    'User Checkpoint:  Anesthetize next batch',1)
##            if reply == 1: self.flags.set('ANESTH')

            self.measure.measureBaseline(self.flies,10)
            
            # Pickle fly object, with a quick fix to avoid a problem with images.
            fly_images = []
            heart_frames = []
            for i,fly in enumerate(self.flies):  
                fly_images.append(fly.fly_image)
                fly.fly_image = None
                heart_frames.append(fly.heart_frame)
                fly.heart_frame = None
            slide_data = {}
            slide_data['flies'] = self.flies
            slide_data['duration'] = self.duration  # another quick fix.  Slide obj should hold this, move Slide methods to Stage
            slide_data['dir'] = self.slide.dir
            f = open(self.slide.dir+'flies_obj.pik','w')
            pickle.dump(slide_data,f)
            f.close()
            
##            reply = win32gui.MessageBox(0,'Measured baseline. Measure hypoxia/recovery now? ',
##                                        'User Checkpoint:  Measure hypoxia',4)
            
            for i,fly_image in enumerate(fly_images):
                self.flies[i].fly_image = fly_image
            for i,heart_frame in enumerate(heart_frames):
                self.flies[i].heart_frame = heart_frame
##            if reply==7: # no don't measure hypoxia now
            
##                return 1 
##            else: # yes measure hypoxia now
##                reply = win32gui.MessageBox(0,'Use multiplex?',
##                                        'User Checkpoint:  Sequential or multiplex',4)
##                if reply == 7:  # no, do sequential
##                    self.measure.measureSequential(self.flies,self.duration,time.clock())
##                    self.slide.moveToStart()
##                    return 1
##                else:  # yes, do multiplex
##                    self.flags.set('GAS')
##                    self.measure.measureMultiplex(self.flies,n_mmodes,time.clock(),self.duration,'hypoxia')
##                    self.flags.reset('GAS')
                    

        self.slide.moveToStart()
        self.flies = []
        return 1
        

    def addFly(self):
        if self.flies == None:  self.newSlide()
        self.slide.refresh()
        ok = self.detect_algs.manualAdd(self.flies,self.auto)
        if ok:
            self.current_fly = len(self.flies)-1
            self.slide.move(self.flies[self.current_fly].position)
            self.mmode.setLine(self.flies[self.current_fly].slope)
            
                    
    def refine(self):
        start_time = time.clock()
        adjust_time = 5
        new_flies = []
        for i,fly in enumerate(self.flies):
            self.flags.reset('SKIP')
            self.current_fly = i
            self.mmode.setLine(fly.slope)
            winsound.MessageBeep()  # lets user know it's time to adjust MMode
            self.slide.move(fly.position)
            self.detect_algs.searchArea()
        
            # time to allow adjustments
            for j in range(adjust_time):
                if j == adjust_time-1:  self.flags.set('FREEZE')
                keep = self.measure.acquireMMode(fly,start_time,save=False)
                self.flags.reset('FREEZE')
            if keep == 1:
                fly.position = self.slide.pos
                new_flies.append(fly)
        self.flies = new_flies
        

def captureMovie(duration,save_dir = None):
    cam = self.device_list['CAM']
    if not save_dir:
        save_dir = raw_input('Input movie directory')
    if not os.path.exists(save_dir): os.mkdir(save_dir)
    if save_dir[-1] != '\\': save_dir = save_dir+'\\'
    cnt = 0
    sample_rate = 60
    num_frames = sample_rate*duration

    frames = []
    start = time.clock()
    last = time.clock()
    for i in range(num_frames):
        frames.append(cam.getFrameImage())
        ## wait for sample time
        now = time.clock()
        while (now - last) < (1./sample_rate):
            now = time.clock()
        last = now

    clocked_time = now - start #- 1./sample_rate

    for i,frame in enumerate(frames):
        if i < 10:
            zeros = '00'
        elif i < 100:
            zeros = '0'
        else:
            zeros = ''
        frame.save(save_dir+'mov'+ zeros + str(i)+'.bmp')
    print 'Movie saved.  Clocked duration = ' + str(clocked_time)        