
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
from classes.gui_functions import MainWindow


#Convert blur into z position
#remeasure pix2metric conversion
#video record not working great made it a seperate thread
#simulation also bottlenecking maybe sperate thread too
#seperate tabs. tracker on left, contrl on right
#

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
