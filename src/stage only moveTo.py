import serial
import time

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

    def moveTo(self, x, y):
        return self.send('M x = %d y = %d' %(x,y))
		
        
    def send(self, command):
        if self.ser:
            self.ser.write(command + '\n')

