# PyQT-Tracker

New microrobotic tracking and control UI

to make a standalone app: /opt/homebrew/bin/python3.10 -m PyInstaller --onedir --windowed --icon TrackerIcon.icns --name Tracker Tracker.py

4 Files:

gui_class.py: this contains the PyQT UI arctecture
main.py: main file to run the app
robot_class.py: a robot class that contains all the information about a detected robot
tracker_class.py: the thread that reads opencv frames and the sends them to the gui. a thread is needed a avoid blocking. 

<img width="1594" alt="PyQT-Tracker" src="https://github.com/MaxSokolich/PyQT-Tracker/assets/50302377/4177282a-906d-4ded-8ba0-9130be71bef4">

