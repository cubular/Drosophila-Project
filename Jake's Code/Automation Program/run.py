#!/usr/bin/env python

#Import libraries
import time
#import subprocess
import os
import wx
import scipy        # Ensuring scipy is imported before Image may avoid
                    # saving errors
import Image

###Initialize camera
##curr_dir = os.getcwd()
##os.startfile(curr_dir+"/initcam.bat")
##os.chdir(curr_dir)
##time.sleep(1)

#Import automation code
from gui import FlyGUI

from devices.slide import Slide
from devices.camera import Camera
from devices.mounting import Mount

#from threads import CameraThread, EngineThread, MountThread
from threads import CameraThread, EngineThread, MountThread
from shared import Flags, FrameBuffer
import mmode


#~~~~~~~~~~  Initialize shared objects

flag_args = {'CLOSE':       False,
             'ANESTH':      False,
             'DEPOSIT':     False,
             'GAS':         False,
             'O2':          False,
             'SCANNING':    False,
             'VIEW':        False,
             'AUTO':        False,
             'LOAD':        False,
             'FIND FLIES':  False,
             'MEASURE FLY': False,
             'SKIP':        False,
             'NEW':         False,
             'ADD':         False,
             'STOP':        False,
             'MOVIE':       False,
             'FREEZE':      False}
flags           =   Flags(flag_args)

device_list = {'CAM'    :   Camera(),
               'SLIDE'  :   Slide(),
               'MOUNT'  :   Mount(port=5)}
           
frames          =   FrameBuffer()
mmode_eng       =   mmode.MModeEngine(frames)


#~~~~~~~~~~  Start threads and GUI ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class BoaApp(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        self.main = FlyGUI.create(None, flags, device_list['SLIDE'])
        self.SetTopWindow(self.main)
        self.main.Show();self.main.Hide();self.main.Show()
        return True
    
    def OnExit(self):
        flags.resetAll()
        flags.set('CLOSE')
        time.sleep(1)

def main():
    try:     
        gui             =   BoaApp(0)
        cam_thread      =   CameraThread(flags, frames, device_list, mmode_eng, gui.main)
        mount_thread    =   MountThread(flags, device_list, gui.main)
        engine_thread   =   EngineThread(flags, frames, device_list, mmode_eng, gui.main)
        
        engine_thread.start()
        cam_thread.start()
        mount_thread.start()
        gui.MainLoop()
    except:   
        flags.set('CLOSE')
        mount_thread.mount.close()
        cam_thread.cam.close()
        device_list['SLIDE'].close()  
        time.sleep(.5)

if __name__ == '__main__':
    main()