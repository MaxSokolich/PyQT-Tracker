
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


class control_widgets(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.mainwindow = parent  # Store a reference to the mainwindow app instance