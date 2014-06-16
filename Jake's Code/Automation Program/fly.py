#.\\Program Files\\Pythono2.2.2
#Boa:PyApp:main
import os
from distutils.file_util import copy_file
import string
import Image, ImageDraw
                    
class Fly:
    
    def __init__(self, position=None, slope=None, load_dir=None):
        """ Fly object represents a single fly on the slide with a unique position and orientation"""
        
        self.position = position
        self.slope = slope
        self.heart_frame = None
        self.fly_image = None
        self.save_dir = None
        self.fly_dir = None
        self.durations = []
        self.load_dir = load_dir
        #self.temp_dir = "c:/documents and settings/jake/local settings/temp/mmodes/"
        self.mmode_ind = 0

    def createDir(self,save_dir,n_mmodes):    
        if save_dir[-1] != "\\":  save_dir = save_dir+"\\"
        n_flies = len(os.listdir(save_dir))
        self.fly_dir = save_dir + 'fly_'+str(n_flies) + '\\'
        os.mkdir(self.fly_dir)
        
        self.mmode_dirs = []
        for i in range(n_mmodes):
            mmode_dir = self.fly_dir + 'mmode_' + str(i) + '\\'
            os.mkdir(mmode_dir)
            self.mmode_dirs.append(mmode_dir)
        
        self.mmode_meta = self.fly_dir + 'metadata.txt'
        f = open(self.mmode_meta,'w')
        f.write('M-mode index\ttime\tlabel\tduration\tfilename\n')
        f.close()

    def addMMode(self,mmode,duration,rec_time,save_dir=None,label=''):
        if self.mmode_ind == 0:
            self.createDir(save_dir,len(mmode))
        for i,im in enumerate(mmode):
            im_file = label+ '_mmode' + str(self.mmode_ind)+'.bmp'
            im_path = self.mmode_dirs[i] + im_file
            im.save(im_path)

        f = open(self.mmode_meta,'a')
        f.write('\t'.join([str(self.mmode_ind),str(rec_time),label,str(duration),im_file]) + '\n')
        f.close()
        
        self.mmode_ind += 1

    def saveMetaData(self):
        if self.fly_dir:
            if self.heart_frame:                      
                self.heart_frame.save(self.fly_dir+'heart_frame.bmp')
            if self.fly_image:
                self.fly_image.save(self.fly_dir+'fly.bmp')

    def loadData(self):        
        if self.load_dir:
            if self.load_dir[-1] != '\\':  self.load_dir = self.load_dir + '\\'
            names = os.listdir(self.load_dir)
            if "heart_frame.bmp" in names:
                self.heart_frame = Image.open(self.load_dir+"heart_frame.bmp")
            if "fly.bmp" in names:
                self.fly_image = Image.open(self.load_dir+"fly.bmp")
