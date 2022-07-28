#LCD Test
#Jean Morris, Ran Urquart-Gilmore

import Display
import os
from datetime import datetime
import numpy as np
import random

class ResistorOvenLCD():
    def __init__(self):
        super().__init__()
        self.Dsp = Display.Display()

    def WriteDisplay(self): #LCD display
        #self.Dsp = Display.Display()
        self.Dsp.DiffT.SetData(random.uniform(1,5)) #dT
        self.Dsp.AvCanT.SetData(random.uniform(29.5,30.5)) #DewarTemp
        self.Dsp.TargT.SetData(30) #Target       
        self.Dsp.AvAmbT.SetData(random.uniform(23,28)) #AmbTemp
        self.Dsp.Pwr.SetData(random.uniform(30,40)) #power
        self.Dsp.DacV.SetData(random.uniform(3,3.2)) #heaterV
        self.Dsp.Prop.SetData(4) #P
        self.Dsp.Int.SetData(random.uniform(-3,3)) #accum
        self.Dsp.Damp.SetData(160) #D
        self.Dsp.Amb.SetData(10) #ambPwr

while True:   
    ResistorOvenLCD = ResistorOvenLCD()
    ResistorOvenLCD.WriteDisplay()
    Dsp = Display.Display()
    Dsp.DisplayService()
