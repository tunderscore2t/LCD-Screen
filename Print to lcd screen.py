#Print to lcd screen
#Now avaiable on github

import os
import serial

class LCD:
	def __init__(self,port = '/dev/ttyACM0'):
		self.LCDs = serial.Serial(port)
		self.LCDs.baudrate = 9600
		self.LCDs.stopbits = serial.STOPBITS_ONE
		self.LCDs.parity   = serial.PARITY_NONE
		self.LCDs.bytesize = serial.EIGHTBITS
		self.LCDs.rtscts   = True
		self.LCDs.timeout  = 1
		#self.ClearScreen()
		self.GetData(chr(0xFE) + chr(0x58))
		
	def PutData(self,s):
		s_encoded = s.encode()
		print(len(s_encoded))
		self.LCDs.write(s_encoded)
	  
	def GetData(self,s):
		
		self.PutData(s)
		#s = "\xFE\x58"
		s = "Hello World"
		return s
		
	def ClearScreen(self):
		self.LCDs.write(b'\xFE\x58')
		self.LCDs.write(b"Hello")

LCD()
