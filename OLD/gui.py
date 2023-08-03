from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets, QtGui, QtCore
import cv2
import os
from os.path import expanduser

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

from tracking_widgets_class import tracker_widgets



class App(QWidget):
    positionChanged = QtCore.pyqtSignal(QtCore.QPoint)

    def __init__(self):
        super().__init__()
        
        
        self.setWindowTitle("Tracker")

        #true image shape
        self.video_width = 0 
        self.video_height = 0

        #dimensions i want to convert to 
        self.display_width = 1330
        self.display_height = 700 #keep this fixed, changed the width dpending on the aspect ratio

        #app h and w
        self.window_width = 1600
        self.window_height = 780
        self.resize(self.window_width, self.window_height)
        
       
        self.videopath = 0
        self.cap = None
        self.tracker = None

        #create widget tabs
        self.tabWidget = QtWidgets.QTabWidget(self)
        self.tabWidget.setGeometry(QtCore.QRect(5, 0, 210, self.window_height))
        self.tabWidget.setObjectName("tabWidget")
    


        self.tracker_tab = tracker_widgets(self)
        self.tracker_tab.setObjectName("tracker_tab")
        self.tracker_tab.setStyleSheet("QTabBar {font: bold 9pt;}")
        self.tabWidget.setStyleSheet(2)                     
        self.tabWidget.addTab(self.tracker_tab, "Tracking")



        self.control_tab = QtWidgets.QWidget()
        self.control_tab.setObjectName("control_tab")
        self.tabWidget.addTab(self.control_tab, "Control")





        self.frameslider = QtWidgets.QSlider(self)
        self.frameslider.setGeometry(QtCore.QRect(220, 20, self.display_width, 30))
        self.frameslider.setMinimum(0)
        self.frameslider.setMaximum(100)
        self.frameslider.setSliderPosition(0)
        self.frameslider.setOrientation(QtCore.Qt.Horizontal)
        self.frameslider.setObjectName("frameslider")
        self.frameslider.tracking = True
        self.frameslider.valueChanged.connect(self.adjustframe)
       

        self.framelabel = QtWidgets.QLabel(self)
        self.framelabel.setGeometry(QtCore.QRect(220, 5, self.display_width, 20))
        self.framelabel.setObjectName("framelabel")
        self.framelabel.setText("Frame:")
        self.framelabel.setStyleSheet("color: rgb(0, 0, 0);"
                                        "font-family: Courier;"
                                        #"background-color: rgb(0, 255, 0);"
                                        #"border-style: outset;"
                                        #"border-width: 2px;"
                                        #"border-radius: 6px;"
                                        #"border-color: rgb(0, 255, 100);"
                                        "font: bold 12px;"
                                        "min-width: 1em;"
                                        "padding: 1px;")
   


        self.VideoFeedLabel = QtWidgets.QLabel(self)
        self.VideoFeedLabel.setGeometry(QtCore.QRect(220, 60, self.display_width, self.display_height))
        self.VideoFeedLabel.setAutoFillBackground(True)
        self.VideoFeedLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.VideoFeedLabel.setText("")
        self.VideoFeedLabel.setObjectName("VideoFeedLabel")
        self.VideoFeedLabel.setStyleSheet("background-color: rgb(0,0,0); border:2px solid rgb(255, 0, 0); ")
        self.VideoFeedLabel.setMouseTracking(True)
        self.VideoFeedLabel.installEventFilter(self)



        





    def adjustframe(self):
        if self.videopath != 0:
            self.tracker.framenum = self.frameslider.value()
            self.framelabel.setText("Frame:"+str(self.tracker.framenum))




    def eventFilter(self, object, event):
        if object is self.VideoFeedLabel: 
            #if event.type() == QtCore.QEvent.MouseMove:
            #    self.positionChanged.emit(event.pos())
            #    pos = event.pos()
            #    print(pos)
                #Robot["pos"] = [pos.x(),pos.y()]


            if self.cap is not None:
                if event.type() == QtCore.QEvent.MouseButtonPress:
                    if event.buttons() == QtCore.Qt.LeftButton:
                    
                        self.positionChanged.emit(event.pos())
                        pos = event.pos()

                        #need a way to convert the video position of mouse to the actually coordinate in the window
                        newx = int(pos.x() * (self.video_width / self.display_width)) 
                        newy = int(pos.y() * (self.video_height / self.display_height))

                        #generate original bounding box
                        x_1 = int(newx - self.tracker.crop_length  / 2)
                        y_1 = int(newy - self.tracker.crop_length  / 2)
                        w = self.tracker.crop_length
                        h = self.tracker.crop_length

                        robot = Robot()  # create robot instance
                        
                        robot.add_frame(self.tracker.framenum)
                        robot.add_time(0)
                        robot.add_position([newx,newy])
                        robot.add_velocity([0,0])
                        robot.add_crop([x_1, y_1, w, h])
                        robot.add_area(0)
                        robot.add_blur(0)
                        
                        
                        self.tracker.robot_list.append(robot)
               
                    if event.buttons() == QtCore.Qt.RightButton:
                    
                        #self.positionChanged.emit(event.pos())
                        #pos = event.pos()
                        del self.tracker.robot_list[:]
                        
        return super().eventFilter(object, event)

        
            
    
if __name__=="__main__":
    app = QApplication(sys.argv)
    a = App()
    a.show()
    sys.exit(app.exec_())