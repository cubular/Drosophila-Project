import serial

class DAQ:
    """ Controls serial port DAQ card.  The default is to run on COM4, check this first if there are
       problems.  The card has two analog inputs and 8 digital I/O lines.  By default, digital lines
       PA0 through PA3 are configured for input and PA4-7 are for output to the valves.  Use set(line)
       and reset(line) for the digital outputs.  Refer to the DAQ card manual for explanations of the
       commands"""
    
    
    def __init__(self,port=5,lineIO='00000000',eol='\r'):
        self.eol = eol
        self.com = serial.Serial(port)
        self.config(lineIO) #configure (1 for input, 0 for output)
        if self.com.portstr != 'COM1':
            print 'warning, possible error in choosing port'

    def config(self,lineIO):
        self.com.write('CPA'+lineIO+self.eol)

    def analogIn(self,line, mode='d'):
        """Read the analog input, mode='d' for decimal, mode='%' for percent full scale (0-5VDC)"""
        if mode=='d':
            self.com.write('RD'+str(line)+self.eol)
            return float(self.com.readline(eol=self.eol))
        elif mode=='%':
            self.com.write('RA'+str(line)+self.eol)
            return float(self.com.readline(eol=self.eol))
        else:
            raise Exception("mode must be either 'd' or '%' for decimal or percent format")

    def set(self,line='all'):
        if line == 'all':
            self.com.write('SPA11111111'+self.eol)
        else:
            self.com.write('SETPA'+str(line)+self.eol)

    def read(self,line='all'):
        if line == 'all':
            self.com.write('RPA'+self.eol)
        else:
            self.com.write('RPA'+str(line)+self.eol)
        return self.com.readline(eol=self.eol)

    def readDec(self):    
        self.com.write('PA\r')
        return self.com.readline(eol=self.eol)

    def reset(self,line='all'):
        if line == 'all':
            self.com.write('SPA00000000'+self.eol)
        else:
            self.com.write('RESPA'+str(line)+self.eol)

    def close(self):
        self.reset('all')
        self.com.close()