# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyQt_Magscope.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 860)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(5, 10, 215, 780))
        self.tabWidget.setStyleSheet("font-size: 15pt;  font-family: Courier;")
        self.tabWidget.setObjectName("tabWidget")
        self.tracking_tab = QtWidgets.QWidget()
        self.tracking_tab.setObjectName("tracking_tab")
        self.robotblurlabel = QtWidgets.QLabel(self.tracking_tab)
        self.robotblurlabel.setGeometry(QtCore.QRect(10, 490, 161, 20))
        self.robotblurlabel.setObjectName("robotblurlabel")
        self.rightbutton = QtWidgets.QToolButton(self.tracking_tab)
        self.rightbutton.setGeometry(QtCore.QRect(110, 140, 60, 21))
        self.rightbutton.setStyleSheet("QToolButton {\n"
"                color: rgb(255, 255, 255);\n"
"                background-color: rgb(0, 0, 0);\n"
"                border-style: outset;\n"
"                border-width: px;\n"
"                border-radius: 2px;\n"
"                border-color: rgb(0, 0, 0);\n"
"                font: bold 16px;\n"
"                min-width: 1em;\n"
"                padding: 1px;\n"
"            }\n"
"            QToolButton:hover {\n"
"                background-color: rgb(100, 100, 100);\n"
"                color: rgb(255, 255, 255);\n"
"                border-color: rgb(100, 100, 100);\n"
"            }\n"
"            QToolButton:pressed {\n"
"                background-color: rgb(100, 100, 100);\n"
"                border: 2px solid rgb(100, 100, 100);\n"
"                border-style: inset;\n"
"                padding-left: 5px;\n"
"                padding-top: 5px;\n"
"            }")
        self.rightbutton.setAutoRepeat(True)
        self.rightbutton.setAutoRepeatInterval(50)
        self.rightbutton.setArrowType(QtCore.Qt.RightArrow)
        self.rightbutton.setObjectName("rightbutton")
        self.choosevideobutton = QtWidgets.QPushButton(self.tracking_tab)
        self.choosevideobutton.setGeometry(QtCore.QRect(20, 0, 165, 25))
        self.choosevideobutton.setStyleSheet("     QPushButton {\n"
"                color: rgb(255, 255, 255);\n"
"                background-color: rgb(0, 0, 0);\n"
"                border-style: outset;\n"
"                border-width: 2px;\n"
"                border-radius: 10px;\n"
"                border-color: rgb(0, 0, 0);\n"
"                min-width: 1em;\n"
"                padding: 1px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: rgb(100, 100, 100);\n"
"                color: rgb(255, 255, 255);\n"
"                border-color: rgb(100, 100, 100);\n"
"            \n"
"            \n"
"            }")
        self.choosevideobutton.setObjectName("choosevideobutton")
        self.croplengthlabel = QtWidgets.QLabel(self.tracking_tab)
        self.croplengthlabel.setGeometry(QtCore.QRect(10, 290, 160, 20))
        self.croplengthlabel.setObjectName("croplengthlabel")
        self.pausebutton = QtWidgets.QPushButton(self.tracking_tab)
        self.pausebutton.setGeometry(QtCore.QRect(20, 110, 160, 20))
        self.pausebutton.setStyleSheet("QPushButton {\n"
"                color: rgb(255, 255, 255);\n"
"                background-color: rgb(150, 0, 0);\n"
"                border-style: outset;\n"
"                border-width: 3px;\n"
"                border-radius: 10px;\n"
"                border-color: rgb(150, 0, 0);\n"
"                min-width: 1em;\n"
"                padding: 1px;\n"
"            }\n"
"            QPushButton:checked {\n"
"                color: rgb(255, 255, 255);\n"
"                background-color: rgb(0, 0, 150);\n"
"                border-style: inset;\n"
"                border-width: 3px;\n"
"                border-radius: 10px;\n"
"                border-color: rgb(0, 0, 150);\n"
"                font: bold 12px;\n"
"                min-width: 1em;\n"
"                padding: 1px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: rgb(100, 100, 100);\n"
"                color: rgb(255, 255, 255);\n"
"                border-color: rgb(100, 100, 100);\n"
"                padding-left: 2px;\n"
"                padding-top: 2px;\n"
"            }")
        self.pausebutton.setCheckable(True)
        self.pausebutton.setObjectName("pausebutton")
        self.trackbutton = QtWidgets.QPushButton(self.tracking_tab)
        self.trackbutton.setGeometry(QtCore.QRect(20, 30, 160, 51))
        self.trackbutton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.trackbutton.setStyleSheet("QPushButton {\n"
"                color: rgb(255, 255, 255);\n"
"                background-color: rgb(0, 0, 255);\n"
"                border-style: outset;\n"
"                border-width: 3px;\n"
"                border-radius: 10px;\n"
"                border-color: rgb(0, 0, 255);\n"
"                min-width: 1em;\n"
"                padding: 6px;\n"
"            }\n"
"      \n"
"            QPushButton:checked {\n"
"                color: rgb(255, 255, 255);\n"
"                background-color: rgb(255, 0, 0);\n"
"                border-style: inset;\n"
"                border-width: 3px;\n"
"                border-radius: 10px;\n"
"                border-color: rgb(255, 0, 0);\n"
"                font: bold 16px;\n"
"                min-width: 1em;\n"
"               \n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: rgb(100, 100, 100);\n"
"                color: rgb(255, 255, 255);\n"
"                border-color: rgb(100, 100, 100);\n"
"                padding-left: 5px;\n"
"                padding-top: 5px;\n"
"            }")
        self.trackbutton.setCheckable(True)
        self.trackbutton.setObjectName("trackbutton")
        self.robotarealabel = QtWidgets.QLabel(self.tracking_tab)
        self.robotarealabel.setGeometry(QtCore.QRect(10, 450, 161, 20))
        self.robotarealabel.setObjectName("robotarealabel")
        self.maskinvert_checkBox = QtWidgets.QCheckBox(self.tracking_tab)
        self.maskinvert_checkBox.setGeometry(QtCore.QRect(10, 210, 191, 21))
        self.maskinvert_checkBox.setObjectName("maskinvert_checkBox")
        self.maskbutton = QtWidgets.QPushButton(self.tracking_tab)
        self.maskbutton.setGeometry(QtCore.QRect(20, 180, 161, 25))
        self.maskbutton.setStyleSheet("QPushButton {\n"
"                color: rgb(255, 255, 255);\n"
"                background-color: rgb(0, 0, 0);\n"
"                border-style: outset;\n"
"                border-width: 2px;\n"
"                border-radius: 10px;\n"
"                border-color: rgb(0, 0, 0);\n"
"                min-width: 1em;\n"
"                padding: 1px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: rgb(100, 100, 100);\n"
"                color: rgb(0, 0, 0);\n"
"                border-style: inset;\n"
"            }")
        self.maskbutton.setCheckable(True)
        self.maskbutton.setObjectName("maskbutton")
        self.CroppedVideoFeedLabel = QtWidgets.QLabel(self.tracking_tab)
        self.CroppedVideoFeedLabel.setGeometry(QtCore.QRect(5, 520, 200, 200))
        self.CroppedVideoFeedLabel.setStyleSheet("background-color: rgb(0,0,0); border:2px solid rgb(255, 0, 0); ")
        self.CroppedVideoFeedLabel.setText("")
        self.CroppedVideoFeedLabel.setObjectName("CroppedVideoFeedLabel")
        self.leftbutton = QtWidgets.QToolButton(self.tracking_tab)
        self.leftbutton.setGeometry(QtCore.QRect(30, 140, 60, 21))
        self.leftbutton.setStyleSheet("QToolButton {\n"
"                color: rgb(255, 255, 255);\n"
"                background-color: rgb(0, 0, 0);\n"
"                border-style: outset;\n"
"                border-width: px;\n"
"                border-radius: 2px;\n"
"                border-color: rgb(0, 0, 0);\n"
"                font: bold 16px;\n"
"                min-width: 1em;\n"
"                padding: 1px;\n"
"            }\n"
"            QToolButton:hover {\n"
"                background-color: rgb(100, 100, 100);\n"
"                color: rgb(255, 255, 255);\n"
"                border-color: rgb(100, 100, 100);\n"
"            }\n"
"            QToolButton:pressed {\n"
"                background-color: rgb(100, 100, 100);\n"
"                border: 2px solid rgb(100, 100, 100);\n"
"                border-style: inset;\n"
"                padding-left: 5px;\n"
"                padding-top: 5px;\n"
"            }")
        self.leftbutton.setAutoRepeat(True)
        self.leftbutton.setAutoRepeatInterval(50)
        self.leftbutton.setArrowType(QtCore.Qt.LeftArrow)
        self.leftbutton.setObjectName("leftbutton")
        self.savedatabutton = QtWidgets.QPushButton(self.tracking_tab)
        self.savedatabutton.setGeometry(QtCore.QRect(20, 350, 160, 41))
        self.savedatabutton.setStyleSheet("QPushButton {\n"
"                color: rgb(0, 0, 0);\n"
"                background-color: rgb(255, 255, 0);\n"
"                border-style: outset;\n"
"                border-width: 3px;\n"
"                border-radius: 10px;\n"
"                border-color: rgb(255, 255, 100);\n"
"                min-width: 1em;\n"
"                padding: 6px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: rgb(255, 255, 200);\n"
"                color: rgb(0, 0, 0);\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: red;\n"
"                border: 2px solid red;\n"
"                padding-left: 5px;\n"
"                padding-top: 5px;\n"
"                border-style: inset;\n"
"                }")
        self.savedatabutton.setCheckable(True)
        self.savedatabutton.setObjectName("savedatabutton")
        self.masksigmalabel = QtWidgets.QLabel(self.tracking_tab)
        self.masksigmalabel.setGeometry(QtCore.QRect(10, 240, 160, 20))
        self.masksigmalabel.setObjectName("masksigmalabel")
        self.croplengthslider = QtWidgets.QSlider(self.tracking_tab)
        self.croplengthslider.setGeometry(QtCore.QRect(10, 310, 180, 25))
        self.croplengthslider.setMinimum(5)
        self.croplengthslider.setMaximum(200)
        self.croplengthslider.setProperty("value", 40)
        self.croplengthslider.setSliderPosition(40)
        self.croplengthslider.setOrientation(QtCore.Qt.Horizontal)
        self.croplengthslider.setObjectName("croplengthslider")
        self.robotvelocitylabel = QtWidgets.QLabel(self.tracking_tab)
        self.robotvelocitylabel.setGeometry(QtCore.QRect(10, 470, 161, 20))
        self.robotvelocitylabel.setObjectName("robotvelocitylabel")
        self.masksigmaslider = QtWidgets.QSlider(self.tracking_tab)
        self.masksigmaslider.setGeometry(QtCore.QRect(10, 260, 180, 25))
        self.masksigmaslider.setMaximum(30)
        self.masksigmaslider.setSliderPosition(7)
        self.masksigmaslider.setOrientation(QtCore.Qt.Horizontal)
        self.masksigmaslider.setObjectName("masksigmaslider")
        self.framelabel = QtWidgets.QLabel(self.tracking_tab)
        self.framelabel.setGeometry(QtCore.QRect(50, 80, 121, 31))
        self.framelabel.setObjectName("framelabel")
        self.recordbutton = QtWidgets.QPushButton(self.tracking_tab)
        self.recordbutton.setGeometry(QtCore.QRect(40, 400, 111, 32))
        self.recordbutton.setStyleSheet("QPushButton {\n"
"                color: rgb(255, 255, 255);\n"
"                background-color: rgb(0, 0, 0);\n"
"                border-style: outset;\n"
"                border-width: 3px;\n"
"                border-radius: 10px;\n"
"                border-color: rgb(0, 0, 0);\n"
"                min-width: 1em;\n"
"                padding: 6px;\n"
"            }\n"
"      \n"
"            QPushButton:checked {\n"
"                color: rgb(255, 255, 255);\n"
"                background-color: rgb(255, 0, 0);\n"
"                border-style: inset;\n"
"                border-width: 3px;\n"
"                border-radius: 10px;\n"
"                border-color: rgb(255, 0, 0);\n"
"                font: bold 16px;\n"
"                min-width: 1em;\n"
"               \n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: rgb(100, 100, 100);\n"
"                color: rgb(255, 255, 255);\n"
"                border-color: rgb(100, 100, 100);\n"
"                padding-left: 5px;\n"
"                padding-top: 5px;\n"
"            }")
        self.recordbutton.setCheckable(True)
        self.recordbutton.setObjectName("recordbutton")
        self.tabWidget.addTab(self.tracking_tab, "")
        self.control_tab = QtWidgets.QWidget()
        self.control_tab.setObjectName("control_tab")
        self.controlbutton = QtWidgets.QPushButton(self.control_tab)
        self.controlbutton.setGeometry(QtCore.QRect(20, 10, 160, 51))
        self.controlbutton.setStyleSheet("QPushButton {\n"
"                color: rgb(255, 255, 255);\n"
"                background-color: rgb(0, 0, 255);\n"
"                border-style: outset;\n"
"                border-width: 3px;\n"
"                border-radius: 10px;\n"
"                border-color: rgb(0, 0, 255);\n"
"                min-width: 1em;\n"
"                padding: 6px;\n"
"            }\n"
"      \n"
"            QPushButton:checked {\n"
"                color: rgb(255, 255, 255);\n"
"                background-color: rgb(255, 0, 0);\n"
"                border-style: inset;\n"
"                border-width: 3px;\n"
"                border-radius: 10px;\n"
"                border-color: rgb(255, 0, 0);\n"
"                font: bold 16px;\n"
"                min-width: 1em;\n"
"               \n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: rgb(100, 100, 100);\n"
"                color: rgb(255, 255, 255);\n"
"                border-color: rgb(100, 100, 100);\n"
"                padding-left: 5px;\n"
"                padding-top: 5px;\n"
"            }")
        self.controlbutton.setCheckable(True)
        self.controlbutton.setObjectName("controlbutton")
        self.controlautoradio = QtWidgets.QRadioButton(self.control_tab)
        self.controlautoradio.setGeometry(QtCore.QRect(90, 70, 111, 21))
        self.controlautoradio.setObjectName("controlautoradio")
        self.controlmanualradio = QtWidgets.QRadioButton(self.control_tab)
        self.controlmanualradio.setGeometry(QtCore.QRect(10, 70, 81, 20))
        self.controlmanualradio.setObjectName("controlmanualradio")
        self.gammaslider = QtWidgets.QSlider(self.control_tab)
        self.gammaslider.setGeometry(QtCore.QRect(10, 324, 180, 31))
        self.gammaslider.setOrientation(QtCore.Qt.Horizontal)
        self.gammaslider.setObjectName("gammaslider")
        self.arrivalthreshslider = QtWidgets.QSlider(self.control_tab)
        self.arrivalthreshslider.setGeometry(QtCore.QRect(10, 274, 180, 31))
        self.arrivalthreshslider.setOrientation(QtCore.Qt.Horizontal)
        self.arrivalthreshslider.setObjectName("arrivalthreshslider")
        self.arrivalthreshlabel = QtWidgets.QLabel(self.control_tab)
        self.arrivalthreshlabel.setGeometry(QtCore.QRect(10, 255, 201, 21))
        self.arrivalthreshlabel.setObjectName("arrivalthreshlabel")
        self.gammalabel = QtWidgets.QLabel(self.control_tab)
        self.gammalabel.setGeometry(QtCore.QRect(10, 305, 201, 20))
        self.gammalabel.setObjectName("gammalabel")
        self.rollingfrequencyslider = QtWidgets.QSlider(self.control_tab)
        self.rollingfrequencyslider.setGeometry(QtCore.QRect(10, 374, 180, 31))
        self.rollingfrequencyslider.setOrientation(QtCore.Qt.Horizontal)
        self.rollingfrequencyslider.setObjectName("rollingfrequencyslider")
        self.rollingfrequencylabel = QtWidgets.QLabel(self.control_tab)
        self.rollingfrequencylabel.setGeometry(QtCore.QRect(10, 355, 201, 21))
        self.rollingfrequencylabel.setObjectName("rollingfrequencylabel")
        self.psislider = QtWidgets.QSlider(self.control_tab)
        self.psislider.setGeometry(QtCore.QRect(10, 424, 180, 31))
        self.psislider.setOrientation(QtCore.Qt.Horizontal)
        self.psislider.setObjectName("psislider")
        self.psilabel = QtWidgets.QLabel(self.control_tab)
        self.psilabel.setGeometry(QtCore.QRect(10, 405, 201, 16))
        self.psilabel.setObjectName("psilabel")
        self.magneticfieldsimlabel = QtWidgets.QLabel(self.control_tab)
        self.magneticfieldsimlabel.setGeometry(QtCore.QRect(5, 520, 200, 200))
        self.magneticfieldsimlabel.setStyleSheet("background-color: rgb(0,0,0); border:2px solid rgb(255, 0, 0); ")
        self.magneticfieldsimlabel.setText("")
        self.magneticfieldsimlabel.setObjectName("magneticfieldsimlabel")
        self.memorylabel = QtWidgets.QLabel(self.control_tab)
        self.memorylabel.setGeometry(QtCore.QRect(10, 455, 201, 21))
        self.memorylabel.setObjectName("memorylabel")
        self.memoryslider = QtWidgets.QSlider(self.control_tab)
        self.memoryslider.setGeometry(QtCore.QRect(10, 474, 180, 31))
        self.memoryslider.setOrientation(QtCore.Qt.Horizontal)
        self.memoryslider.setObjectName("memoryslider")
        self.joystickbutton = QtWidgets.QPushButton(self.control_tab)
        self.joystickbutton.setGeometry(QtCore.QRect(30, 110, 141, 31))
        self.joystickbutton.setStyleSheet("QPushButton {\n"
"                color: rgb(255, 255, 255);\n"
"                background-color: rgb(255, 0, 255);\n"
"                border-style: outset;\n"
"                border-width: 3px;\n"
"                border-radius: 10px;\n"
"                border-color: rgb(255, 0, 255);\n"
"                min-width: 1em;\n"
"                padding: 6px;\n"
"            }\n"
"      \n"
"            QPushButton:checked {\n"
"                color: rgb(255, 255, 255);\n"
"                background-color: rgb(200, 0, 200);\n"
"                border-style: inset;\n"
"                border-width: 3px;\n"
"                border-radius: 10px;\n"
"                border-color: rgb(200, 0, 200);\n"
"                font: bold 16px;\n"
"                min-width: 1em;\n"
"              padding-left: 5px;\n"
"                padding-top: 5px;\n"
"               \n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: rgb(100, 100, 100);\n"
"                color: rgb(255, 255, 255);\n"
"                border-color: rgb(100, 100, 100);\n"
"                padding-left: 5px;\n"
"                padding-top: 5px;\n"
"            }")
        self.joystickbutton.setCheckable(True)
        self.joystickbutton.setObjectName("joystickbutton")
        self.acousticfreq_spinBox = QtWidgets.QSpinBox(self.control_tab)
        self.acousticfreq_spinBox.setGeometry(QtCore.QRect(20, 170, 171, 31))
        self.acousticfreq_spinBox.setMaximum(3000000)
        self.acousticfreq_spinBox.setObjectName("acousticfreq_spinBox")
        self.acousticfreqlabel = QtWidgets.QLabel(self.control_tab)
        self.acousticfreqlabel.setGeometry(QtCore.QRect(10, 150, 191, 21))
        self.acousticfreqlabel.setObjectName("acousticfreqlabel")
        self.applyacousticbutton = QtWidgets.QPushButton(self.control_tab)
        self.applyacousticbutton.setGeometry(QtCore.QRect(20, 210, 161, 25))
        self.applyacousticbutton.setStyleSheet("QPushButton {\n"
"                color: rgb(255, 255, 255);\n"
"                background-color: rgb(0, 0, 0);\n"
"                border-style: outset;\n"
"                border-width: 2px;\n"
"                border-radius: 10px;\n"
"                border-color: rgb(0, 0, 0);\n"
"                min-width: 1em;\n"
"                padding: 1px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: rgb(100, 100, 100);\n"
"                color: rgb(0, 0, 0);\n"
"                border-style: inset;\n"
"            }")
        self.applyacousticbutton.setCheckable(True)
        self.applyacousticbutton.setObjectName("applyacousticbutton")
        self.tabWidget.addTab(self.control_tab, "")
        self.VideoFeedLabel = QtWidgets.QLabel(self.centralwidget)
        self.VideoFeedLabel.setGeometry(QtCore.QRect(230, 30, 1330, 700))
        self.VideoFeedLabel.setMouseTracking(True)
        self.VideoFeedLabel.setStyleSheet("background-color: rgb(0,0,0); border:2px solid rgb(255, 0, 0); ")
        self.VideoFeedLabel.setText("")
        self.VideoFeedLabel.setObjectName("VideoFeedLabel")
        self.frameslider = QtWidgets.QSlider(self.centralwidget)
        self.frameslider.setGeometry(QtCore.QRect(230, 0, 1321, 30))
        self.frameslider.setOrientation(QtCore.Qt.Horizontal)
        self.frameslider.setObjectName("frameslider")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(230, 735, 791, 91))
        self.plainTextEdit.setMouseTracking(True)
        self.plainTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.plainTextEdit.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.plainTextEdit.setCenterOnScroll(False)
        self.plainTextEdit.setObjectName("plainTextEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.robotblurlabel.setText(_translate("MainWindow", "Blur:"))
        self.rightbutton.setText(_translate("MainWindow", "..."))
        self.choosevideobutton.setText(_translate("MainWindow", "Choose Video"))
        self.croplengthlabel.setText(_translate("MainWindow", "Crop Length: 40"))
        self.pausebutton.setText(_translate("MainWindow", "Pause"))
        self.trackbutton.setText(_translate("MainWindow", "Track"))
        self.robotarealabel.setText(_translate("MainWindow", "Area:"))
        self.maskinvert_checkBox.setText(_translate("MainWindow", "Mask Invert: True"))
        self.maskbutton.setText(_translate("MainWindow", "Mask"))
        self.leftbutton.setText(_translate("MainWindow", "..."))
        self.savedatabutton.setText(_translate("MainWindow", "Save Data"))
        self.masksigmalabel.setText(_translate("MainWindow", "Mask Sigma: 0.7"))
        self.robotvelocitylabel.setText(_translate("MainWindow", "Velocity:"))
        self.framelabel.setText(_translate("MainWindow", "Frame: "))
        self.recordbutton.setText(_translate("MainWindow", "Record"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tracking_tab), _translate("MainWindow", "Tracking"))
        self.controlbutton.setText(_translate("MainWindow", "Control"))
        self.controlautoradio.setText(_translate("MainWindow", "Automatic"))
        self.controlmanualradio.setText(_translate("MainWindow", "Manual"))
        self.arrivalthreshlabel.setText(_translate("MainWindow", "arivial thresh"))
        self.gammalabel.setText(_translate("MainWindow", "gamma"))
        self.rollingfrequencylabel.setText(_translate("MainWindow", "rolling frequency"))
        self.psilabel.setText(_translate("MainWindow", "psi"))
        self.memorylabel.setText(_translate("MainWindow", "memory"))
        self.joystickbutton.setText(_translate("MainWindow", "Joystick"))
        self.acousticfreqlabel.setText(_translate("MainWindow", "Acoustic Frequency"))
        self.applyacousticbutton.setText(_translate("MainWindow", "Apply"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.control_tab), _translate("MainWindow", "Control"))
