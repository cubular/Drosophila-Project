#!/usr/bin/env python
#Boa:App:BoaApp

from wxPython.wx import *

# Ensuring scipy is imported before Image may avoid mysterious saving errors
import scipy        
import Image

from gui import FlywxFrame

from devices.slide import Slide
from devices.camera import Camera
from devices.mounting import Mount

from threads import CameraThread, EngineThread, MountThread
from shared import Flags, FrameBuffer
import mmode


#~~~~~~~~~~  Initialize shared objects


flag_args = {'CLOSE':       False,
             'ANESTH':      False,
             'DEPOSIT':     False,
             'GAS':         False,
             'SCANNING':    False,
             'VIEW':        False,
             'AUTO':        False,
             'LOAD':        False,
             'DETECT':      False,
             'FIND FLIES':  False,
             'MEASURE FLY': False,
             'SKIP':        False,
             'NEW':         False,
             'ADD':         False,
             'NEXT':        False,
             'STOP':        False,
             'MMODE':       False,
             'MOVIE':       False,
             'SAVE':        False}
flags           =   Flags(flag_args)

device_list = {'CAM'    :   Camera(),
               'SLIDE'  :   Slide(),
               'MOUNT'  :   Mount()}
           
frames          =   FrameBuffer()
mmode_eng       =   mmode.MModeEngine(frames)


#~~~~~~~~~~  Start threads and GUI ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class BoaApp(wxApp):
    def OnInit(self):
        wx.wxInitAllImageHandlers()
        self.main = FlywxFrame.create(None, flags, device_list['SLIDE'])
        self.SetTopWindow(self.main)
        self.main.Show();self.main.Hide();self.main.Show()
        return True
    
    def OnExit(self):
        flags.set('CLOSE')
        flags.reset('FIND FLIES')

gui             =   BoaApp(0)
cam_thread      =   CameraThread(flags, frames, device_list, mmode_eng, gui.main)
mount_thread    =   MountThread(flags, device_list)
engine_thread   =   EngineThread(flags, frames, device_list, mmode_eng, gui.main)
    
engine_thread.start()
cam_thread.start()
mount_thread.start()
#gui.MainLoop()
m = device_list['MOUNT']
s = device_list['SLIDE']
d = engine_thread.detect_algs