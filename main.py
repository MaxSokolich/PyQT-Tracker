
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
from classes.gui_functions import MainWindow

# issues mask calcuation so expesnive. if not enough remove ndlabels part too
# i can also prolly only calculte one mask once instead pf having a display and a control
# add zoom feature?
# use middle mouse button to clear robot
# try blur thing

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
