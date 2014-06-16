from time import time
import scipy
from scipy import linalg
import Image,ImageStat, ImageFilter, ImageOps, ImageChops, ImageDraw
#import Gnuplot
import sys
from fly import Fly

class DetectAlgorithms:
    def __init__(self, slide, frames, flags, window):     
        self.slide = slide
        self.frames = frames
        self.flags = flags
        self.window = window
        self.slide_width = 67700
        self.left_edge = None
        self.g = None
        self.pic_id = 0
        self.mask = self.createMask()

    def calibrate(self,get_width=False, step = 100):        
        f = self.frames.getFrame()
        while not self.emptyFrame(f):
            self.slide.displaceX(step)
            f = self.frames.getFrame()
        self.left_edge = self.slide.pos[0]
        if get_width:
            self.slide.moveX(72000)
            f = self.frames.getFrame()
            while not self.emptyFrame(f):
                self.slide.displaceX(-step)
                f = self.frames.getFrame()
            right_edge = self.slide.pos[0]
            self.slide_width = right_edge-self.left_edge  # usually 67700, assigned in __init__
        self.slide.moveToStart()      
         
    def scan(self,n_rows = 25):
        #start_time = time.clock()
        self.row_height = 750
        x_size,y_size = (40,30)     # size frames are shrunk to
        filter = Image.NEAREST # shrinking filter can also be BILINEAR, BICUBIC, or ANTIALIAS
        skip_rate = 5
        self.rows = []    
        dir = 'RIGHT'
        self.slide_pic = Image.new('L',(x_size,y_size*n_rows),255)
        for i in range(n_rows):
            if dir == 'RIGHT':  position = self.slide_width+5000
            else:               position = 0
            self.frames.fillBuffer()
            self.slide.moveX(position)
            f = self.frames.getBuffer()
            f = [frame.resize((x_size,y_size),filter) for frame in f] 
            #print 'Rate = ',frames.getFrameRate()
            self.slide.displaceY(self.row_height)      
            if dir == 'RIGHT':
                dir = 'LEFT'
            elif dir == 'LEFT':
                f.reverse()
                dir = 'RIGHT'
            while not self.emptyFrame(f[0]):  # trim black frames at edge
                f.pop(0)
            while not self.emptyFrame(f[-1]):
                f.pop(-1)
            sample_indices = [ind*skip_rate for ind in range(len(f)/skip_rate)]
            f = [f[ind] for ind in sample_indices]
            self.rows.append(f)
            x_size,y_size = self.rows[0][0].size
    
            max_frames = max([len(r) for r in self.rows])
            if max_frames*x_size > self.slide_pic.size[0]:
                self.slide_pic = Image.new('L',(x_size*max_frames,y_size*n_rows),255)
            for i,row in enumerate(self.rows):
                for j,frame in enumerate(row):
                    self.slide_pic.paste(frame,(x_size*j,y_size*i))
            self.window.displaySlide(self.slide_pic)
            if self.flags.get('CLOSE'): return                  # good spot to check for closed window
        #self.slide_pic.save(r'c:\\Documents and Settings\\Jake F\\My Documents\\frames\\slide.bmp')
            #print "took ",time.clock()-start_time," seconds"

    def manualAdd(self,flies,auto = False):
        centroid, slope, fly_image = self.trace()
        aligned = self.alignFlyImage(fly_image,slope)
        self.curr_mask = self.rotateMask(self.mask,slope)  #  Create a mask that extracts the center axis of the fly
        if auto:
            self.searchAxis(centroid,slope,rec_time=.5,num_points=3,step=250) #  Find a frame containing the heart
            self.autofocus()
            self.centerMoving(rec_time=1) #  Center on the area of greatest motion
        new_fly = Fly(self.slide.pos,slope)
        new_fly.fly_image = aligned
        flies.append(new_fly)
        return 1

    def findFlies(self,n_rows=25,auto=True):
        self.slide.moveToStart()
        if not self.left_edge: self.calibrate()
        self.flags.set('SCANNING')
        self.scan(n_rows)
        self.locate()
        self.flags.reset('SCANNING')
        if self.flags.get('CLOSE'): return   
        flies = []
        for coord in self.fly_coords:
            self.slide.move(coord)
            self.searchArea()
            try:
                centroid, slope, fly_image = self.trace()              # Trace outline and find centroid of points
                if self.flags.get('SKIP'): raise Exception('Fly skipped')
                aligned = self.alignFlyImage(fly_image,slope)
                if auto:
                    self.curr_mask = self.rotateMask(self.mask,slope)  #  Create a mask that extracts the center axis of the fly
                    self.searchAxis(centroid,slope,rec_time=.5,num_points=3,step=250) #  Find a frame containing the heart
                    if self.flags.get('SKIP'): raise Exception('Fly skipped')
                    self.autofocus()
                    if self.flags.get('SKIP'): raise Exception('Fly skipped')
                    self.centerMoving(rec_time=1) #  Center on the area of greatest motion
                new_fly = Fly(self.slide.pos,slope)
                new_fly.fly_image = aligned
                flies.append(new_fly)
            except Exception,e:
                if self.flags.get('SKIP'):  self.flags.reset('SKIP')
                print 'Error detecting heart:  ',e
