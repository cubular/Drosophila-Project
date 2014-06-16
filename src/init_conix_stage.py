import time
import serial

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
	port='COM1',
	baudrate=9600,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS,
        rtscts = True,
)

print ser.name
ser.isOpen()

#ser.open()
#ser.isOpen()

# Reset coordinates to (0,0) at bottom left
out = ''
ser.write("MOVE X = 701000 Y = -2067405\n")
time.sleep(10)
ser.write("zero\n")
time.sleep(5)

# print 'Enter your commands below.\r\nInsert "exit" to leave the application.'
input=1
while 1 :
	# get keyboard input
	input = raw_input(">> ")
        # Python 3 users
        # input = input(">> ")
	if input == 'exit':
		ser.close()
		exit()
	else:
		# send the character to the device
		# (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
		ser.write(input + '\n')
		out = ''
		# let's wait one second before reading output (let's give device time to answer)
		time.sleep(1)
		while ser.inWaiting() > 0:
			out += ser.read(1)
			
		if out != '':
			print ">>" + out
