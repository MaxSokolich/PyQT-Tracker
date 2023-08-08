
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
from classes.gui_functions import MainWindow

# try blur thing z
#cv2.CAP_PROP_FRAME_COUN not on easypyspin
#stop acoustic print and add reset button coustic [param]
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
