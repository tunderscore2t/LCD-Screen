#Print to lcd screen
#Now avaiable on github

import os
import serial

class LCD:
	def __init__(self,port = 'COM3'): # '/dev/ttyACM0' -raspberry pi 'COM3' - windows
		self.LCDs = serial.Serial(port)
		self.LCDs.baudrate = 9600
		self.LCDs.stopbits = serial.STOPBITS_ONE
		self.LCDs.parity   = serial.PARITY_NONE
		self.LCDs.bytesize = serial.EIGHTBITS
		self.LCDs.rtscts   = True
		self.LCDs.timeout  = 1
		#self.ClearScreen()
		self.GetData(chr(0xFE) + chr(0x58))
		#self.GetData("Hello")
		
	def PutData(self,s):
		split_string = list(s)
		string_length = len(s)
		array = []
		for i in range (0, string_length):
			pointer = ord(split_string[i])
			array.append(pointer)
		byte_array = bytearray(array)
		print(byte_array)
		self.LCDs.write(byte_array)

	  
	def GetData(self,s):
		self.PutData(s)
		return s
		
	def ClearScreen(self):
		self.LCDs.write(b'\xFE\x58')
		self.LCDs.write(b"Hello")

LCD()
