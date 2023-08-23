
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
from classes.gui_functions import MainWindow


# Convert blur into z position
# put RRT trajectory in seperate thead
# fix zoom feature and maybe make it continous


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
