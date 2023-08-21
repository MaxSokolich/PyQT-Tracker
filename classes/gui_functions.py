from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
from PyQt5.QtGui import QWheelEvent
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.QtCore import Qt, QTimer, PYQT_VERSION_STR
from PyQt5 import QtWidgets, QtGui, QtCore
import cv2
import os
from os.path import expanduser

import pandas as pd
from datetime import datetime
import sys
from PyQt5.QtWidgets import QApplication
import numpy as np
import cv2
import matplotlib.pyplot as plt 
import time
import platform
os.environ["SDL_JOYSTICK_ALLOW_BACKGROUND_EVENTS"] = "1"
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
try:
    import EasyPySpin
except Exception:
    pass

from classes.tracker_class import VideoThread
from classes.gui_widgets import Ui_MainWindow

from classes.robot_class import Robot
from classes.arduino_class import ArduinoHandler
from classes.joystick_class import Mac_Controller,Linux_Controller,Windows_Controller
from classes.simulation_class import HelmholtzSimulator
from classes.projection_class import AxisProjection
from classes.acoustic_class import AcousticClass
from classes.halleffect_class import HallEffect
#from classes.record_class import RecordThread



class MainWindow(QtWidgets.QMainWindow):
    positionChanged = QtCore.pyqtSignal(QtCore.QPoint)

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        
        
        #self.showMaximized()

        #resize some widgets to fit the screen better
        screen  = QtWidgets.QDesktopWidget().screenGeometry(-1)
        
        self.window_width = screen.width()
        self.window_height = screen.height()
        self.resize(self.window_width, self.window_height)
        self.display_width = self.window_width-265# self.ui.frameGeometry().width()

        self.displayheightratio = 0.79
        self.framesliderheightratio = 0.031
        self.textheightratio = .129
        #self.tabheightratio = 0.925
        
        self.aspectratio = 1041/801
        self.resize_widgets()

    
      
        #create folder in homerdiractory of user
        home_dir = expanduser("~")
        new_dir_name = "Tracking Data"
        desktop_path = os.path.join(home_dir, "Desktop")
        self.new_dir_path = os.path.join(desktop_path, new_dir_name)
        if not os.path.exists(self.new_dir_path):
            os.makedirs(self.new_dir_path)


        
        self.result = None
        self.currentframe = None
        self.videopath = 0
        self.cap = None
        self.drawing = False
        self.acoustic_frequency = 0
        self.magnetic_field_list = []
        
        self.actions = [0,0,0,0,0,0,0,0,0,0,0,0]
        self.Bx, self.By, self.Bz = 0,0,0
        self.Mx, self.My, self.Mz = 0,0,0
        self.alpha, self.gamma, self.psi, self.freq = 0,0,0,0
        self.sensorBx, self.sensorBy, self.sensorBz = 0,0,0

        #control tab functions
        self.control_status = False
        self.joystick_status = False


        #connect to arduino
        if "mac" in platform.platform():
            self.tbprint("Detected OS: macos")
            PORT = "/dev/cu.usbmodem2101"
            self.controller_actions = Mac_Controller()
        elif "Linux" in platform.platform():
            self.tbprint("Detected OS: Linux")
            PORT = "/dev/ttyACM0"
            self.controller_actions = Linux_Controller()
        elif "Windows" in platform.platform():
            self.tbprint("Detected OS:  Windows")
            PORT = "COM3"
            self.controller_actions = Windows_Controller()
        else:
            self.tbprint("undetected operating system")
            PORT = None
        
        self.arduino = ArduinoHandler(self.tbprint)
        self.arduino.connect(PORT)
        
        
        #define, simulator class, pojection class, and acoustic class
        self.simulator = HelmholtzSimulator(self.ui.magneticfieldsimlabel, width=310, height=310, dpi=200)
        self.projection = AxisProjection()
        self.acoustic_module = AcousticClass()
        self.halleffect = HallEffect(self)
        self.halleffect.sensor_signal.connect(self.update_halleffect_sensor)
        self.halleffect.start()
        
        
        
        pygame.init()
        if pygame.joystick.get_count() == 0:
            self.tbprint("No Joystick Connected...")
            
        else:
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()
            self.tbprint("Connected to: "+str(self.joystick.get_name()))
        
        

     

        #tracker tab functions
        self.ui.pausebutton.hide()
        self.ui.leftbutton.hide()
        self.ui.rightbutton.hide()
        
        self.ui.choosevideobutton.clicked.connect(self.selectFile)
        self.ui.trackbutton.clicked.connect(self.track)
        self.ui.pausebutton.clicked.connect(self.pause)
        self.ui.rightbutton.clicked.connect(self.frameright)
        self.ui.leftbutton.clicked.connect(self.frameleft)
        self.ui.maskbutton.clicked.connect(self.showmask)
        self.ui.maskinvert_checkBox.toggled.connect(self.invertmaskcommand)
        self.ui.maskthreshbox.valueChanged.connect(self.get_slider_vals)
        self.ui.maskdilationbox.valueChanged.connect(self.get_slider_vals)
        self.ui.maskblurbox.valueChanged.connect(self.get_slider_vals)
        self.ui.croplengthbox.valueChanged.connect(self.get_slider_vals)
        self.ui.savedatabutton.clicked.connect(self.savedata)
        self.ui.VideoFeedLabel.installEventFilter(self)
        self.ui.recordbutton.clicked.connect(self.recordfunction)
        self.ui.controlbutton.clicked.connect(self.toggle_control_status)
        self.ui.memorybox.valueChanged.connect(self.get_slider_vals)
        self.ui.RRTtreesizebox.valueChanged.connect(self.get_slider_vals)
        self.ui.arrivalthreshbox.valueChanged.connect(self.get_slider_vals)
        self.ui.magneticfrequencydial.valueChanged.connect(self.get_slider_vals)
        self.ui.gammadial.valueChanged.connect(self.get_slider_vals)
        self.ui.psidial.valueChanged.connect(self.get_slider_vals)
        self.ui.applyacousticbutton.clicked.connect(self.apply_acoustic)
        self.ui.acousticfreq_spinBox.valueChanged.connect(self.get_acoustic_frequency)
        self.ui.resetdefaultbutton.clicked.connect(self.resetparams)
        self.ui.simulationbutton.clicked.connect(self.toggle_simulation)
        self.ui.orientradio.toggled.connect(self.checkorient)
        self.ui.objectivebox.valueChanged.connect(self.get_objective)
        self.ui.exposurebox.valueChanged.connect(self.get_exposure)
        self.ui.joystickbutton.clicked.connect(self.toggle_joystick_status)
        self.ui.leftfieldbutton.clicked.connect(self.quickfieldleft)
        self.ui.rightfieldbutton.clicked.connect(self.quickfieldright)
        self.ui.upfieldbutton.clicked.connect(self.quickfieldup)
        self.ui.downfieldbutton.clicked.connect(self.quickfielddown)
        self.ui.plusZbutton.clicked.connect(self.quickfieldplusZ)
        self.ui.minusZbutton.clicked.connect(self.quickfieldminusZ)
        self.ui.autoacousticbutton.clicked.connect(self.toggle_autoacoustic)

        #self.showFullScreen()


       

    def toggle_simulation(self):
        if self.ui.simulationbutton.isChecked():
            self.simulator.start()
            self.tbprint("Simulation Off")
            self.ui.simulationbutton.setText("Simulation Off")
        else:
            self.simulator.stop()
            self.tbprint("Simulation On")
            self.ui.simulationbutton.setText("Simulation On")
   
    
    
    def toggle_control_status(self): 
        if self.ui.controlbutton.isChecked():
            self.control_status = True
            self.ui.controlbutton.setText("Stop")
            self.tbprint("Control On: {} Hz".format(self.acoustic_frequency))
        else:
            self.control_status = False
            self.ui.controlbutton.setText("Control")
            self.tbprint("Control Off")
            self.apply_actions(False)
            
            
    

    def toggle_joystick_status(self):
        if pygame.joystick.get_count() != 0:
            if self.ui.joystickbutton.isChecked():
                self.joystick_status = True
                self.ui.joystickbutton.setText("Stop")
                self.tbprint("Joystick On")
            else:
                self.joystick_status = False
                self.ui.joystickbutton.setText("Joystick")
                self.tbprint("Joystick Off")
                self.apply_actions(False)
        else:
            self.tbprint("No Joystick Connected...")



    def update_actions(self, actions, stopped):
        #alpha argument is signal from tracker_class: actions_signal
        #output actions if control status is on
        if self.ui.autoacousticbutton.isChecked():
            self.acoustic_frequency  = actions[-1]   
        
        if self.control_status == True:
            self.Bx, self.By, self.Bz, self.alpha, self.gamma, self.freq, self.psi, _  = actions    
           
             


            if self.ui.orientradio.isChecked():
                self.freq = 0
            else:
                self.freq = self.ui.magneticfrequencydial.value()

            if stopped == True:
                self.Bx, self.By, self.Bz, self.alpha, self.gamma, self.freq, self.psi, self.acoustic_frequency = 0,0,0,0,0,0,0,0

            
        
        elif self.joystick_status == True:
            self.Bx, self.By, self.Bz, self.alpha, self.gamma, self.freq, self.psi, _ = self.controller_actions.run(self.joystick)
            
            if self.freq !=0:
                self.freq = self.ui.magneticfrequencydial.value()
            
        
        #save the current action outputs to a list to be saved 
        self.gamma = np.radians(self.ui.gammadial.value())
        self.psi = np.radians(self.ui.psidial.value())

        self.actions = [self.tracker.framenum,self.Bx, self.By, self.Bz, self.alpha, self.gamma, self.freq, self.psi, 
                        self.acoustic_frequency, self.sensorBx, self.sensorBy, self.sensorBz] 
        self.magnetic_field_list.append(self.actions)
        self.apply_actions(True)

        


    def apply_actions(self, status):
        #the purpose of this function is to output the actions via arduino, 
        # show the actions via the simulator
        # and record the actions by appending the field_list
        
        #toggle between alpha and orient
        if self.freq > 0:
            if self.ui.swimradio.isChecked():
                self.simulator.roll = False
            elif self.ui.rollradio.isChecked():
                self.alpha = self.alpha - np.pi/2
                self.simulator.roll = True

        #zero output
        if status == False:
            self.Bx, self.By, self.Bz, self.alpha, self.gamma, self.freq, self.psi = 0,0,0,0,0,0,0

        #send arduino commands
        self.arduino.send(self.Bx, self.By, self.Bz, self.alpha, self.gamma, self.freq, self.psi, self.acoustic_frequency)
        
        #output current actions to simulator
        self.simulator.Bx = self.Bx
        self.simulator.By = self.By
        self.simulator.Bz = self.Bz
        self.simulator.alpha = self.alpha
        self.simulator.gamma = self.gamma
        self.simulator.psi = self.psi
        self.simulator.freq = self.freq/15
        self.simulator.omega = 2 * np.pi * self.simulator.freq
    


    
    
    def toggle_autoacoustic(self):
        if self.cap is not None:
            if self.ui.autoacousticbutton.isChecked():
                self.tracker.autoacousticstatus = True
                self.ui.led.setStyleSheet("\n"
"                background-color: rgb(0, 255, 0);\n"
"                border-style: outset;\n"
"                border-width: 3px;\n"
"                border-radius: 12px;\n"
"                border-color: rgb(0, 255, 0);\n"
"         \n"
"                padding: 6px;")
            else:
                self.tracker.autoacousticstatus = False
                self.acoustic_frequency = 0
                self.ui.led.setStyleSheet("\n"
"                background-color: rgb(255, 0, 0);\n"
"                border-style: outset;\n"
"                border-width: 3px;\n"
"                border-radius: 12px;\n"
"                border-color: rgb(255, 0, 0);\n"
"         \n"
"                padding: 6px;")

    def get_acoustic_frequency(self):
        if self.ui.applyacousticbutton.isChecked():
            self.acoustic_frequency = self.ui.acousticfreq_spinBox.value()
            #self.tbprint("Control On: {} Hz".format(self.acoustic_frequency))
            self.apply_acoustic()
        
    
    def apply_acoustic(self):
        if self.ui.applyacousticbutton.isChecked():
            self.ui.applyacousticbutton.setText("Stop")
            #self.tbprint("Control On: {} Hz".format(self.acoustic_frequency))
            self.acoustic_frequency = self.ui.acousticfreq_spinBox.value()
            #self.acoustic_module.start(self.acoustic_frequency, 0)
            self.ui.led.setStyleSheet("\n"
"                background-color: rgb(0, 255, 0);\n"
"                border-style: outset;\n"
"                border-width: 3px;\n"
"                border-radius: 12px;\n"
"                border-color: rgb(0, 255, 0);\n"
"         \n"
"                padding: 6px;")
        
        else:
            self.ui.applyacousticbutton.setText("Apply")
            #self.tbprint("Acoustic Module Off")
            #self.acoustic_module.stop()
            self.acoustic_frequency = 0
            self.ui.led.setStyleSheet("\n"
"                background-color: rgb(255, 0, 0);\n"
"                border-style: outset;\n"
"                border-width: 3px;\n"
"                border-radius: 12px;\n"
"                border-color: rgb(255, 0, 0);\n"
"         \n"
"                padding: 6px;")
       
        

    def tbprint(self, text):
        #print to textbox
        self.ui.plainTextEdit.appendPlainText("$ "+ text)
        
    def get_slider_vals(self):
        memory = self.ui.memorybox.value()
        RRTtreesize = self.ui.RRTtreesizebox.value()
        arrivalthresh = self.ui.arrivalthreshbox.value()
        magneticfreq = self.ui.magneticfrequencydial.value()
        gamma = self.ui.gammadial.value()
        psi = self.ui.psidial.value()
        thresh = self.ui.maskthreshbox.value() 
        dilation = self.ui.maskdilationbox.value() 
        maskblur = self.ui.maskblurbox.value()
        crop_length = self.ui.croplengthbox.value()

        if self.cap is not None: 
            self.tracker.memory = memory
            self.tracker.RRTtreesize = RRTtreesize
            self.tracker.arrivalthresh = arrivalthresh
            self.tracker.mask_thresh = thresh
            self.tracker.mask_dilation = dilation
            self.tracker.mask_blur = maskblur
            self.tracker.crop_length = crop_length

        self.ui.gammalabel.setText("Gamma: {}".format(gamma))
        self.ui.psilabel.setText("Psi: {}".format(psi))
        self.ui.rollingfrequencylabel.setText("Freq: {}".format(magneticfreq))
        
  
        


    def selectFile(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.ReadOnly
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;Text Files (*.txt);;Python Files (*.py)", options=options)

        if file_path:
            self.videopath = file_path
            file_info = QtCore.QFileInfo(file_path)
            file_name = file_info.fileName()
            print(file_path, file_name)
            self.ui.choosevideobutton.setText(file_name)
            self.tbprint(file_name)
        else:
            self.videopath = 0
            self.ui.choosevideobutton.setText("Live")
            self.tbprint("Using Video Camera")


    def convert_coords(self,pos):
        #need a way to convert the video position of mouse to the actually coordinate in the window
        newx = int(pos.x() * (self.video_width / self.display_width)) 
        newy = int(pos.y() * (self.video_height / self.display_height))
        return newx, newy

    def eventFilter(self, object, event):
        if object is self.ui.VideoFeedLabel: 
            if self.cap is not None:
                if event.type() == QtCore.QEvent.MouseButtonPress:   
                    if event.buttons() == QtCore.Qt.LeftButton:
                        newx, newy = self.convert_coords(event.pos())
                        #generate original bounding box
                        crop_length = self.ui.croplengthbox.value()

                        x_1 = int(newx - crop_length  / 2)
                        y_1 = int(newy - crop_length  / 2)
                        w = crop_length
                        h = crop_length

                        #reset algorithm nodes
                        self.tracker.control_robot.reset()

                        robot = Robot()  # create robot instance
                        robot.add_frame(self.tracker.framenum)
                        robot.add_time(0)
                        robot.add_position([newx,newy])
                        robot.add_velocity([0,0,0])
                        robot.add_crop([x_1, y_1, w, h])
                        robot.add_area(0)
                        robot.add_blur(0)
                        
                        self.tracker.robot_list.append(robot)

                    if event.buttons() == QtCore.Qt.RightButton: 
                        self.drawing = True
                        newx, newy = self.convert_coords(event.pos())
                        if len(self.tracker.robot_list) > 0:
                            self.tracker.control_robot.reset()
                            self.tracker.control_robot.arrived = False
                            self.tracker.robot_list[-1].add_trajectory([newx, newy])
                
                
                    if event.buttons() == QtCore.Qt.MiddleButton: 
                        del self.tracker.robot_list[:]
                        del self.magnetic_field_list[:]
                        self.apply_actions(False)
                       
                    
                            
                elif event.type() == QtCore.QEvent.MouseMove:
                    if event.buttons() == QtCore.Qt.RightButton:
                        if self.drawing == True:
                            if len(self.tracker.robot_list)>0:
                                newx, newy = self.convert_coords(event.pos())
                                
                                self.tracker.robot_list[-1].add_trajectory([newx, newy])
                
                elif event.type() == QtCore.QEvent.MouseButtonRelease:
                    if event.buttons() == QtCore.Qt.RightButton: 
                        self.drawing = False
                        
                    
        return super().eventFilter(object, event)
        

    def update_image(self, frame):
        """Updates the image_label with a new opencv image"""
        #display projection
        if self.control_status == True or self.joystick_status == True:
            self.projection.roll = self.ui.rollradio.isChecked()
            frame, self.projection.draw_sideview(frame,self.Bx,self.By,self.Bz,self.alpha,self.gamma,self.video_width,self.video_height)
            frame, self.projection.draw_topview(frame,self.Bx,self.By,self.Bz,self.alpha,self.gamma,self.video_width,self.video_height)
        
    
        self.currentframe = frame
        if self.result is not None:
            cv2.putText(frame,"frame: " + str(self.tracker.framenum),
                        (int(self.video_width / 15),
                         int(self.video_height / 30)),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=1, 
                        thickness=4,
                        color = (255, 255, 255))
            self.result.write(frame)
        

        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
      
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.display_width, self.display_height, Qt.KeepAspectRatio)
        qt_img = QPixmap.fromImage(p)
       
        #update frame slider too
        self.ui.framelabel.setText("Frame:"+str(self.tracker.framenum))
        if self.videopath !=0:
            self.ui.frameslider.setValue(self.tracker.framenum)
        
        #also update robot info
        if len(self.tracker.robot_list) > 0:
            robot_diameter = round(np.sqrt(4*self.tracker.robot_list[-1].avg_area/np.pi),1)
            self.ui.vellcdnum.display(self.tracker.robot_list[-1].velocity_list[-1][2])
            self.ui.blurlcdnum.display(self.tracker.robot_list[-1].blur_list[-1])
            self.ui.sizelcdnum.display(robot_diameter)
                
       
        self.ui.VideoFeedLabel.setPixmap(qt_img)
        

    

    def update_croppedimage(self, frame):
        """Updates the cropped image_label with a new cropped opencv image"""
        
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(310, 310, Qt.KeepAspectRatio)
        qt_cimg = QPixmap.fromImage(p)
        self.ui.CroppedVideoFeedLabel.setPixmap(qt_cimg)
    


         
    """def recordfunction_class(self):
        if self.cap is not None:
            if self.ui.recordbutton.isChecked():
                
                self.recorder = RecordThread(self)
                self.recorder.recordstatus = True
                self.recorder.start()
                

                self.ui.recordbutton.setText("Stop")
                self.tbprint("Start Record")
                
            else:
                self.recorder.stop()
                self.ui.recordbutton.setText("Record")
                self.tbprint("End Record, Data Saved")
                self.savedata()"""


    def recordfunction(self):
        if self.cap is not None:
            if self.ui.recordbutton.isChecked():
                self.ui.recordbutton.setText("Stop")
                self.tbprint("Start Record")
                date = datetime.now().strftime('%Y.%m.%d-%H.%M.%S')
                file_path  = os.path.join(self.new_dir_path, date+".mp4")
                self.rec_start_time = time.time()
                self.result = cv2.VideoWriter(
                    file_path,
                    cv2.VideoWriter_fourcc(*"mp4v"),
                    int(self.videofps),    
                    (self.video_width, self.video_height), ) 
            else:
                self.ui.recordbutton.setText("Record")
                if self.result is not None:
                    self.result.release()
                    self.result = None
                    self.tbprint("End Record, Data Saved")
                    self.savedata()
                    

    def track(self):
        if self.videopath is not None:
                        
            if self.ui.trackbutton.isChecked():

                if self.videopath == 0:
                    try:
                        self.cap  = EasyPySpin.VideoCapture(0)
                    except Exception:
                        self.cap  = cv2.VideoCapture(0) 
                        self.tbprint("No EasyPySpin Camera Available")
        
                else:
                    self.cap  = cv2.VideoCapture(self.videopath)
                    self.ui.pausebutton.show()
                    self.ui.leftbutton.show()
                    self.ui.rightbutton.show()
                
    
                self.video_width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                self.video_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                self.videofps = int(self.cap.get(cv2.CAP_PROP_FPS))
                self.tbprint("Width: {}  --  Height: {}  --  Fps: {}".format(self.video_width,self.video_height,self.videofps))

                self.aspectratio = (self.video_width / self.video_height)

                self.resize_widgets()        
                
                self.ui.VideoFeedLabel.setStyleSheet("border:2px solid rgb(0, 255, 0); ")
                self.ui.CroppedVideoFeedLabel.setStyleSheet("border:2px solid rgb(0, 255, 0); ")
        
                
                if self.videopath != 0:
                    self.totalnumframes = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
                    self.ui.frameslider.setGeometry(QtCore.QRect(10, self.display_height+12, self.display_width, 20))
                    self.ui.frameslider.setMaximum(self.totalnumframes)
                    self.ui.frameslider.show()
            
                self.tracker = VideoThread(self)
                self.tracker.change_pixmap_signal.connect(self.update_image)
                self.tracker.cropped_frame_signal.connect(self.update_croppedimage)
                self.tracker.actions_signal.connect(self.update_actions)
                self.tracker.start()
                
                self.ui.trackbutton.setText("Stop")

                if self.videopath == 0:
                    self.ui.robotsizeunitslabel.setText("um")
                    self.ui.robotvelocityunitslabel.setText("um/s")
                    
                else:
                    self.ui.robotsizeunitslabel.setText("px")
                    self.ui.robotvelocityunitslabel.setText("px/s")
                    
                    
                if self.videopath == 0:
                    self.ui.pausebutton.hide()
                    self.ui.leftbutton.hide()
                    self.ui.rightbutton.hide()
                    self.ui.frameslider.hide()
        
                
            else:
                self.ui.VideoFeedLabel.setStyleSheet("background-color: rgb(0,0,0); border:2px solid rgb(255, 0, 0); ")
                self.ui.CroppedVideoFeedLabel.setStyleSheet("background-color: rgb(0,0,0); border:2px solid rgb(255, 0, 0); ")
        
                
                if self.cap is not None:
                    self.ui.trackbutton.setText("Track")
                    self.tracker.stop()
                    
                    #reset control button
                    self.control_status = False
                    self.ui.controlbutton.setText("Control")
                    self.tbprint("Control Off")
                    self.ui.controlbutton.setChecked(False)

                    #reset joystick button
                    self.joystick_status = False
                    self.ui.joystickbutton.setText("Joystick")
                    self.tbprint("Joystick Off")
                    self.ui.joystickbutton.setChecked(False)

                    #reset mask button
                    self.tracker.mask_flag = False
                    self.ui.maskbutton.setText("Mask")
                    self.ui.maskbutton.setChecked(False)

                    
                    #also reset pause button
                    self.ui.pausebutton.setChecked(False)
                    self.ui.pausebutton.setText("Pause")

                    self.ui.pausebutton.hide()
                    self.ui.leftbutton.hide()
                    self.ui.rightbutton.hide()
                

                    #zero arduino commands
                    self.apply_actions(False)

                    self.ui.applyacousticbutton.setChecked(False)
                    self.ui.led.setStyleSheet("\n"
                    "                background-color: rgb(255, 0, 0);\n"
                    "                border-style: outset;\n"
                    "                border-width: 3px;\n"
                    "                border-radius: 12px;\n"
                    "                border-color: rgb(255, 0, 0);\n"
                    "         \n"
                    "                padding: 6px;")
                    
            
        
            

    def showmask(self):
        if self.cap is not None:
            if self.ui.maskbutton.isChecked():
                self.ui.maskbutton.setText("Original")
                self.tracker.mask_flag = True
            else:
                self.ui.maskbutton.setText("Mask")
                self.tracker.mask_flag = False


    
         
    def get_objective(self):
        if self.cap is not None:
            self.tracker.objective = self.ui.objectivebox.value()

    def get_exposure(self):
        if self.cap is not None:
            self.tracker.exposure = self.ui.exposurebox.value()
            
    def checkorient(self):
        if self.cap is not None:
            self.tracker.orientstatus = self.ui.orientradio.isChecked()

    def invertmaskcommand(self):
        if self.cap is not None:
            self.ui.maskinvert_checkBox.setText("Invert Mask: " + str(self.ui.maskinvert_checkBox.isChecked()))
            self.tracker.maskinvert = self.ui.maskinvert_checkBox.isChecked()

    def pause(self):
        if self.videopath != 0:
            if self.ui.pausebutton.isChecked():
                self.tracker._play_flag = False
                self.ui.pausebutton.setText("Play")
              
            else:#play
                self.tracker._play_flag = True
                self.ui.pausebutton.setText("Pause")
                
    def frameright(self):
        if self.videopath != 0:
            self.tracker.framenum+=1
            self.ui.frameslider.setValue(self.tracker.framenum)
            self.ui.framelabel.setText("Frame:"+str(self.tracker.framenum))

    def frameleft(self):
        if self.videopath != 0:
            self.tracker.framenum-=1
            self.ui.frameslider.setValue(self.tracker.framenum)
            self.ui.framelabel.setText("Frame:"+str(self.tracker.framenum))

    def savedata(self):
        date = datetime.now().strftime('%Y.%m.%d-%H.%M.%S')
        file_path  = os.path.join(self.new_dir_path, date+".xlsx")
        robot_dictionary = []
        for bot in self.tracker.robot_list:
            robot_dictionary.append(bot.as_dict())
        
        with pd.ExcelWriter(file_path) as writer:
            
            if self.cap is not None: 
                if len(self.tracker.robot_list)>0:      
        
                    for idx, mydict in enumerate(robot_dictionary, start=0):
                        # Create a DataFrame from the dictionary
                        df = pd.DataFrame()
                        
                        for key, value in mydict.items():
                            if key == "Frame":
                                df[f"{key}"] = pd.Series(value, dtype='float64')
                        
                            elif key == "Times":
                                df[f"{key}"] = pd.Series(value, dtype='float64')
                        
                            elif key == "Position":
                                if len(value) > 0:
                                    x_coords, y_coords = zip(*value)
                                    df[f"{key}_X"] = pd.Series(x_coords, dtype='float64')
                                    df[f"{key}_Y"] = pd.Series(y_coords, dtype='float64')
                        
                            elif key == "Velocity":
                                if len(value) > 0:
                                    x_coords, y_coords, mag = zip(*value)
                                    df[f"{key}_X"] = pd.Series(x_coords, dtype='float64')
                                    df[f"{key}_Y"] = pd.Series(y_coords, dtype='float64')
                                    df[f"{key}_Mag"] = pd.Series(mag, dtype='float64')
                            
                            elif key == "Cropped Frame Dim":
                                if len(value) > 0:
                                    x1, y1, w, h = zip(*value)
                                    df[f"{key}_x1"] = pd.Series(x1, dtype='float64')
                                    df[f"{key}_y1"] = pd.Series(y1, dtype='float64')
                                    df[f"{key}_w"] = pd.Series(w, dtype='float64')
                                    df[f"{key}_h"] = pd.Series(h, dtype='float64')
                            
                            elif key == "Area":
                                df[f"{key}"] = pd.Series(value, dtype='float64')

                            elif key == "Blur":
                                df[f"{key}"] = pd.Series(value, dtype='float64')
                            
                            elif key == "Avg Area":
                                df[f"{key}"] = pd.Series(value, dtype='float64')
                        
                            elif key == "Trajectory":
                                if len(value) > 0:
                                    x_coords, y_coords = zip(*value)
                                    df[f"{key}_X"] = pd.Series(x_coords, dtype='float64')
                                    df[f"{key}_Y"] = pd.Series(y_coords, dtype='float64')
                        
                            elif key == "Acoustic Frequency":
                                if len(value) > 0:
                                    df[f"{key}"] = pd.Series(value, dtype='float64')


                            # Write the DataFrame to a separate sheet with sheet name "Sheet_<idx>"
                            df.to_excel(writer, sheet_name=f"Robot_{idx+1}", index=False)
                        
            #also save the magnetic field params 
            if len(self.magnetic_field_list) > 0:     
                df2 = pd.DataFrame()      

                MFFrame, Bx, By, Bz, alpha, gamma, freq, psi, acoustic_freq ,sensorBx, sensorBy, sensorBz = zip(*self.magnetic_field_list)
                df2[f"Applied on Frame"] = pd.Series(MFFrame, dtype='float64')
                df2[f"Bx"] = pd.Series(Bx, dtype='float64')
                df2[f"By"] = pd.Series(By, dtype='float64')
                df2[f"Bz"] = pd.Series(Bz, dtype='float64')
                df2[f"alpha"] = pd.Series(alpha, dtype='float64')
                df2[f"gamma"] = pd.Series(gamma, dtype='float64')
                df2[f"freq"] = pd.Series(freq, dtype='float64')
                df2[f"psi"] = pd.Series(psi, dtype='float64')
                df2[f"acoustic_frequency"] = pd.Series(acoustic_freq, dtype='float64')
                df2[f"sensor Bx"] = pd.Series(sensorBx, dtype='float64')
                df2[f"sensor By"] = pd.Series(sensorBy, dtype='float64')
                df2[f"sensor Bz"] = pd.Series(sensorBz, dtype='float64')
                df2.to_excel(writer, sheet_name=f"Magnetic Field", index=False)
    
    def update_halleffect_sensor(self, vals):
        sensorBx, sensorBy, sensorBz = vals
        self.ui.bxlabel.setText("Bx:               mT")
        self.ui.bylabel.setText("Bx:               mT")
        self.ui.bzlabel.setText("Bx:               mT")
        self.ui.bxlcdnum.display(sensorBx)
        self.ui.bylcdnum.display(sensorBy)
        self.ui.bzlcdnum.display(sensorBz)
        self.sensorBx = sensorBx
        self.sensorBy = sensorBy
        self.sensorBz = sensorBz


    def quickfieldleft(self):
        if self.ui.leftfieldbutton.isChecked():
            self.ui.upfieldbutton.setChecked(False)
            self.ui.downfieldbutton.setChecked(False)
            self.ui.rightfieldbutton.setChecked(False)
            self.ui.plusZbutton.setChecked(False)
            self.ui.minusZbutton.setChecked(False)
            self.Bx = -1
            self.By = 0
            self.Bz = 0
            self.apply_actions(True)
        else:
            self.apply_actions(False)

    def quickfieldright(self):
        if self.ui.rightfieldbutton.isChecked():
            self.ui.upfieldbutton.setChecked(False)
            self.ui.downfieldbutton.setChecked(False)
            self.ui.leftfieldbutton.setChecked(False)
            self.ui.plusZbutton.setChecked(False)
            self.ui.minusZbutton.setChecked(False)
            self.Bx = 1
            self.By = 0
            self.Bz = 0
            self.apply_actions(True)
        else:
            self.apply_actions(False)

    def quickfieldup(self):
        if self.ui.upfieldbutton.isChecked():
            self.ui.rightfieldbutton.setChecked(False)
            self.ui.downfieldbutton.setChecked(False)
            self.ui.leftfieldbutton.setChecked(False)
            self.ui.plusZbutton.setChecked(False)
            self.ui.minusZbutton.setChecked(False)
            self.By = 1
            self.Bx = 0
            self.Bz = 0
            self.apply_actions(True)
        else:
            self.apply_actions(False)
          
    def quickfielddown(self):
        if self.ui.downfieldbutton.isChecked():
            self.ui.upfieldbutton.setChecked(False)
            self.ui.rightfieldbutton.setChecked(False)
            self.ui.leftfieldbutton.setChecked(False)
            self.ui.plusZbutton.setChecked(False)
            self.ui.minusZbutton.setChecked(False)
            self.By = -1
            self.Bx = 0
            self.Bz = 0
            self.apply_actions(True)
        else:
            self.apply_actions(False)

    def quickfieldplusZ(self):
        if self.ui.plusZbutton.isChecked():
            self.ui.upfieldbutton.setChecked(False)
            self.ui.rightfieldbutton.setChecked(False)
            self.ui.leftfieldbutton.setChecked(False)
            self.ui.minusZbutton.setChecked(False)
            self.ui.downfieldbutton.setChecked(False)
            self.Bz = 1
            self.By = 0
            self.Bx = 0
            self.apply_actions(True)
        else:
            self.apply_actions(False)

    def quickfieldminusZ(self):
        if self.ui.minusZbutton.isChecked():
            self.ui.upfieldbutton.setChecked(False)
            self.ui.rightfieldbutton.setChecked(False)
            self.ui.leftfieldbutton.setChecked(False)
            self.ui.plusZbutton.setChecked(False)
            self.ui.downfieldbutton.setChecked(False)
            self.Bz = -1
            self.By = 0
            self.Bx = 0
            self.apply_actions(True)
        else:
            self.apply_actions(False)
         
        
    def resetparams(self):
        self.ui.maskthreshbox.setValue(128)
        self.ui.maskdilationbox.setValue(0)
        self.ui.croplengthbox.setValue(40)
        self.ui.memorybox.setValue(15)
        self.ui.RRTtreesizebox.setValue(25)
        self.ui.arrivalthreshbox.setValue(15)
        self.ui.gammadial.setSliderPosition(90)
        self.ui.psidial.setSliderPosition(90)
        self.ui.magneticfrequencydial.setSliderPosition(10)
        self.ui.acousticfreq_spinBox.setValue(1000000)
        self.ui.objectivebox.setValue(10)
        self.ui.exposurebox.setValue(5000)
        self.ui.maskblurbox.setValue(0)

    def resizeEvent(self, event):
        windowsize = event.size()
        self.window_width = windowsize.width()
        self.window_height = windowsize.height()
        self.resize_widgets()
 
    def resize_widgets(self):
        self.display_height = self.window_height*self.displayheightratio #keep this fixed, changed the width dpending on the aspect ratio
        self.framesliderheight = self.window_height*self.framesliderheightratio
        self.textheight = self.window_height*self.textheightratio
        #self.tabheight = self.window_height*self.tabheightratio

        self.display_width = int(self.display_height * self.aspectratio)

        self.ui.VideoFeedLabel.setGeometry(QtCore.QRect(10,  5,                       self.display_width,     self.display_height))
        self.ui.frameslider.setGeometry(QtCore.QRect(10,    self.display_height+12,   self.display_width,     self.framesliderheight))
        self.ui.plainTextEdit.setGeometry(QtCore.QRect(10,  self.display_height+20+self.framesliderheight,   self.display_width,     self.textheight))

        #self.ui.tabWidget.setGeometry(QtCore.QRect(12,  6,  260 ,     self.tabheight))

    def wheelEvent(self, event: QWheelEvent):
        # Get the scroll amount (event.angleDelta().y()) and the scroll orientation (event.angleDelta().x())
        if self.cap is not None:
            scroll_amount = event.angleDelta().y()
            if scroll_amount > 1:
                del self.tracker.robot_list[:]
                del self.magnetic_field_list[:]
                self.apply_actions(False)

    def closeEvent(self, event):
        """
        called when x button is pressed
        """
        
        if self.cap is not None:
            self.tracker.stop()
        self.simulator.stop()
        self.apply_actions(False)
        self.halleffect.stop()
        self.arduino.close()