##                raise e
        return flies
    
    def searchArea(self):
        coord = self.slide.pos
        if self.emptyFrame(self.frames.getFrame()):
            neighbors = [[coord[0]-1000,coord[1],coord[2]],[coord[0],coord[1]-750,coord[2]], \
                         [coord[0]+1000,coord[1],coord[2]],[coord[0],coord[1]+750,coord[2]]]
            for neighbor in neighbors:
                self.slide.move(neighbor)
                if not self.emptyFrame(self.frames.getFrame()): break
                
    def locate(self):
        buffer_size = 5
        n_frames = scipy.mean([len(row) for row in self.rows])
        
        frame_width = self.slide_width/float(n_frames)
        fly_frames = []
        for i,row in enumerate(self.rows):
            fly_frames.append([])
            for j,frame in enumerate(row):
                if self.emptyFrame(frame): fly_frames[i].append(0)
                else:  fly_frames[i].append(1)

        clusters = []                
        for i,row in enumerate(fly_frames):
            for j,fly_frame in enumerate(row):
                assigned_to_cluster = False
                if fly_frame:
                    for cluster in clusters:
                        cluster_ave = [scipy.mean([coord[0] for coord in cluster]), \
                                       scipy.mean([coord[1] for coord in cluster])]
                        distance = ((cluster_ave[0]-i)**2 + (cluster_ave[1]-j)**2)**(.5)
                        if distance < buffer_size:
                            cluster.append([i,j])
                            assigned_to_cluster= True
                            break
                    if not assigned_to_cluster:  clusters.append([[i,j]])
                    
        # lambda is sorting fn (by x-position)
        clusters.sort(lambda x,y:(y[0][0] -  y[0][1]) - (x[0][0] - x[0][1]))     

        draw = ImageDraw.Draw(self.slide_pic)
        self.fly_coords = []
        for index,cluster in enumerate(clusters):
            coord_ij = [scipy.mean([c[0] for c in cluster]),scipy.mean([c[1] for c in cluster])]
            coord_xyz = [coord_ij[1]*frame_width+self.left_edge, coord_ij[0]*self.row_height,0]
            self.fly_coords.append(coord_xyz)
            #image is scaled down by a factor of 16
            draw.rectangle([coord_xyz[0]/16-50,coord_xyz[1]/16-50,coord_xyz[0]/16+50,coord_xyz[1]/16+50],outline=128)
        self.window.displaySlide(self.slide_pic)
        #self.slide_pic.save(r'c:\temp\pic.bmp')



    def makeFlyImage(self,edge_frames,center_coords):
        frame_size = edge_frames[0].size        
        xmin = min([int(c[0]) for c in center_coords])
        xmax = max([int(c[0]) for c in center_coords])
        ymin = min([int(c[1]) for c in center_coords])
        ymax = max([int(c[1]) for c in center_coords])

        fly_image = Image.new('L',(xmax-xmin+frame_size[0],ymax-ymin+frame_size[1]),255)
        for i,frame in enumerate(edge_frames):
            x,y,z = center_coords[i]
            left_corner = (int(x-xmin),int(y-ymin))
            # to blend:  curr = fly_image.crop(left_corner,etc..)
            #           paste_im = Image.blend(frame, curr)
            fly_image.paste(frame,left_corner)
        #fly_image.save(r'c:\\Documents and Settings\\Jake F\\My Documents\\frames\\fly.bmp')
        return fly_image

    def alignFlyImage(self,fly_image,slope):
        #paste into triple-size image to avoid losing corners in rotation
        deg = scipy.arctan(slope)*180./scipy.pi+90
        x,y = fly_image.size
        large = Image.new("L",(3*x,3*y),255)
        large.paste(fly_image,(x,y))
        #convert slope to angle and rotate to vertical
        aligned = large.rotate(deg)
        cropped = aligned.crop((int(1.2*x),int(.5*y),int(1.8*x),int(2.5*y)))
        bounded = cropped.crop(self.getbbox(cropped))
        self.pic_id += 1
        #bounded.save(r'c:\\Documents and Settings\\Jake F\\My Documents\\frames\\aligned\\'+str(self.pic_id)+r'.bmp')
        self.window.displayEngine2(bounded.resize((80,120)))
        return bounded

    def calcAxis(self,centroid,slope,num_points,step):
        points = []
        for i in range(num_points):
            shift_distance = step*(i-num_points/2)    # so that middle point is centroid
            if shift_distance > 0:
                x = (shift_distance**2/(slope**2+1))**(0.5)     # get coords shift
            else:
                x = -(shift_distance**2/(slope**2+1))**(0.5)
            y = x*slope
            points.append([x+centroid[0],y+centroid[1],0])
        return points

    def searchAxis(self,centroid,slope,num_points=2,step=250,rec_time=0.5):
        """ Move 300-micron steps up and down the axis of the fly from the centroid, looking for motion"""
        points = self.calcAxis(centroid,slope,num_points,step)
        motion = []                         # Detect the absolute amount of motion at each point
        for point in points:                #  to find the frame that contains the heart
            self.slide.move(point)
            m = ImageStat.Stat(self.detectMotion(rec_time=rec_time)).sum[0]
            motion.append(m)
        point = points[scipy.argmax(motion)]# find the point with the most motion
        self.slide.move(point) 
        return point

    def createMask(self,max_distance=200.):
        mask = Image.new('L',(1000,1000))
        d_range = range(501)
        f_table = [int(255.*scipy.exp(-d**2/2./(max_distance/3.)**2)) for d in d_range]
        for y in range(mask.size[1]): #coords of x domain
            distance = abs(500-y)
            f = f_table[distance]
            for x in range(mask.size[0]):
                mask.putpixel((x,y),f)   # mask has gaussian function centered on axis, deemphasizing fly edges
        return mask

    def rotateMask(self,mask,slope):
        size = mask.size
        deg = scipy.arctan(-slope)*180./scipy.pi
        rotated = mask.rotate(deg)
        cropped = rotated.crop((size[0]/2-320,size[1]/2-240,size[0]/2+319,size[1]/2+239))
        return cropped
                                
    def centerMoving(self,rec_time=0.5):
        """Center on the area with the most motion"""
        bbox=None # Bounding box of moving region
        for i in range(5):  # Try 5 times to get a frame with motion in it
            motion = self.detectMotion(rec_time=rec_time)
            #increase threshold until motion is confined to small bounding box
            threshold = 0
            area_thresh = 7500  
            motion = ImageOps.autocontrast(motion) # Scales intensity to 0-255 (max and min possible)
            for j in range(50):
                # Increase threshold, apply threshold and filter
                threshold = 5*j
                thresholded = motion.point(lambda i: 255*(i > threshold))
                if i > 1:  filtered = thresholded
                else: filtered = thresholded.filter(ImageFilter.MinFilter(3))  #filter the first couple times
                self.window.displayEngine3(motion)
                self.window.displayEngine4(filtered)
                # Check size of bounding box.  If small enough, you're done
                bbox = filtered.getbbox()
                if bbox:
                    area = (bbox[3]-bbox[1])*(bbox[2]-bbox[0])
                    if area < area_thresh: break
            if bbox: break
        if not bbox:
            return [0,0] # No luck after 5 tries
        x_offset = -320
        y_offset = -240
        # Move stage to center of bounding box
        x_disp = self.slide.scales['XPIX2MICR']*((bbox[0]+bbox[2])/2.+x_offset) 
        y_disp = self.slide.scales['YPIX2MICR']*((bbox[1]+bbox[3])/2.+y_offset)
        self.slide.displace([x_disp,y_disp,0])
        return [x_disp,y_disp]
            
    def emptyFrame(self,frame,intens_thresh=250,pix_thresh=.95):
        hist = frame.histogram()
        num_pixels = frame.size[0]*frame.size[1]
        if sum(hist[intens_thresh:]) > pix_thresh*num_pixels:  return True
        else:  return False
    
    def trace(self):
        """Traces outline of the fly and calculates centroid and slope"""
        if self.emptyFrame(self.frames.getFrame()): raise Exception('Empty frame')
        fly_image = Image.new('L',(2000,2000),255)
        x0,y0,z0 = self.slide.pos
        last='r'
        move_cnt = 0        
        step = 350
        xscale = self.slide.scales['XPIX2MICR']                       #pixels per stage increment in low magnification
        yscale = self.slide.scales['YPIX2MICR']
        edge_frame = self.frames.getFrame()
        bbox = self.getbbox(edge_frame)      # Bounding box, used to find outline of fly
        coords = []
        edge_frames = []
        center_coords = []
        full_circle = 0
        displace_cnt = 0
        move_out = False
        while not full_circle:
            step_mult = 1
            if bbox == None: free_walls = [1,1,1,1]
            else:free_walls = [bbox[0]>10,bbox[1]>10,bbox[2]<630,bbox[3]<470]# Tells whether bounding box touches edges of frame
                                                                           #  free_walls:   0 = left edge free?
                                                                           #                1 = top edge free?
                                                                           #                2 = right edge free?
                                                                           #                3 = bottom edge free?
            ## Lots of heuristic rules here, they amount to tracing the fly edge clockwise
            if sum(free_walls) == 4:                # lost fly, move back
                move_out = True
                if last =='d':move='u'
                elif last =='u':move='d'
                elif last =='l':move='r'
                elif last =='r':move='l'
            elif free_walls[1] and free_walls[3]:  # free wall on top and bottom - more decisions needed
                if free_walls[0]: move='r'
                elif free_walls[2]: move='l'
                elif last=='d': move='l'
                elif last=='u': move='r'
                else: move = last
                coords.append((self.slide.pos[0],self.slide.pos[1]))
            elif free_walls[0] and free_walls[2]:  # free wall on left and right - more decisions needed
                if free_walls[1]: move='d'
                elif free_walls[3]: move='u'
                elif last=='l': move='d'
                elif last=='r': move='u'
                else: move = last
                coords.append((self.slide.pos[0],self.slide.pos[1]))
            elif free_walls[3] and not free_walls[0]:  #bottom free, left not - move left
                move = 'l'
                x = self.slide.pos[0]
                y = int(self.slide.pos[1]-yscale*(240-bbox[3]))
                coords.append((x,y))
            elif free_walls[1] and not free_walls[2]:   #top free, right not - move right
                move = 'r'
                x = self.slide.pos[0]
                y = int(self.slide.pos[1]-yscale*(240-bbox[1]))
                coords.append((x,y))
            elif free_walls[0] and not free_walls[1]:  #left free, top not - move up
                move = 'u'   
                x = int(self.slide.pos[0]-xscale*(320-bbox[0]))  # get coords at wall edge
                y = self.slide.pos[1]
                coords.append((x,y))
            elif free_walls[2] and not free_walls[3]:   #right free, bottom not - move down
                move = 'd'   
                x = int(self.slide.pos[0]-xscale*(320-bbox[2]))  # get coords at wall edge
                y = self.slide.pos[1]
                coords.append((x,y))
            elif sum(free_walls) == 0:  # in middle of fly - move out (depends on last move)
                move_out = True
                if last=='r': move='u'
                elif last=='u': move='l'
                elif last=='l': move='d'
                elif last=='d': move='r'
            else:
                print "Error tracing fly"
                return self.slide.pos,0  # everything should be covered, but just in case

            x,y,z = self.slide.pos
            center_coords.append([x,y,z])
            edge_frames.append(edge_frame)
            if x < x0 or y < y0: fly_image = Image.new("L",(2000,2000),255)
            if x < x0: x0 = x
            if y < y0: y0 = y
            
            for f,c in zip(edge_frames,center_coords):
                x,y,z = c
                left_corner = (int(x-x0),int(y-y0))
                fly_image.paste(f,left_corner)
            self.window.displayEngine1(fly_image.resize((160,120)))
            
            disp = [0,0,0]
            if move_out:
                disp_step = step/2.
                move_out=False
                move_cnt += 1
                if move_cnt > 15: raise Exception ('Moved out too far')
            else:
                disp_step = step
                last = move
            if move=='r':    disp[0] += disp_step
            elif move=='d':  disp[1] += disp_step
            elif move=='l':  disp[0] -= disp_step
            elif move=='u':  disp[1] -= disp_step
            self.slide.displace(disp)
                
            edge_frame = self.frames.getFrame()
            bbox = self.getbbox(edge_frame)  
            
            # stop loop if new point is close to first 3 or
            # after n iterations
            if len(coords) > 8:
                for i in range(3):
                    distance = ((coords[-1][0]-coords[i][0])**2 + (coords[-1][1]-coords[i][1])**2)**(0.5)
                    if distance < step:
                        full_circle = True
            if len(coords) > 25:
                full_circle = True

        # Calculate centroid, use PCA to get slope of long axis            
        coords = scipy.array(coords)
        centroid = [scipy.mean(coords[:,0]),scipy.mean(coords[:,1]),0]
        detrended = coords.copy() - centroid[0:2]
        U,S,V = linalg.svd(detrended)
        principal = V[0,:]
        slope = principal[1]/float(principal[0])
        axis = self.calcAxis(centroid,slope,1000/step,step)

