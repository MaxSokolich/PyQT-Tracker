import sys
from src.gui_class import App
from PyQt5.QtWidgets import QApplication

"""
to create stand alone app:
    pyinstaller --onefile --windowed --icon icon.icns --name Tracker main.py


    /path/to/python3 -m PyInstaller your_script.py
"""
if __name__=="__main__":
    app = QApplication(sys.argv)
    a = App()
    a.show()
    sys.exit(app.exec_())