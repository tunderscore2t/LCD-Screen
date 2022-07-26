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
    self.CmdChr = chr(0xFE) 
    #self.HomeCursor()
    #self.AutoScrollOff()
    self.LCDs.write(b"Hello")

LCD()
