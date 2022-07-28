# Kibble Balance Thermal Control System
# LCD.py - Serial control for the Adafruit USB/Serial RGB LCD backpack kit

import os 
import time
import serial

class LCD:
  def __init__(self,port = "/dev/ttyACM0"):
    self.LCDs = serial.Serial(port)
    self.LCDs.baudrate = 9600
    self.LCDs.stopbits = serial.STOPBITS_ONE
    self.LCDs.parity   = serial.PARITY_NONE
    self.LCDs.bytesize = serial.EIGHTBITS
    self.LCDs.rtscts   = True
    self.LCDs.timeout  = 1
    self.CmdChr = chr(0xFE) 
    self.ClearScreen()
    self.HomeCursor()
    self.AutoScrollOff()
    self.LCDs.write(b"LCD Driver is go")
       
  
  def PutData(self,s):
	  s_encoded = s.encode() 
	  self.LCDs.write(s_encoded) #change to write single byte
	  #	iterate through string i.e for x in <string>
	  #	Convert unicode into byte:
	  #	Convert unicode into its hex equivelant
	  #	Chop off the final bit of the unicode
	  #	Feed that into the LCD screen
	  
	  #V2
	  #split unicode and send it into a bytearray
	  #loop adding it to a bytearray
	  #convert chr [0xFE] -> byte [0xFE]
	  #write the byte to screen
  
  def GetData(self,s):
    self.PutData(s)
    s = self.LCDs.readline()
    return s

  def DisplayOn(self):
    self.PutData(self.CmdChr+chr(0x42))

  def DisplayOff(self):
    self.PutData(self.CmdChr+chr(0x46))

  def AutoScrollOn(self):
    self.PutData(self.CmdChr+chr(0x51))

  def AutoScrollOff(self):
    self.PutData(self.CmdChr+chr(0x52))

  def ClearScreen(self):
    #self.PutData(self.CmdChr+chr(0x58))
    self.LCDs.write(b'\xFE\x58') #Do the sae

  def SetCursorPos(self,X,Y):
    self.PutData(self.CmdChr+chr(0x47)+chr(X)+chr(Y))

  def HomeCursor(self):
    self.PutData(self.CmdChr+chr(0x48))

  def CursorForward(self):
    self.PutData(self.CmdChr+chr(0x4d))

  def CursorBack(self):
    self.PutData(self.CmdChr+chr(0x4c))

  def UnderLineCursorOn(self):
    self.PutData(self.CmdChr+chr(0x4a))

  def UnderLineCursorOff(self):
    self.PutData(self.CmdChr+chr(0x4b))

  def BlockCursorOn(self):
    self.PutData(self.CmdChr+chr(0x53))

  def BlockCursorOn(self):
    self.PutData(self.CmdChr+chr(0x54))

  def SetRGB(self,R,G,B):
    self.PutData(self.CmdChr+chr(0xD0)+chr(R)+chr(G)+chr(B))

  def WriteAt(self,x,y,img):
    self.SetCursorPos(x,y)
    self.PutData(img)

class Field:
  def __init__(self,fmt,ulim,llim):
    self.image=""
    self.ulim = ulim
    self.llim = llim 
    self.fmt  = fmt
    self.SetData(0.0)
  
  def SetData(self,f):
    if f > self.ulim: f = self.ulim
    if f < self.llim: f = self.llim
    self.data = f
    self.image = self.fmt % (self.data)

  def s(self):
    self.image = self.fmt % (self.data)
    return self.image

class LineController:
  def __init__(self,LCD,line,delay):
    self.LCD = LCD
    self.line = line
    self.cline = 0
    self.lines = []
    self.nxtime = time.time() + delay
    self.delay = delay

  def AddLine(self,line):
    self.lines.append(line)

  def Service(self):
    if time.time() > self.nxtime:
      self.cline = self.cline + 1
      if self.cline >= len(self.lines):
        self.cline = 0
      op = self.lines[self.cline]()
      self.LCD.WriteAt(1,self.line,op)
      self.nxtime = time.time() + self.delay

