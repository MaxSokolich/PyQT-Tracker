# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MagscopeLinux.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1874, 1065)
        font = QtGui.QFont()
        font.setFamily("Arial")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("font-family: Arial;")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(250, 1000))
        self.tabWidget.setStyleSheet("font-size: 15pt; font: Arial;")
        self.tabWidget.setObjectName("tabWidget")
        self.tracking_tab = QtWidgets.QWidget()
        self.tracking_tab.setObjectName("tracking_tab")
        self.robotblurlabel = QtWidgets.QLabel(self.tracking_tab)
        self.robotblurlabel.setGeometry(QtCore.QRect(10, 480, 161, 20))
        self.robotblurlabel.setObjectName("robotblurlabel")
        self.rightbutton = QtWidgets.QToolButton(self.tracking_tab)
        self.rightbutton.setGeometry(QtCore.QRect(110, 140, 60, 25))
        self.rightbutton.setStyleSheet("QToolButton {\n"
"                color: rgb(255, 255, 255);\n"
"                background-color: rgb(0, 0, 0);\n"
"                border-style: outset;\n"
"                border-width: px;\n"
"                border-radius: 10px;\n"
"                border: 2px solid rgb(0, 0, 0);\n"
"                font: bold 16px;\n"
"                min-width: 1em;\n"
"                padding: 1px;\n"
"            }\n"
"            QToolButton:hover {\n"
"                background-color: rgb(100, 100, 100);\n"
"                color: rgb(255, 255, 255);\n"
"                border: 2px solid rgb(0, 255, 0);\n"
"            }\n"
"            QToolButton:pressed {\n"
"                background-color: rgb(100, 100, 100);\n"
"                border: 2px solid rgb(255, 0, 0);\n"
"                border-style: inset;\n"
"                padding-left: 5px;\n"
"                padding-top: 5px;\n"
"            }")
        self.rightbutton.setAutoRepeat(True)
        self.rightbutton.setAutoRepeatInterval(1)
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
        self.croplengthlabel.setGeometry(QtCore.QRect(10, 325, 101, 20))
        self.croplengthlabel.setObjectName("croplengthlabel")
        self.pausebutton = QtWidgets.QPushButton(self.tracking_tab)
        self.pausebutton.setGeometry(QtCore.QRect(20, 110, 160, 25))
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
"                border-color: rgb(0, 0, 255);\n"
"                font: bold 12px;\n"
"                min-width: 1em;\n"
"                padding: 1px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: rgb(100, 100, 100);\n"
"                color: rgb(255, 255, 255);\n"
"                border-color: rgb(255, 0, 0);\n"
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
"                border-color: rgb(0, 255, 0);\n"
"                padding-left: 5px;\n"
"                padding-top: 5px;\n"
"            }")
        self.trackbutton.setCheckable(True)
        self.trackbutton.setObjectName("trackbutton")
        self.robotarealabel = QtWidgets.QLabel(self.tracking_tab)
        self.robotarealabel.setGeometry(QtCore.QRect(10, 440, 161, 20))
        self.robotarealabel.setObjectName("robotarealabel")
        self.maskinvert_checkBox = QtWidgets.QCheckBox(self.tracking_tab)
        self.maskinvert_checkBox.setGeometry(QtCore.QRect(10, 210, 191, 21))
        self.maskinvert_checkBox.setChecked(True)
        self.maskinvert_checkBox.setObjectName("maskinvert_checkBox")
        self.maskbutton = QtWidgets.QPushButton(self.tracking_tab)
        self.maskbutton.setGeometry(QtCore.QRect(20, 174, 161, 31))
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
"                color: rgb(255, 255, 255);\n"
"                border-style: inset;\n"
"              border-color: rgb(0, 255, 0);\n"
"            }")
        self.maskbutton.setCheckable(True)
        self.maskbutton.setChecked(False)
        self.maskbutton.setObjectName("maskbutton")
        self.CroppedVideoFeedLabel = QtWidgets.QLabel(self.tracking_tab)
        self.CroppedVideoFeedLabel.setGeometry(QtCore.QRect(5, 520, 200, 200))
        self.CroppedVideoFeedLabel.setStyleSheet("background-color: rgb(0,0,0); border:2px solid rgb(255, 0, 0); ")
        self.CroppedVideoFeedLabel.setText("")
        self.CroppedVideoFeedLabel.setObjectName("CroppedVideoFeedLabel")
        self.leftbutton = QtWidgets.QToolButton(self.tracking_tab)
        self.leftbutton.setGeometry(QtCore.QRect(30, 140, 60, 25))
        self.leftbutton.setStyleSheet("QToolButton {\n"
"                color: rgb(255, 255, 255);\n"
"                background-color: rgb(0, 0, 0);\n"
"                border-style: outset;\n"
"                border-width: px;\n"
"                border-radius: 10px;\n"
"                border: 2px solid rgb(0, 0, 0);\n"
"                font: bold 16px;\n"
"                min-width: 1em;\n"
"                padding: 1px;\n"
"            }\n"
"            QToolButton:hover {\n"
"                background-color: rgb(100, 100, 100);\n"
"                color: rgb(255, 255, 255);\n"
"                border: 2px solid rgb(0, 255, 0);\n"
"            }\n"
"            QToolButton:pressed {\n"
"                background-color: rgb(100, 100, 100);\n"
"                border: 2px solid rgb(255, 0, 0);\n"
"                border-style: inset;\n"
"                padding-left: 5px;\n"
"                padding-top: 5px;\n"
"            }")
        self.leftbutton.setAutoRepeat(True)
        self.leftbutton.setAutoRepeatInterval(1)
        self.leftbutton.setArrowType(QtCore.Qt.LeftArrow)
        self.leftbutton.setObjectName("leftbutton")
        self.savedatabutton = QtWidgets.QPushButton(self.tracking_tab)
        self.savedatabutton.setGeometry(QtCore.QRect(0, 365, 100, 51))
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
        self.maskthreshlabel = QtWidgets.QLabel(self.tracking_tab)
        self.maskthreshlabel.setGeometry(QtCore.QRect(10, 245, 111, 20))
        self.maskthreshlabel.setObjectName("maskthreshlabel")
        self.robotvelocitylabel = QtWidgets.QLabel(self.tracking_tab)
        self.robotvelocitylabel.setGeometry(QtCore.QRect(10, 460, 161, 20))
        self.robotvelocitylabel.setObjectName("robotvelocitylabel")
        self.framelabel = QtWidgets.QLabel(self.tracking_tab)
        self.framelabel.setGeometry(QtCore.QRect(50, 80, 121, 31))
        self.framelabel.setObjectName("framelabel")
        self.recordbutton = QtWidgets.QPushButton(self.tracking_tab)
        self.recordbutton.setGeometry(QtCore.QRect(105, 365, 100, 51))
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
        self.label = QtWidgets.QLabel(self.tracking_tab)
        self.label.setGeometry(QtCore.QRect(0, 430, 205, 80))
        self.label.setStyleSheet("color: rgb(0, 0, 0);\n"
"                background-color: rgb(255, 255, 255);\n"
"                border-style: outset;\n"
"                border-width: 3px;\n"
"                border-radius: 10px;\n"
"                border-color: rgb(0, 0, 0);\n"
"                min-width: 1em;\n"
"                padding: 6px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.maskdilationlabel = QtWidgets.QLabel(self.tracking_tab)
        self.maskdilationlabel.setGeometry(QtCore.QRect(10, 285, 121, 20))
        self.maskdilationlabel.setObjectName("maskdilationlabel")
        self.maskdilationbox = QtWidgets.QSpinBox(self.tracking_tab)
        self.maskdilationbox.setGeometry(QtCore.QRect(140, 280, 61, 31))
        self.maskdilationbox.setMaximum(40)
        self.maskdilationbox.setObjectName("maskdilationbox")
        self.croplengthbox = QtWidgets.QSpinBox(self.tracking_tab)
        self.croplengthbox.setGeometry(QtCore.QRect(140, 320, 61, 31))
        self.croplengthbox.setMinimum(5)
        self.croplengthbox.setMaximum(300)
        self.croplengthbox.setProperty("value", 40)
        self.croplengthbox.setDisplayIntegerBase(10)
        self.croplengthbox.setObjectName("croplengthbox")
        self.resetdefaultbutton = QtWidgets.QPushButton(self.tracking_tab)
        self.resetdefaultbutton.setGeometry(QtCore.QRect(30, 730, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.resetdefaultbutton.setFont(font)
        self.resetdefaultbutton.setStyleSheet("QPushButton {\n"
"                color: rgb(255, 255, 255);\n"
"                background-color: rgb(100, 100, 100);\n"
"                border-style: outset;\n"
"                border-width: 2px;\n"
"                border-radius: 10px;\n"
"                border-color: rgb(100, 100, 100);\n"
"                min-width: 1em;\n"
"                padding: 1px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: rgb(200, 200, 200);\n"
"                color: rgb(0, 0, 0);\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: rgb(200, 200, 200);\n"
"         \n"
"                padding-left: 5px;\n"
"                padding-top: 5px;\n"
"                border-style: inset;\n"
"                }")
        self.resetdefaultbutton.setObjectName("resetdefaultbutton")
        self.maskthreshbox = QtWidgets.QSpinBox(self.tracking_tab)
        self.maskthreshbox.setGeometry(QtCore.QRect(140, 240, 61, 31))
        self.maskthreshbox.setMaximum(255)
        self.maskthreshbox.setProperty("value", 128)
        self.maskthreshbox.setObjectName("maskthreshbox")
        self.label.raise_()
        self.robotblurlabel.raise_()
        self.rightbutton.raise_()
        self.choosevideobutton.raise_()
        self.croplengthlabel.raise_()
        self.pausebutton.raise_()
        self.trackbutton.raise_()
        self.robotarealabel.raise_()
        self.maskinvert_checkBox.raise_()
        self.maskbutton.raise_()
        self.CroppedVideoFeedLabel.raise_()
        self.leftbutton.raise_()
        self.savedatabutton.raise_()
        self.maskthreshlabel.raise_()
        self.robotvelocitylabel.raise_()
        self.framelabel.raise_()
        self.recordbutton.raise_()
        self.maskdilationlabel.raise_()
        self.maskdilationbox.raise_()
        self.croplengthbox.raise_()
        self.resetdefaultbutton.raise_()
        self.maskthreshbox.raise_()
        self.tabWidget.addTab(self.tracking_tab, "")
        self.control_tab = QtWidgets.QWidget()
        self.control_tab.setObjectName("control_tab")
        self.controlbutton = QtWidgets.QPushButton(self.control_tab)
        self.controlbutton.setGeometry(QtCore.QRect(20, 5, 160, 51))
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
"                border-color: rgb(0, 255, 0);\n"
"                padding-left: 5px;\n"
"                padding-top: 5px;\n"
"            }")
        self.controlbutton.setCheckable(True)
        self.controlbutton.setObjectName("controlbutton")
        self.arrivalthreshlabel = QtWidgets.QLabel(self.control_tab)
        self.arrivalthreshlabel.setGeometry(QtCore.QRect(10, 310, 131, 21))
        self.arrivalthreshlabel.setObjectName("arrivalthreshlabel")
        self.gammalabel = QtWidgets.QLabel(self.control_tab)
        self.gammalabel.setGeometry(QtCore.QRect(110, 490, 101, 20))
        self.gammalabel.setObjectName("gammalabel")
        self.rollingfrequencylabel = QtWidgets.QLabel(self.control_tab)
        self.rollingfrequencylabel.setGeometry(QtCore.QRect(10, 350, 91, 21))
        self.rollingfrequencylabel.setObjectName("rollingfrequencylabel")
        self.psilabel = QtWidgets.QLabel(self.control_tab)
        self.psilabel.setGeometry(QtCore.QRect(20, 490, 71, 21))
        self.psilabel.setObjectName("psilabel")
        self.magneticfieldsimlabel = QtWidgets.QLabel(self.control_tab)
        self.magneticfieldsimlabel.setGeometry(QtCore.QRect(5, 520, 200, 200))
        self.magneticfieldsimlabel.setStyleSheet("background-color: rgb(0,0,0); border:2px solid rgb(255, 0, 0); ")
        self.magneticfieldsimlabel.setText("")
        self.magneticfieldsimlabel.setObjectName("magneticfieldsimlabel")
        self.joystickbutton = QtWidgets.QPushButton(self.control_tab)
        self.joystickbutton.setGeometry(QtCore.QRect(30, 90, 141, 31))
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
        self.acousticfreq_spinBox.setGeometry(QtCore.QRect(20, 150, 171, 31))
        self.acousticfreq_spinBox.setMaximum(3000000)
        self.acousticfreq_spinBox.setObjectName("acousticfreq_spinBox")
        self.acousticfreqlabel = QtWidgets.QLabel(self.control_tab)
        self.acousticfreqlabel.setGeometry(QtCore.QRect(20, 130, 171, 21))
        self.acousticfreqlabel.setObjectName("acousticfreqlabel")
        self.applyacousticbutton = QtWidgets.QPushButton(self.control_tab)
        self.applyacousticbutton.setGeometry(QtCore.QRect(20, 190, 111, 25))
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
"            }\n"
"\n"
"         QPushButton:checked {\n"
"                color: rgb(255, 255, 255);\n"
"                background-color: rgb(255, 0, 0);\n"
"                border-style: outset;\n"
"                border-width: 2px;\n"
"                border-radius: 10px;\n"
"                border-color: rgb(200, 0, 0);\n"
"                min-width: 1em;\n"
"                padding: 1px;\n"
"}")
        self.applyacousticbutton.setCheckable(True)
        self.applyacousticbutton.setObjectName("applyacousticbutton")
        self.RRTtreesizelabel = QtWidgets.QLabel(self.control_tab)
        self.RRTtreesizelabel.setGeometry(QtCore.QRect(10, 270, 131, 21))
        self.RRTtreesizelabel.setObjectName("RRTtreesizelabel")
        self.memorylabel = QtWidgets.QLabel(self.control_tab)
        self.memorylabel.setGeometry(QtCore.QRect(10, 230, 61, 21))
        self.memorylabel.setObjectName("memorylabel")
        self.rollradio = QtWidgets.QRadioButton(self.control_tab)
        self.rollradio.setGeometry(QtCore.QRect(10, 65, 61, 20))
        self.rollradio.setChecked(True)
        self.rollradio.setObjectName("rollradio")
        self.swimradio = QtWidgets.QRadioButton(self.control_tab)
        self.swimradio.setGeometry(QtCore.QRect(70, 65, 61, 20))
        self.swimradio.setObjectName("swimradio")
        self.led = QtWidgets.QLabel(self.control_tab)
        self.led.setGeometry(QtCore.QRect(150, 190, 25, 25))
        self.led.setStyleSheet("\n"
"                background-color: rgb(255, 0, 0);\n"
"                border-style: outset;\n"
"                border-width: 3px;\n"
"                border-radius: 12px;\n"
"                border-color: rgb(255, 0, 0);\n"
"         \n"
"                padding: 6px;")
        self.led.setText("")
        self.led.setObjectName("led")
        self.memorybox = QtWidgets.QSpinBox(self.control_tab)
        self.memorybox.setGeometry(QtCore.QRect(140, 220, 61, 31))
        self.memorybox.setMinimum(1)
        self.memorybox.setMaximum(100)
        self.memorybox.setProperty("value", 15)
        self.memorybox.setObjectName("memorybox")
        self.RRTtreesizebox = QtWidgets.QSpinBox(self.control_tab)
        self.RRTtreesizebox.setGeometry(QtCore.QRect(140, 260, 61, 31))
        self.RRTtreesizebox.setMinimum(1)
        self.RRTtreesizebox.setMaximum(100)
        self.RRTtreesizebox.setProperty("value", 25)
        self.RRTtreesizebox.setObjectName("RRTtreesizebox")
        self.arrivalthreshbox = QtWidgets.QSpinBox(self.control_tab)
        self.arrivalthreshbox.setGeometry(QtCore.QRect(140, 300, 61, 31))
        self.arrivalthreshbox.setMinimum(1)
        self.arrivalthreshbox.setMaximum(100)
        self.arrivalthreshbox.setProperty("value", 20)
        self.arrivalthreshbox.setObjectName("arrivalthreshbox")
        self.rollingfrequencybox = QtWidgets.QSpinBox(self.control_tab)
        self.rollingfrequencybox.setGeometry(QtCore.QRect(140, 340, 61, 31))
        self.rollingfrequencybox.setMinimum(0)
        self.rollingfrequencybox.setMaximum(40)
        self.rollingfrequencybox.setProperty("value", 10)
        self.rollingfrequencybox.setObjectName("rollingfrequencybox")
        self.psidial = QtWidgets.QDial(self.control_tab)
        self.psidial.setGeometry(QtCore.QRect(10, 380, 91, 101))
        self.psidial.setStyleSheet("QDial\n"
"    {\n"
"        background-color:QLinearGradient( \n"
"            x1: 0.177, y1: 0.004, x2: 0.831, y2: 0.911, \n"
"            stop: 0 white, \n"
"            stop: 0.061 white, \n"
"            stop: 0.066 lightgray, \n"
"            stop: 0.5 #242424, \n"
"            stop: 0.505 #000000,\n"
"            stop: 0.827 #040404,\n"
"            stop: 0.966 #292929,\n"
"            stop: 0.983 #2e2e2e\n"
"        );\n"
"    }")
        self.psidial.setMinimum(1)
        self.psidial.setMaximum(90)
        self.psidial.setSingleStep(5)
        self.psidial.setProperty("value", 90)
        self.psidial.setNotchTarget(10.0)
        self.psidial.setNotchesVisible(True)
        self.psidial.setObjectName("psidial")
        self.gammadial = QtWidgets.QDial(self.control_tab)
        self.gammadial.setGeometry(QtCore.QRect(110, 380, 91, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.gammadial.setFont(font)
        self.gammadial.setStyleSheet("QDial {\n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0 #1a5276, stop:0.3 #2980b9, stop:0.7 #3498db, stop:1 #1a5276);\n"
"    border: 2px solid #1a5276;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QDial::handle {\n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0 #f39c12, stop:0.3 #f1c40f, stop:0.7 #f39c12, stop:1 #f1c40f);\n"
"    border: 2px solid #e67e22;\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    border-radius: 10px;\n"
"    margin: -5px;\n"
"}\n"
"")
        self.gammadial.setMaximum(180)
        self.gammadial.setSingleStep(5)
        self.gammadial.setPageStep(10)
        self.gammadial.setProperty("value", 90)
        self.gammadial.setOrientation(QtCore.Qt.Horizontal)
        self.gammadial.setWrapping(False)
        self.gammadial.setNotchTarget(10.0)
        self.gammadial.setNotchesVisible(True)
        self.gammadial.setObjectName("gammadial")
        self.simulationbutton = QtWidgets.QPushButton(self.control_tab)
        self.simulationbutton.setGeometry(QtCore.QRect(20, 730, 171, 21))
        self.simulationbutton.setStyleSheet("QPushButton {\n"
"                color: rgb(255, 255, 255);\n"
"                background-color: rgb(0, 255, 0);\n"
"                border-style: outset;\n"
"                border-width: 2px;\n"
"                border-radius: 10px;\n"
"                border-color: rgb(0, 100, 0);\n"
"                min-width: 1em;\n"
"                padding: 2px;\n"
"            }\n"
"      \n"
"            QPushButton:checked {\n"
"                color: rgb(255, 255, 255);\n"
"                background-color: rgb(255, 100, 0);\n"
"                border-style: inset;\n"
"                border-width: 2px;\n"
"                border-radius: 10px;\n"
"                border-color: rgb(255, 0, 0);\n"
"                font: bold 16px;\n"
"                min-width: 1em;\n"
"\n"
"               \n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: rgb(100, 100, 100);\n"
"                color: rgb(255, 255, 255);\n"
"                border-color: rgb(100, 100, 100);\n"
"                padding-left: 5px;\n"
"                padding-top: 5px;\n"
"            }")
        self.simulationbutton.setCheckable(True)
        self.simulationbutton.setObjectName("simulationbutton")
        self.orientradio = QtWidgets.QRadioButton(self.control_tab)
        self.orientradio.setGeometry(QtCore.QRect(140, 65, 71, 20))
        self.orientradio.setObjectName("orientradio")
        self.tabWidget.addTab(self.control_tab, "")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.tabWidget)
        self.VideoFeedLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VideoFeedLabel.sizePolicy().hasHeightForWidth())
        self.VideoFeedLabel.setSizePolicy(sizePolicy)
        self.VideoFeedLabel.setMouseTracking(True)
        self.VideoFeedLabel.setStyleSheet("background-color: rgb(0,0,0); border:2px solid rgb(255, 0, 0); ")
        self.VideoFeedLabel.setText("")
        self.VideoFeedLabel.setScaledContents(False)
        self.VideoFeedLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.VideoFeedLabel.setObjectName("VideoFeedLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.VideoFeedLabel)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actiondock = QtWidgets.QAction(MainWindow)
        self.actiondock.setMenuRole(QtWidgets.QAction.NoRole)
        self.actiondock.setObjectName("actiondock")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.robotblurlabel.setText(_translate("MainWindow", "Blur:"))
        self.rightbutton.setText(_translate("MainWindow", "..."))
        self.choosevideobutton.setText(_translate("MainWindow", "Choose Video"))
        self.croplengthlabel.setText(_translate("MainWindow", "Crop Length"))
        self.pausebutton.setText(_translate("MainWindow", "Pause"))
        self.trackbutton.setText(_translate("MainWindow", "Track"))
        self.robotarealabel.setText(_translate("MainWindow", "Area:"))
        self.maskinvert_checkBox.setText(_translate("MainWindow", "Invert Mask: True"))
        self.maskbutton.setText(_translate("MainWindow", "Mask"))
        self.leftbutton.setText(_translate("MainWindow", "..."))
        self.savedatabutton.setText(_translate("MainWindow", "Save Data"))
        self.maskthreshlabel.setText(_translate("MainWindow", "Mask Thresh"))
        self.robotvelocitylabel.setText(_translate("MainWindow", "Velocity:"))
        self.framelabel.setText(_translate("MainWindow", "Frame: "))
        self.recordbutton.setText(_translate("MainWindow", "Record"))
        self.maskdilationlabel.setText(_translate("MainWindow", "Mask Dilation"))
        self.resetdefaultbutton.setText(_translate("MainWindow", "Reset"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tracking_tab), _translate("MainWindow", "Tracking"))
        self.controlbutton.setText(_translate("MainWindow", "Control"))
        self.arrivalthreshlabel.setText(_translate("MainWindow", "Arrive Thresh"))
        self.gammalabel.setText(_translate("MainWindow", "Gamma: 90"))
        self.rollingfrequencylabel.setText(_translate("MainWindow", "Frequency"))
        self.psilabel.setText(_translate("MainWindow", "Psi: 90"))
        self.joystickbutton.setText(_translate("MainWindow", "Joystick"))
        self.acousticfreqlabel.setText(_translate("MainWindow", "Acoustic Frequency"))
        self.applyacousticbutton.setText(_translate("MainWindow", "Apply"))
        self.RRTtreesizelabel.setText(_translate("MainWindow", "RRT Tree Size"))
        self.memorylabel.setText(_translate("MainWindow", "Memory"))
        self.rollradio.setText(_translate("MainWindow", "Roll"))
        self.swimradio.setText(_translate("MainWindow", "Swim"))
        self.simulationbutton.setText(_translate("MainWindow", "Simulation On"))
        self.orientradio.setText(_translate("MainWindow", "Orient"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.control_tab), _translate("MainWindow", "Control"))
        self.actiondock.setText(_translate("MainWindow", "dock"))
