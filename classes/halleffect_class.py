"""
Note: Both HallEffect.py and AcousticHandler.py must be have the same pinmode 
configuration. i.e. GPIO.BOARD, BCM, TEGRA_SOC, or CVM. 

What I found is compatible with adafruit is BOARD. User must change line 8 
in python3.8/site-packages/adafruit_blinka/microcontroller/tegra/t194/pin.py
to:

Jetson.GPIO.setmode(GPIO.BOARD)
"""
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread,QTimer
import time as time
try:
    import board
    import busio
    import numpy as np
    import matplotlib.pyplot as plt
    import adafruit_ads1x15.ads1115 as ADS
    from adafruit_ads1x15.analog_in import AnalogIn
    from scipy.interpolate import interp1d
   
    
    import time
    
    class HallEffect(QThread):
        """
        Class for managing the Hall Effect sensors via i2c
        Args:
            None
        """

        sensor_signal = pyqtSignal(list)

        def __init__(self, parent):
            super().__init__(parent=parent)
            self.parent = parent
            #set up sensor I2C
            #GPIO.setmode(GPIO.BOARD)
            self.i2c = busio.I2C(board.SCL, board.SDA)
            self.ads = ADS.ADS1115(self.i2c)
            
            self.chanPosY = AnalogIn(self.ads, ADS.P2)
            self.chanPosX = AnalogIn(self.ads, ADS.P1)  #big external EM
            self.chanNegY = AnalogIn(self.ads, ADS.P0)  # one of the 4 coil config Em
            self.chanNegX = AnalogIn(self.ads, ADS.P3)

            self.run_flag = True

   

        def createBounds(self):
            """
            creates initial bounds to be updated when field is being read
            Args:
                none
            Returns:
                list of min max bounds
            """
            #call this in readField maybe
            neg_max = float(100000002)
            pos_max = -float(100000000)
            return [neg_max, pos_max]
        
        def readFIELD(self, channel,bound):
            """
            reads hall effect sensor field data given an analog obejct
            Args:
                channel:   AnalogIN channel object 1-4
                bound: class object that stores the min and max bounds generated from sensor
            Returns:
                mapped_field: scaled field value -100 to 100
            """             
            VAL = channel.value

            if VAL < bound[0]:
                bound[0] = VAL
            elif VAL > bound[1]:
                bound[1] = VAL
               
            m = interp1d([bound[0],bound[1]],[-100,100])
            mapped_field = int(m(VAL))
            return mapped_field
        
        def run(self):
              
            posY = self.createBounds() #create bounds for positive Y EM sensor
            posX = self.createBounds() #create bounds for positive X EM sensor
            negY = self.createBounds() #create bounds for negative Y EM sensor
            negX = self.createBounds() #create bounds for negative X EM sensor
            while self.run_flag:
                
                s1 = self.readFIELD(self.chanPosY, posY)
                s2 = self.readFIELD(self.chanPosX, posX)
                s3 = self.readFIELD(self.chanNegY, negY)
                s4 = self.readFIELD(self.chanNegX, negX)

                self.sensor_signal.emit([s1,s2,s3])
                time.sleep(.1)
            print(" -- Sensor Process Terminated -- ")


        def stop(self):
            self.run_flag = False
            
except Exception:
    class HallEffect(QThread):
        sensor_signal = pyqtSignal(list)
        def __init__(self, parent):
            super().__init__(parent=parent)
            self.parent = parent
            self.run_flag = True
            
        def createBounds(self):
            pass
        def readFIELD(self, channel, bound):
            pass
        def showFIELD(self):
            pass
        def run(self):
            i=0
            while self.run_flag:
                
                bx = i
                by = 2
                bz = 3


                self.sensor_signal.emit([bx,by,bz])
                time.sleep(.1)
                i+=1
        def stop(self):
            self.run_flag = False
        



