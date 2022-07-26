# Kibble Balance Thermal Control System
# Display.py - Display driver for the Resistor Oven

# Written by Ian Robinson (ian.robinson@npl.co.uk)

import time
import datetime
import socket
import LCD

class Display:
  def __init__(self):
    self.MyLCD    = LCD.LCD()
    self.DiffT    = LCD.Field("% 7.3f",99.999,-99.999)
    self.AvCanT   = LCD.Field("% 7.3f",99.999,-99.999)
    self.TargT    = LCD.Field("% 7.3f",99.999,-99.999)
    self.AvAmbT   = LCD.Field("% 7.3f",99.999,-99.999)
    self.Pwr      = LCD.Field("% 7.3f",99.999,-99.999)
    self.DacV     = LCD.Field("% 7.3f",99.999,-99.999)
    self.Prop     = LCD.Field("% 7.3f",99.999,-99.999)
    self.Int      = LCD.Field("% 7.3f",99.999,-99.999)
    self.Damp     = LCD.Field("% 7.3f",99.999,-99.999)    
    self.Amb      = LCD.Field("% 7.3f",99.999,-99.999)
    self.MJDT     = LCD.Field("% 12.6f",100000.0,50000.0)
    self.Nrdg     = LCD.Field("% 4.0f",999,0)
    
    self.MyLine1  = LCD.LineController(self.MyLCD,1,2)
    self.MyLine2  = LCD.LineController(self.MyLCD,2,2)
    self.MyLCD.ClearScreen()
    time.sleep(1)
    
    self.MyLine1.AddLine(self.DiffTLine)
    self.MyLine1.AddLine(self.ACTLine)
    self.MyLine2.AddLine(self.TGTLine)
    self.MyLine2.AddLine(self.AATLine)
    self.MyLine2.AddLine(self.PWRLine)
    self.MyLine2.AddLine(self.DateLine)
    self.MyLine2.AddLine(self.MNLine)
    self.MyLine2.AddLine(self.IPLine)
    self.MyLine2.AddLine(self.MJDLine)
    self.MyLine2.AddLine(self.RSNLine)

  def DiffTLine(self):
    st = "DiffT  " + self.DiffT.s() + " C " 
    return st[0:16]
  def ACTLine(self):
    st = "AvCanT " + self.AvCanT.s() + " C "
    return st[0:16]
  def TGTLine(self):
    st = "TargT  " + self.TargT.s() + " C " 
    return st[0:16]
  def AATLine(self):
    st = "AvAmbT " + self.AvAmbT.s() + " C " 
    return st[0:16]
  def PWRLine(self):
    st = "Pwr    " + self.Pwr.s() + " W " 
    return st[0:16]
  def AVNLine(self):
    st = "Navg   " + self.Nrdg.s() + "        " 
    return st[0:16]
  def DateLine(self):
    now = datetime.datetime.now()
    st = now.strftime("%d/%m/%y %H:%M") + "   "  
    return st[0:16]
  def MNLine(self):
    MName = socket.gethostname()
    st = MName + "            "  
    return st[0:16]
  def IPLine(self):
    MName = socket.gethostname()
    try:
      IPAdd = socket.gethostbyname(MName)
    except:
      IPAdd = "---.---.---.---"
    st = IPAdd + "            "  
    return st[0:16]
  def MJDLine(self):
    MJDTime = (time.time()/86400.0) + 40587.0
    self.MJDT.SetData(MJDTime)
    st = self.MJDT.s() + "        "
    return st[0:16]
  def RSNLine(self):
    ResNo = "262766"
    st = "RSerNo:" + ResNo + "        " 
    return st[0:16]
  
  def DisplayService(self):
    self.MyLine1.Service()
    self.MyLine2.Service()
