#Initialize Camera
print "Initializing Camera..."
import MMCorePy
from pylab import *
mmc = MMCorePy.CMMCore()

mmc.loadDevice("cam","HamamatsuHam","HamamatsuHam_DCAM")
mmc.initializeDevice("cam")
mmc.setCameraDevice("cam")
print "Camera initialization successful!"

# Image Processing
import matplotlib.pyplot as plt

import serial
import time

# Camera viewing length and height
incrementX = '36000'
incrementY = '30000'


rowSize = 14
numberOfRows = 14

class StageDriver:

# Initiate driver
    def __init__(self):
        print "Initializing Stage..."
        self.ser = serial.Serial(
            port = 'COM1',
            baudrate = 9600,
            parity = serial.PARITY_NONE,
            stopbits = serial.STOPBITS_ONE,
            bytesize = serial.EIGHTBITS,
            rtscts = True,
        )
        self.send('SPEED 9')
        self.pictureNumber = 0
        self.ser.isOpen()
        print "Stage initialization successful!"

    # Position of X
    def whereX(self):
        self.send('WHERE X')
        out = ''
        time.sleep(1)
        while self.ser.inWaiting() > 0:
            out += self.ser.read(1)
        out = out[-8:-2]
        return out
    
    def whereY(self):
        self.send('WHERE Y')
        out = ''
        time.sleep(1)
        while self.ser.inWaiting() > 0:
            out += self.ser.read(1)
        out = out[-8:-2]
        return out

    def snapImage(self):
        mmc.snapImage()
        im1 = mmc.getImage()
        fig = plt.imshow(im1, cmap = cm.gray)
        plt.axis('off')
        self.pictureNumber+=1
        plt.savefig("Pieces\piece%d.png" % self.pictureNumber, bbox_inches = 'tight')

    def moveRightRow(self, count):
        self.moveRight(count)
        time.sleep(1)
        return True

    def moveLeftRow(self, count):
        self.moveLeft(count)
        time.sleep(1)
        return True

    def moveRight(self, count):
        for i in range(1,count+1):
            self.send('RELMOVE X=-' + incrementX)
            time.sleep(0.5)
            self.snapImage()
        return True
    
    def moveLeft(self, count):
        for i in range(1,count):
            self.send('RELMOVE X=' + incrementX)
            time.sleep(0.5)
            self.snapImage()
        return True
    
    def moveUp(self, count):
        for i in range(1,count):
            self.send('RELMOVE Y=' + incrementY)
            time.sleep(0.5)
            self.snapImage()
        return True
    
    def moveDown(self, count):
        for i in range(1,count):
            self.send('RELMOVE Y=-' + incrementY)
            time.sleep(0.5)
            self.snapImage()
        return True

    def resetRow(self):
        self.send('RELMOVE Y=-' + incrementY)
        time.sleep(1)
        self.send('MOVE X = ' + incrementX)
        time.sleep(1)

    def startSearch(self):
        print "Scanning for flies..."
        self.pictureNumber = 0
        self.send('RELMOVE X=' + incrementX)
        for i in range(1,numberOfRows+1):
            print "Scanning row " + str(i) + "..."
            self.moveRight(rowSize)
            self.resetRow()
        return True

    def close(self):
        self.ser.close()
        del self.ser
        self.com = None
        return True
        
    def send(self, command):
        if self.ser:
            self.ser.write(command + '\n')

    def zero(self):
        self.send("ZERO")

    def moveTo(self, x, y):
        return self.send('M x = %d y = %d' %(x,y))

    def displace(self, disp_xyz):
        x,y,z = disp_xyz
        return self.send('RM x=%d y=%d z=%d' %(x,y,z))


