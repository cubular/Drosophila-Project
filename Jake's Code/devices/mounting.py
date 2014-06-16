import time
import os
import win32gui
import string
from threading import RLock
import daq

class Mount:
    """ Uses serial DAQ to control the automated anesthesia and mounting system"""
    
    def __init__(self,port=5,lineIO='00001111'):
        self.daq = daq.DAQ(port=port)
        self.lock = RLock()
        self.calibration = None
        self.targetO2 = None
        
##      no longer used, but code can be reused in future
##    def getCount(self):
##        daq_string = self.daq.read()
##        bin_count = string.rstrip(string.replace(daq_string,' ',''))[4:]
##        return 8*int(bin_count[0])+4*int(bin_count[1])+2*int(bin_count[2])+int(bin_count[3])

    def getTargetO2(self):
        self.lock.acquire()
        targetO2 = self.targetO2
        self.lock.release()
        return targetO2

    def setTargetO2(self,targetO2):
        self.lock.acquire()
        self.targetO2 = targetO2
        self.lock.release()
        return
    
    def getO2(self):
        self.lock.acquire()
        if not self.calibration:
            self.calibrate()
        y = self.daq.analogIn(0,'d')
        y0 = self.calibration[0]
        y_atm = self.calibration[1]
        m = (y_atm-y0)/0.2095   # Calibrated at 21%
        x = (y-y0)/m
        self.lock.release()
        return x*100

    def calibrate(self,use_file=True):
        filename = r'./calibration.txt'
        if use_file and os.path.exists(filename):
            f = open(filename)
            lines = f.readlines()
            calibration_strings = string.split(string.strip(lines[1]),'\t')
            self.calibration = map(float,calibration_strings)
        else:
            self.gas(0)
            win32gui.MessageBox(0,'Click OK at atmospheric oxygen, then wait for prompt', 'O2 Sensor Calibration',0)
            time.sleep(12)
            time.sleep(1)
            y_atm = self.daq.analogIn(0,'d')
            self.gas(1)
            win32gui.MessageBox(0,'Click OK at 0% oxygen then wait 10 seconds.','O2 Sensor Calibration',0)
            time.sleep(12)
            self.gas(0)
            time.sleep(0.5)
            y0 = self.daq.analogIn(0,'d')
            
            self.calibration = [y0,y_atm]
            f = open(filename,'w')
            f.write('Voltage at 0% O2\tVoltage at 20.95% O2\n')
            f.write(str(y0)+'\t'+str(y_atm)+'\n')
        f.close()        

    def set(self, line, value, on_time=None):
        """ Output to data acquision card, digital lines 0 to 7.  Value = True to set, False 
            to reset.  If on_time is supplied, line is switched on for that number of seconds
            and value param is ignored"""
        
        self.lock.acquire()
        if on_time:
            self.daq.set(line)
            time.sleep(on_time)
            self.daq.reset(line)
        else:
            if value:
                self.daq.set(line)
            else:
                self.daq.reset(line)
        self.lock.release()

    def o2(self, value, on_time=None):
        self.set(3,value,on_time)

    def gas(self, value, on_time=None):
        self.set(6,value,on_time)
        
    def air(self, value, on_time=None):
        self.set(4,value,on_time)
                
    def anesth(self, value, on_time=None):
        self.set(5,value,on_time)

    def vac(self, value, on_time=None):
        self.set(7,value,on_time)

    def close(self):
        self.daq.close()