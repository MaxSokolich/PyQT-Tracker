import numpy as np
from scipy import interpolate



class Actions:
    """
    Actions are inherited in the Controller class.
    In order to bind to the controller events, subclass the Controller class and
    override desired action events in this class.
    
    
    self.Bx             : magnetic field in x
    self.By             : magnetic field in y
    self.Bz             : magnetic field in z
    self.Mx             : stage motor in x
    self.My             : stage motor in y
    self.Mz             : stage motor in z
    self.alpha          : rolling polar angle 
    self.gamma          : rolling azimuthal angle
    self.freq.          : rolling frequency
    self.acoustic_status: acoustic module status on or off
    """
    def __init__(self):
        self.right_stick = [0,0]
        self.left_stick = [0,0]
        #iprocessing queue for storing joystick actions in seperate thread
        
        #initlize actions actions
        self.Bx, self.By, self.Bz = 0,0,0
        self.Mx, self.My, self.Mz = 0,0,0
        self.alpha, self.gamma, self.freq = 0,0,0
        self.acoustic_status = 0
        
        return
    
    def on_x_press(self):
        """
        acoustic on
        """
        self.acoustic_status = 1
        actions = [self.Bx, self.By, self.Bz,
                  self.Mx, self.My, self.Mz,
                  self.alpha, self.gamma, self.freq,
                  self.acoustic_status]
        self.queue.put(actions)

    def on_x_release(self):
        """
        acoustic off
        """
        self.acoustic_status = 0
        actions = [self.Bx, self.By, self.Bz,
                  self.Mx, self.My, self.Mz,
                  self.alpha, self.gamma, self.freq,
                  self.acoustic_status]
        self.queue.put(actions)

    def on_triangle_press(self):
        """
        quick spin 10 Hz on
        """
        self.gamma = 0
        self.freq = 10
        actions = [self.Bx, self.By, self.Bz,
                  self.Mx, self.My, self.Mz,
                  self.alpha, self.gamma, self.freq,
                  self.acoustic_status]
        self.queue.put(actions)
       

    def on_triangle_release(self):
        """
        quick spin 10 Hz off
        """
        self.gamma = 0
        self.freq = 0
        actions = [self.Bx, self.By, self.Bz,
                  self.Mx, self.My, self.Mz,
                  self.alpha, self.gamma, self.freq,
                  self.acoustic_status]
        self.queue.put(actions)
        

    def on_circle_press(self):
        pass

    def on_circle_release(self):
        pass

    def on_square_press(self):
        pass

    def on_square_release(self):
        pass

    """
    # FUNCTIONS FOR TYP 0 --> MOTOR STAGE
    """
    def on_L2_press(self, value):
        """
        negative Z stage on
        """
        
        f = interpolate.interp1d([-1,1], [0,1])  #need to map the -1 to 1 output to 0-1
        self.Mz = -round(float(f(value/32767)),3)
    
        actions = [self.Bx, self.By, self.Bz,
                  self.Mx, self.My, self.Mz,
                  self.alpha, self.gamma, self.freq,
                  self.acoustic_status]
        self.queue.put(actions)
        
    def on_L2_release(self):
        """
        negative Z stage off
        """
        self.Mz = 0
        actions = [self.Bx, self.By, self.Bz,
                  self.Mx, self.My, self.Mz,
                  self.alpha, self.gamma, self.freq,
                  self.acoustic_status]
        self.queue.put(actions)
        

    def on_R2_press(self, value):
        """
        positive Z stage on
        """
    
        f = interpolate.interp1d([-1,1], [0,1])  #need to map the -1 to 1 output to 0-1
        self.Mz = round(float(f(value/32767)),3)
   
        actions = [self.Bx, self.By, self.Bz,
                  self.Mx, self.My, self.Mz,
                  self.alpha, self.gamma, self.freq,
                  self.acoustic_status]
        self.queue.put(actions)

    def on_R2_release(self):
        """
        positive Z stage off
        """
        
        self.Mz = 0
        actions = [self.Bx, self.By, self.Bz,
                  self.Mx, self.My, self.Mz,
                  self.alpha, self.gamma, self.freq,
                  self.acoustic_status]
        self.queue.put(actions)

    def on_up_arrow_press(self):
        """
        postitive Y stage motor on 
        """
        
        self.My = 1
        actions = [self.Bx, self.By, self.Bz,
                  self.Mx, self.My, self.Mz,
                  self.alpha, self.gamma, self.freq,
                  self.acoustic_status]
        self.queue.put(actions)
        
    def on_up_down_arrow_release(self):
        """
        Y stage motor off 
        """
        self.My = 0
        actions = [self.Bx, self.By, self.Bz,
                  self.Mx, self.My, self.Mz,
                  self.alpha, self.gamma, self.freq,
                  self.acoustic_status]
        self.queue.put(actions)
        
    def on_down_arrow_press(self):
        """
        negative Y stage motor on
        """
        self.My = -1
        actions = [self.Bx, self.By, self.Bz,
                  self.Mx, self.My, self.Mz,
                  self.alpha, self.gamma, self.freq,
                  self.acoustic_status]
        self.queue.put(actions)

    def on_left_arrow_press(self):
        """
        negative X stage motor on
        """
        self.Mx = -1
        actions = [self.Bx, self.By, self.Bz,
                  self.Mx, self.My, self.Mz,
                  self.alpha, self.gamma, self.freq,
                  self.acoustic_status]
        self.queue.put(actions)

    def on_left_right_arrow_release(self):
        """
        X stage motor off
        """
        self.Mx = 0
        actions = [self.Bx, self.By, self.Bz,
                  self.Mx, self.My, self.Mz,
                  self.alpha, self.gamma, self.freq,
                  self.acoustic_status]
        self.queue.put(actions)
        

    def on_right_arrow_press(self):
        """
        positive X stage motor on
        """
        self.Mx = 1
        actions = [self.Bx, self.By, self.Bz,
                  self.Mx, self.My, self.Mz,
                  self.alpha, self.gamma, self.freq,
                  self.acoustic_status]
        self.queue.put(actions)
    

    """
    # FUNCTIONS  COIL ROLL
    """
    def get_right_stick_xy(self): ######new adding
        """
        coil roll on
        """
        x = round(self.right_stick[0]/32767,3)
        y = -round(self.right_stick[1]/32767,3)
        if self.right_stick == [0,0]:
            self.alpha = 0
            self.gamma = 0
            self.freq = 0

        elif x == 0 and y > 0:
            self.alpha = np.pi/2
            self.gamma = 90
            self.freq = int(np.sqrt((x)**2 + (y)**2)*20)
            
        elif x == 0 and y < 0:
            self.alpha = -np.pi/2
            self.gamma = 90
            self.freq = int(np.sqrt((x)**2 + (y)**2)*20)
        else:
            angle = np.arctan2(y,x) + np.pi/2
            self.alpha = round(angle,3)
            self.gamma = 90
            self.freq = int(np.sqrt((x)**2 + (y)**2)*20)
       
        actions = [self.Bx, self.By, self.Bz,
                  self.Mx, self.My, self.Mz,
                  self.alpha, self.gamma, self.freq,
                  self.acoustic_status]
        self.queue.put(actions)
    

    """
    # FUNCTIONS FOR COIL ORIENT
    """
    def get_left_stick_xy(self): ######new adding
        """
        coil orient on
        """
        x = round(self.left_stick[0],3)
        y = -round(self.left_stick[1],3)
        
        self.Bx = round(x/32767,3)
        self.By = round(y/32767,3)
         
        actions = [self.Bx, self.By, self.Bz,
                  self.Mx, self.My, self.Mz,
                  self.alpha, self.gamma, self.freq,
                  self.acoustic_status]
        self.queue.put(actions)
    
    def on_L1_press(self):
        """
        coil orient -Z on
        """
        self.Bz = -1
        actions = [self.Bx, self.By, self.Bz,
                  self.Mx, self.My, self.Mz,
                  self.alpha, self.gamma, self.freq,
                  self.acoustic_status]
        self.queue.put(actions)
        

    def on_L1_release(self):
        """
        coil orient -Z off
        """
        self.Bz = 0
        actions = [self.Bx, self.By, self.Bz,
                  self.Mx, self.My, self.Mz,
                  self.alpha, self.gamma, self.freq,
                  self.acoustic_status]
        self.queue.put(actions)
        
    def on_R1_press(self):
        """
        coil orient +Z on
        """
        self.Bz = 1
        actions = [self.Bx, self.By, self.Bz,
                  self.Mx, self.My, self.Mz,
                  self.alpha, self.gamma, self.freq,
                  self.acoustic_status]
        self.queue.put(actions)

    def on_R1_release(self):
        """
        coil orient +Z off
        """
        self.Bz = 0
        actions = [self.Bx, self.By, self.Bz,
                  self.Mx, self.My, self.Mz,
                  self.alpha, self.gamma, self.freq,
                  self.acoustic_status]
        self.queue.put(actions)

    def on_L3_up(self, value):
        pass

    def on_L3_down(self, value):
        pass

    def on_L3_left(self, value):
        pass

    def on_L3_right(self, value):
        pass

    def on_L3_y_at_rest(self):
        """L3 joystick is at rest after the joystick was moved and let go off"""
        pass

    def on_L3_x_at_rest(self):
        """L3 joystick is at rest after the joystick was moved and let go off"""
        pass

    def on_L3_press(self):
        """L3 joystick is clicked. This event is only detected when connecting without ds4drv"""
        pass

    def on_L3_release(self):
        """L3 joystick is released after the click. This event is only detected when connecting without ds4drv"""
        pass

    def on_R3_up(self, value):
        pass

    def on_R3_down(self, value):
        pass

    def on_R3_left(self, value):
        pass

    def on_R3_right(self, value):
        pass

    def on_R3_y_at_rest(self):
        """R3 joystick is at rest after the joystick was moved and let go off"""
        pass

    def on_R3_x_at_rest(self):
        """R3 joystick is at rest after the joystick was moved and let go off"""
        pass

    def on_R3_press(self):
        """R3 joystick is clicked. This event is only detected when connecting without ds4drv"""
        pass

    def on_R3_release(self):
        """R3 joystick is released after the click. This event is only detected when connecting without ds4drv"""
        pass

    def on_options_press(self):
        pass

    def on_options_release(self):
        pass

    def on_share_press(self):
        """this event is only detected when connecting without ds4drv"""
        pass

    def on_share_release(self):
        """this event is only detected when connecting without ds4drv"""
        pass

    def on_playstation_button_press(self,exit):
        """this event is only detected when connecting without ds4drv"""
        print("Disconnecting")
        actions = False
        self.queue.put(actions)
        exit(1)

    def on_playstation_button_release(self):
        """this event is only detected when connecting without ds4drv"""
        pass
