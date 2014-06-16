
import serial
class StageDriver:
    def __init__(self,port=timeout=None):
        self.com = serial.Serial(0,timeout = timeout)
        if not self.send('RESET'):
            print "Impossible to open COM5!"
        self.send('SPEED 9')

    def send(self,command):
        if self.com:
            self.com.write(command+'\r')
            r = self.com.readline(eol='\r')
            if r != (':N -1 Unknown Command\r') or (''):
                return True
        return False

    def read(self,command):
        if self.com:
            self.com.write(command+'\r')
            r = self.com.readline(eol='\r')
            if r != (':N -1 Unknown Command\r') or (''):
                return r
        return ''
    
    def reset(self):
        return self.send('ZERO')

    def resetFocus(self):
        return self.send('HERE Z=0')
        
    def moveTo(self, xyz):
        x,y,z = xyz  #unpack three element tuple xyz
        return self.send('M x=%d y=%d z=%d' %(x,y,z))
        
    def displace(self, disp_xyz):
        x,y,z = disp_xyz  #unpack three element tuple disp_xyz
        return self.send('RM x=%d y=%d z=%d' %(x,y,z))

    def where(self):
        r = self.read('WHERE x y z')
        if r != (''):
            r = r.split()[1:]
            where = [int(r[0]), int(r[1]), int(r[2])]
            return where
        else:
            return None
    
    def close(self):
        self.com.close()
        del self.com
        self.com = None
        return True
    