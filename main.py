
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
from classes.gui_functions import MainWindow


# Convert blur into z position
# put RRT trajectory in seperate thead
# ideally refactor the actions output function, not sure the best way to do it though
# add joystick when camera is off. see above
# calibrate x and y z coils by adding a calbration value
# add a track all feature
# need to recode saving and recording data function. there are timing issues



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
