# PyQT-Tracker
New microrobotic tracking and control UI

/opt/homebrew/bin/python3.10 -m PyInstaller --onedir --windowed --icon MagScopeBox.icns --name MagScope main.py

--osx-entitlements-file Info.plist

 pyuic5 MagscopeWindows.ui -o gui_widgets_windows.py
  pyuic5 MagscopeMac.ui -o gui_widgets_mac.py 

mk-icns MagScopeBox.png 
# Tracker Tab

<img width="1683" alt="MagScopeTracker" src="https://github.com/MaxSokolich/PyQT-Tracker/assets/50302377/97b103b2-4e89-4b2e-89fc-73de8a278ae8">

# Control Tab

<img width="1680" alt="MagScopeControl" src="https://github.com/MaxSokolich/PyQT-Tracker/assets/50302377/fa50d165-aaee-476f-ab29-0af3a1e49d97">