##        # Plot points, axis        
##        g = Gnuplot.Gnuplot()                              
##        g('set data style points')
##        g('set origin 0,0')
##        g.plot(axis,coords)

        for point in axis:
            self.slide.move([point[0],point[1],0])
            center_coords.append(self.slide.pos)
            edge_frames.append(self.frames.getFrame())            
        for f,c in zip(edge_frames,center_coords):
            x,y,z = c
            left_corner = (int(x-x0),int(y-y0))
            fly_image.paste(f,left_corner)
            self.window.displayEngine1(fly_image.resize((160,120)))
        fly_image = self.makeFlyImage(edge_frames,center_coords)
        
        return centroid, slope, fly_image

    def getbbox(self,frame,threshold=250):
        " Finds the bounding box of the current frame, after applying a filter and threshold"
        
        #filt = ImageFilter.MinFilter(3)  # Helps if sporadic points are making bbox too big
        thresh_frame = frame.point(lambda i: i < threshold) # Threshold before filtering
        #filt_frame = thresh_frame.filter(filt)
        bbox = thresh_frame.getbbox()        
        return bbox

    def detectMotion(self,rec_time=0.5):
        "Accumulates a number of frame-to-frame differences."
        # Gather accumulated frame differences
        frames = self.frames.getFrames(rec_time=rec_time)
        sample_rate = 3
        sample_indices = [ind*sample_rate for ind in range(len(frames)/sample_rate)]
        frames = [frames[ind] for ind in sample_indices]
        #frame.point(lambda i: i*(i<250)+128*(i>250)) #turn bright white to mid-grey to reduce edge effects
        num_frames = len(frames)
        motion = Image.new('L',(640,480))
        scale = num_frames/50.
        for i in range(num_frames-2):
            diff = ImageChops.difference(frames[i+2],frames[i])  # abs of difference
            diff = diff.point(lambda i: int(i/scale)) # dividing by scale prevents saturation
            motion = ImageChops.add(motion,diff)
        motion = ImageChops.multiply(motion,self.curr_mask)   #only look at the middle of the fly
        self.window.displayEngine3(motion)         
        return motion 

    def autofocus(self,step=5000):
        if self.slide.pos[2] >= 0:  step = -step
        self.slide.moveZ(-step/2)
        z_start = self.slide.pos[2]
        self.frames.fillBuffer()
        self.slide.displaceZ(step)
        z_frames = self.frames.getBuffer()

        #sample every kth plus its lth neighbor:  for k=10,l=2 sample frame 0,10,20 and 2,12,22
        k = 10
        l = 2
        sample_ind = [ind*k for ind in range(len(z_frames)/k)]
        sample_ind2 = [ind*k+l for ind in range(len(z_frames)/k)]
        f = [z_frames[ind] for ind in sample_ind]
        f2 = [z_frames[ind] for ind in sample_ind2]
        n = len(f)
        diffs = []
        for i in range(n-2):
            diffs.append(ImageChops.difference(f[i],f2[i]))
        motion = []
        for f in diffs:
            f = ImageChops.multiply(f,self.curr_mask)
            motion.append(ImageStat.Stat(f).sum[0])
        #g = Gnuplot.Gnuplot()
        #g.plot(motion)

        max_frame = scipy.argmax(motion)
        max_focus = (max_frame/float(n))*step + z_start
        self.slide.moveZ(max_focus)
        return max_focus