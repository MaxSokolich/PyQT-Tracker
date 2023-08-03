from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets, QtGui, QtCore
import cv2
import os
from os.path import expanduser
from tracker_class import VideoThread
from robot_class import Robot
import pandas as pd
from datetime import datetime
import sys
from PyQt5.QtWidgets import QApplication
import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy import ndimage 
import time


class tracker_widgets(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.mainwindow = parent  # Store a reference to the mainwindow app instance

        self.choosevideobutton = QtWidgets.QPushButton(self)
        self.choosevideobutton.setGeometry(QtCore.QRect(20, 0, 160, 25))
        self.choosevideobutton.setObjectName("choosevideobutton")
        self.choosevideobutton.setText("Choose Video")
        self.choosevideobutton.clicked.connect(self.selectFile)
        self.choosevideobutton.setStyleSheet('''
            QPushButton {
                color: rgb(255, 255, 255);
                background-color: rgb(0, 0, 0);
                border-style: outset;
                border-width: 2px;
                border-radius: 10px;
                border-color: rgb(0, 0, 0);
                font: bold 12px;
                min-width: 1em;
                padding: 1px;
            }
            QPushButton:hover {
                background-color: rgb(100, 100, 100);
                color: rgb(255, 255, 255);
                border-color: rgb(100, 100, 100);
            
            
            }
          
        ''')



        self.trackbutton = QtWidgets.QPushButton("Toggle",self)
        self.trackbutton.setGeometry(QtCore.QRect(20, 30, 160, 35))
        self.trackbutton.setObjectName("trackbutton")
        self.trackbutton.setText("Track")
        self.trackbutton.setCheckable(True)
        self.trackbutton.clicked.connect(self.track)
        self.trackbutton.setStyleSheet('''
            QPushButton {
                color: rgb(255, 255, 255);
                background-color: rgb(0, 0, 255);
                border-style: outset;
                border-width: 3px;
                border-radius: 10px;
                border-color: rgb(0, 0, 255);
                font: bold 16px;
                min-width: 1em;
                padding: 6px;
            }
      
            QPushButton:checked {
                color: rgb(255, 255, 255);
                background-color: rgb(255, 0, 0);
                border-style: inset;
                border-width: 3px;
                border-radius: 10px;
                border-color: rgb(255, 0, 0);
                font: bold 16px;
                min-width: 1em;
               
            }
            QPushButton:hover {
                background-color: rgb(100, 100, 100);
                color: rgb(255, 255, 255);
                border-color: rgb(100, 100, 100);
                padding-left: 5px;
                padding-top: 5px;
            }
         
            
            
        ''')


        self.pausebutton = QtWidgets.QPushButton("Toggle", self)
        self.pausebutton.setGeometry(QtCore.QRect(20, 70, 160, 20))
        self.pausebutton.setObjectName("pausebutton")
        self.pausebutton.setText("Pause")
        self.pausebutton.setCheckable(True)
        self.pausebutton.clicked.connect(self.pause)
        self.pausebutton.hide()
        self.pausebutton.setStyleSheet('''
            QPushButton {
                color: rgb(255, 255, 255);
                background-color: rgb(150, 0, 0);
                border-style: outset;
                border-width: 3px;
                border-radius: 10px;
                border-color: rgb(150, 0, 0);
                font: bold 12px;
                min-width: 1em;
                padding: 1px;
            }
            QPushButton:checked {
                color: rgb(255, 255, 255);
                background-color: rgb(0, 0, 150);
                border-style: inset;
                border-width: 3px;
                border-radius: 10px;
                border-color: rgb(0, 0, 150);
                font: bold 12px;
                min-width: 1em;
                padding: 1px;
            }
            QPushButton:hover {
                background-color: rgb(100, 100, 100);
                color: rgb(255, 255, 255);
                border-color: rgb(100, 100, 100);
                padding-left: 2px;
                padding-top: 2px;
            }
            
            
        ''')


        self.rightbutton = QtWidgets.QToolButton(self)
        self.rightbutton.setGeometry(QtCore.QRect(105, 100, 60, 20))
        self.rightbutton.setArrowType(Qt.RightArrow)
        self.rightbutton.setAutoRepeat(True)
        #self.rightbutton.setAutoRepeatDelay(200)
        #self.rightbutton.setAutoRepeatInterval(50)
        self.rightbutton.clicked.connect(self.frameright)
        self.rightbutton.hide()
        self.rightbutton.setStyleSheet('''
            QToolButton {
                color: rgb(255, 255, 255);
                background-color: rgb(0, 0, 0);
                border-style: outset;
                border-width: px;
                border-radius: 2px;
                border-color: rgb(0, 0, 0);
                font: bold 16px;
                min-width: 1em;
                padding: 1px;
            }
            QToolButton:hover {
                background-color: rgb(100, 100, 100);
                color: rgb(255, 255, 255);
                border-color: rgb(100, 100, 100);
            }
            QToolButton:pressed {
                background-color: rgb(100, 100, 100);
                border: 2px solid rgb(100, 100, 100);
                border-style: inset;
                padding-left: 5px;
                padding-top: 5px;
            }
          
            
        ''')


        self.leftbutton = QtWidgets.QToolButton(self)
        self.leftbutton.setGeometry(QtCore.QRect(35, 100, 60, 20))
        self.leftbutton.setArrowType(Qt.LeftArrow)
        self.leftbutton.setAutoRepeat(True)
        #self.leftbutton.setAutoRepeatDelay(200)
        #self.leftbutton.setAutoRepeatInterval(50)
        self.leftbutton.clicked.connect(self.frameleft)
        self.leftbutton.hide()
        self.leftbutton.setStyleSheet('''
            QToolButton {
                color: rgb(255, 255, 255);
                background-color: rgb(0, 0, 0);
                border-style: outset;
                border-width: px;
                border-radius: 2px;
                border-color: rgb(0, 0, 0);
                font: bold 16px;
                min-width: 1em;
                padding: 1px;
            }
            QToolButton:hover {
                background-color: rgb(100, 100, 100);
                color: rgb(255, 255, 255);
                border-color: rgb(100, 100, 100);
            }
            QToolButton:pressed {
                background-color: rgb(100, 100, 100);
                border: 2px solid rgb(100, 100, 100);
                border-style: inset;
                padding-left: 5px;
                padding-top: 5px;
            }
          
            
        ''')
        

     

        self.maskbutton = QtWidgets.QPushButton("Toggle",self)
        self.maskbutton.setGeometry(QtCore.QRect(20, 130, 160, 20))
        self.maskbutton.setObjectName("maskbutton")
        self.maskbutton.setText("Mask")
        self.maskbutton.setCheckable(True)
        self.maskbutton.clicked.connect(self.showmask)
        self.maskbutton.hide()
        self.maskbutton.setStyleSheet('''
            QPushButton {
                color: rgb(255, 255, 255);
                background-color: rgb(0, 0, 0);
                border-style: outset;
                border-width: 2px;
                border-radius: 10px;
                border-color: rgb(0, 0, 0);
                font: bold 10px;
                min-width: 1em;
                padding: 1px;
            }
            QPushButton:hover {
                background-color: rgb(100, 100, 100);
                color: rgb(0, 0, 0);
                border-style: inset;
            }
        ''')
        


        self.maskinvert_checkBox = QtWidgets.QCheckBox(self)
        self.maskinvert_checkBox.setGeometry(QtCore.QRect(20, 160, 25, 25))
        self.maskinvert_checkBox.setObjectName("maskinvert_checkBox")
        self.maskinvert_checkBox.setChecked(True)
        self.maskinvert_checkBox.toggled.connect(self.invertmaskcommand)
      
    
        self.maskinvert_label = QtWidgets.QLabel(self)
        self.maskinvert_label.setGeometry(QtCore.QRect(50, 160, 160, 20))
        self.maskinvert_label.setObjectName("maskinvert_label")
        self.maskinvert_label.setText("Invert Mask: False")
        self.maskinvert_label.setStyleSheet("color: rgb(0, 0, 0);"
                                        #"background-color: rgb(0, 255, 0);"
                                        #"border-style: outset;"
                                        #"border-width: 2px;"
                                        #"border-radius: 6px;"
                                        #"border-color: rgb(0, 255, 100);"
                                        "font: bold 12px;"
                                        "min-width: 1em;"
                                        "padding: 1px;")





        self.masksigmalabel = QtWidgets.QLabel(self)
        self.masksigmalabel.setGeometry(QtCore.QRect(20, 185, 160, 20))
        self.masksigmalabel.setObjectName("masksigmalabel")
        self.masksigmalabel.setText("Mask Sigma: 7")
        self.masksigmalabel.setStyleSheet("color: rgb(0, 0, 0);"
                                        #"background-color: rgb(0, 255, 0);"
                                        #"border-style: outset;"
                                        #"border-width: 2px;"
                                        #"border-radius: 6px;"
                                        #"border-color: rgb(0, 255, 100);"
                                        "font: bold 12px;"
                                        "min-width: 1em;"
                                        "padding: 1px;")

        self.masksigmaslider = QtWidgets.QSlider(self)
        self.masksigmaslider.setGeometry(QtCore.QRect(20, 205, 160, 30))
        self.masksigmaslider.setMinimum(0)
        self.masksigmaslider.setMaximum(30)
        self.masksigmaslider.setSliderPosition(7)
        self.masksigmaslider.setOrientation(QtCore.Qt.Horizontal)
        self.masksigmaslider.setObjectName("masksigmaslider")
        self.masksigmaslider.valueChanged.connect(self.get_masksigma)
        

        self.croplengthlabel = QtWidgets.QLabel(self)
        self.croplengthlabel.setGeometry(QtCore.QRect(20, 235, 160, 20))
        self.croplengthlabel.setObjectName("croplengthlabel")
        self.croplengthlabel.setText("Crop Length: 40")
        self.croplengthlabel.setStyleSheet("color: rgb(0, 0, 0);"
                                        #"background-color: rgb(0, 255, 0);"
                                        #"border-style: outset;"
                                        #"border-width: 2px;"
                                        #"border-radius: 6px;"
                                        #"border-color: rgb(0, 255, 100);"
                                        "font: bold 12px;"
                                        "min-width: 1em;"
                                        "padding: 1px;")

        self.croplengthslider = QtWidgets.QSlider(self)
        self.croplengthslider.setGeometry(QtCore.QRect(20, 255, 160, 30))
        self.croplengthslider.setMinimum(5)
        self.croplengthslider.setMaximum(200)
        self.croplengthslider.setSliderPosition(40)
        self.croplengthslider.setOrientation(QtCore.Qt.Horizontal)
        self.croplengthslider.setObjectName("croplengthslider")
        self.croplengthslider.valueChanged.connect(self.get_croplength)

        self.savedatabutton = QtWidgets.QPushButton("Toggle",self)
        self.savedatabutton.setGeometry(QtCore.QRect(20, 290, 160, 30))
        self.savedatabutton.setObjectName("savedatabutton")
        self.savedatabutton.setText("Save Data")
        self.savedatabutton.setCheckable(True)
        self.savedatabutton.clicked.connect(self.savedata)
        self.savedatabutton.setStyleSheet('''
            QPushButton {
                color: rgb(0, 0, 0);
                background-color: rgb(255, 255, 0);
                border-style: outset;
                border-width: 3px;
                border-radius: 6px;
                border-color: rgb(255, 255, 100);
                font: bold 12px;
                min-width: 1em;
                padding: 1px;
            }
            QPushButton:hover {
                background-color: rgb(255, 255, 200);
                color: rgb(0, 0, 0);
            }
            QPushButton:pressed {
                background-color: red;
                border: 2px solid red;
                padding-left: 5px;
                padding-top: 5px;
                border-style: inset;
                }
                        
        ''')


        self.robotarealabel = QtWidgets.QLabel(self)
        self.robotarealabel.setGeometry(QtCore.QRect(20, 320, 160, 20))
        self.robotarealabel.setObjectName("robotarealabel")
        self.robotarealabel.setText("Area:")
        self.robotarealabel.setStyleSheet("color: rgb(0, 0, 0);"
                                        #"background-color: rgb(0, 255, 0);"
                                        #"border-style: outset;"
                                        #"border-width: 2px;"
                                        #"border-radius: 6px;"
                                        #"border-color: rgb(0, 255, 100);"
                                        "font: bold 12px;"
                                        "min-width: 1em;"
                                        "padding: 1px;")

        self.robotvelocitylabel = QtWidgets.QLabel(self)
        self.robotvelocitylabel.setGeometry(QtCore.QRect(20, 340, 160, 20))
        self.robotvelocitylabel.setObjectName("robotvelocitylabel")
        self.robotvelocitylabel.setText("Velocity:")
        self.robotvelocitylabel.setStyleSheet("color: rgb(0, 0, 0);"
                                        #"background-color: rgb(0, 255, 0);"
                                        #"border-style: outset;"
                                        #"border-width: 2px;"
                                        #"border-radius: 6px;"
                                        #"border-color: rgb(0, 255, 100);"
                                        "font: bold 12px;"
                                        "min-width: 1em;"
                                        "padding: 1px;")

        self.robotblurlabel = QtWidgets.QLabel(self)
        self.robotblurlabel.setGeometry(QtCore.QRect(20, 360, 160, 20))
        self.robotblurlabel.setObjectName("robotblurlabel")
        self.robotblurlabel.setText("Blur:")
        self.robotblurlabel.setStyleSheet("color: rgb(0, 0, 0);"
                                        #"background-color: rgb(0, 255, 0);"
                                        #"border-style: outset;"
                                        #"border-width: 2px;"
                                        #"border-radius: 6px;"
                                        #"border-color: rgb(0, 255, 100);"
                                        "font: bold 12px;"
                                        "min-width: 1em;"
                                        "padding: 1px;")


        self.CroppedVideoFeedLabel = QtWidgets.QLabel(self)
        self.CroppedVideoFeedLabel.setGeometry(QtCore.QRect(0, 380, 200, 200))
        self.CroppedVideoFeedLabel.setAutoFillBackground(True)
        self.CroppedVideoFeedLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CroppedVideoFeedLabel.setText("")
        self.CroppedVideoFeedLabel.setObjectName("CroppedVideoFeedLabel")
        self.CroppedVideoFeedLabel.setStyleSheet("background-color: rgb(0,0,0); border:2px solid rgb(255, 0, 0); ")



        









    def selectFile(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.ReadOnly
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;Text Files (*.txt);;Python Files (*.py)", options=options)

        if file_path:
            self.mainwindow.videopath = file_path
            file_info = QtCore.QFileInfo(file_path)
            file_name = file_info.fileName()
            print(file_path, file_name)
            self.choosevideobutton.setText(file_name)
        else:
            self.mainwindow.videopath = 0
            self.choosevideobutton.setText(str(0))
        
        


        
    def update_image(self, frame):
        """Updates the image_label with a new opencv image"""
        
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.mainwindow.display_width, self.mainwindow.display_height, Qt.KeepAspectRatio)
        qt_img = QPixmap.fromImage(p)    
        
        #update frame slider too
        self.mainwindow.framelabel.setText("Frame:"+str(self.mainwindow.tracker.framenum))
        self.mainwindow.frameslider.setSliderPosition(self.mainwindow.tracker.framenum)

        #also update robot info
        if len(self.mainwindow.tracker.robot_list) > 0:
            self.robotarealabel.setText("Area: {0:.2f} px^2".format(self.mainwindow.tracker.robot_list[-1].avg_area))
            self.robotvelocitylabel.setText("Vx: {0:.2f}, Vy: {0:.2f} px/f".format(self.mainwindow.tracker.robot_list[-1].velocity_list[-1][0], self.mainwindow.tracker.robot_list[-1].velocity_list[-1][1]  )  )
            self.robotblurlabel.setText("Blur: {0:.2f} units".format(self.mainwindow.tracker.robot_list[-1].blur_list[-1]))
        
  
        self.mainwindow.VideoFeedLabel.setPixmap(qt_img)
        

    
    def update_croppedimage(self, frame):
        """Updates the cropped image_label with a new cropped opencv image"""
        
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(200, 200, Qt.KeepAspectRatio)
        qt_cimg = QPixmap.fromImage(p)
        self.CroppedVideoFeedLabel.setPixmap(qt_cimg)
        


    
    def track(self):
        if self.mainwindow.videopath is not None:
            if self.trackbutton.isChecked():
                

                #start video thread
                self.pausebutton.show()
                self.leftbutton.show()
                self.rightbutton.show()
                self.maskbutton.show()

                #need to resize the window in order to maintain proper aspect ratios
                self.mainwindow.cap = cv2.VideoCapture(self.mainwindow.videopath)
                self.mainwindow.video_width = int(self.mainwindow.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                self.mainwindow.video_height = int(self.mainwindow.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                self.totalnumframes = int(self.mainwindow.cap.get(cv2.CAP_PROP_FRAME_COUNT))

                self.mainwindow.display_width = int(self.mainwindow.display_height * (self.mainwindow.video_width / self.mainwindow.video_height))
                self.mainwindow.VideoFeedLabel.setGeometry(QtCore.QRect(220, 60, self.mainwindow.display_width, self.mainwindow.display_height))
                self.mainwindow.VideoFeedLabel.setStyleSheet("border:2px solid rgb(0, 255, 0); ")
                self.CroppedVideoFeedLabel.setStyleSheet("border:2px solid rgb(0, 255, 0); ")
                


                self.mainwindow.frameslider.setGeometry(QtCore.QRect(220, 20, self.mainwindow.display_width, 30))
                self.mainwindow.frameslider.setMaximum(self.totalnumframes)
            

                self.mainwindow.tracker = VideoThread(self.mainwindow.cap)
                self.mainwindow.tracker.change_pixmap_signal.connect(self.update_image)
                self.mainwindow.tracker.cropped_frame_signal.connect(self.update_croppedimage)
                self.mainwindow.tracker.start()
                
                self.trackbutton.setText("Stop")
                
                if self.mainwindow.videopath == 0:
                    self.pausebutton.hide()
                    self.leftbutton.hide()
                    self.rightbutton.hide()
         
                
        
            else:
                self.mainwindow.VideoFeedLabel.setStyleSheet("background-color: rgb(0,0,0); border:2px solid rgb(255, 0, 0); ")
                self.CroppedVideoFeedLabel.setStyleSheet("background-color: rgb(0,0,0); border:2px solid rgb(255, 0, 0); ")
         
                
                if self.mainwindow.cap is not None:
                    self.trackbutton.setText("Track")
                    self.mainwindow.tracker.stop()
                    
                   
                    #also reset pause button
                    self.pausebutton.setChecked(False)
                    self.pausebutton.setText("Pause")

                    self.pausebutton.hide()
                    self.leftbutton.hide()
                    self.rightbutton.hide()
                    self.maskbutton.hide()
                    

                

        else:
            self.trackbutton.setText("No Video")
            
    def showmask(self):
        if self.mainwindow.cap is not None:
            if self.maskbutton.isChecked():
                self.maskbutton.setText("Original")
                self.mainwindow.tracker.mask_flag = True
                
            else:
                self.maskbutton.setText("Mask")
                self.mainwindow.tracker.mask_flag = False
                
           
    def invertmaskcommand(self):
        if self.mainwindow.cap is not None:
            self.maskinvert_label.setText("Invert Mask: " + str(self.maskinvert_checkBox.isChecked()))
            self.mainwindow.tracker.maskinvert = self.maskinvert_checkBox.isChecked()

    def pause(self):
        if self.mainwindow.videopath != 0:
            if self.pausebutton.isChecked():
                self.mainwindow.tracker._play_flag = False
                self.pausebutton.setText("Play")
              
            else:#play
                self.mainwindow.tracker._play_flag = True
                self.pausebutton.setText("Pause")
                

                
    
    def adjustframe(self):
        if self.mainwindow.videopath != 0:
            self.mainwindow.tracker.framenum = self.mainwindow.frameslider.value()
            self.mainwindow.framelabel.setText("Frame:"+str(self.mainwindow.tracker.framenum))
        
            


    def frameright(self):
        if self.mainwindow.videopath != 0:
            self.mainwindow.tracker.framenum+=1
            
            self.mainwindow.frameslider.setSliderPosition(self.mainwindow.tracker.framenum)
            self.mainwindow.framelabel.setText("Frame:"+str(self.mainwindow.tracker.framenum))



    def frameleft(self):
        if self.mainwindow.videopath != 0:
            self.mainwindow.tracker.framenum-=1
            self.mainwindow.frameslider.setSliderPosition(self.mainwindow.tracker.framenum)
            self.mainwindow.framelabel.setText("Frame:"+str(self.mainwindow.tracker.framenum))
    
    
    def get_masksigma(self):
        sigma = self.masksigmaslider.value() /10
        self.masksigmalabel.setText("Mask Sigma: {}".format(sigma) )
        if self.mainwindow.cap is not None:        
            self.mainwindow.tracker.mask_sigma = sigma
        


    def get_croplength(self): 
        crop_length = self.croplengthslider.value()
        if crop_length %2 ==0:
            self.croplengthlabel.setText("Crop Length: {}".format(crop_length) )
            if self.mainwindow.cap is not None:
                self.mainwindow.tracker.crop_length = crop_length



    def savedata(self):
        #create folder in homerdiractory of user
        home_dir = expanduser("~")
        new_dir_name = "Tracking Data"
        desktop_path = os.path.join(home_dir, "Desktop")
        new_dir_path = os.path.join(desktop_path, new_dir_name)
        if not os.path.exists(new_dir_path):
            os.makedirs(new_dir_path)
        
        
        if self.mainwindow.cap is not None and len(self.mainwindow.tracker.robot_list)>0:      
            robot_dictionary = []
            for bot in self.mainwindow.tracker.robot_list:
                robot_dictionary.append(bot.as_dict())
            #create dictionarys from the robot class
            file_path  = os.path.join(new_dir_path, str(datetime.now())+".xlsx")

            
            with pd.ExcelWriter(file_path) as writer:
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
                                x_coords, y_coords = zip(*value)
                                df[f"{key}_X"] = pd.Series(x_coords, dtype='float64')
                                df[f"{key}_Y"] = pd.Series(y_coords, dtype='float64')
                        
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

                        elif key == "Magnetic Field":
                            if len(value) > 0:
                                for MFkey, MFvalue in value.items():
                                    df[f"{MFkey}"] = pd.Series(MFvalue, dtype='float64')

                    # Write the DataFrame to a separate sheet with sheet name "Sheet_<idx>"
                    df.to_excel(writer, sheet_name=f"Robot_{idx+1}", index=False)
                