from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread,QTimer
import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
from datetime import datetime 
from scipy import ndimage 
import time

from classes.algorithm_class import algorithm
    
#add unique crop length 
class RecordThread(QThread):

    def __init__(self, parent):
        super().__init__(parent=parent)
        self.parent = parent
        
        self.recordstatus = True
        self.cap = self.parent.cap
        self.width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.videofps = int(self.cap.get(cv2.CAP_PROP_FPS))

      
        date = datetime.now().strftime('%Y.%m.%d-%H.%M.%S')
        file_path  = os.path.join(self.parent.new_dir_path, date+".mp4")
        self.result = cv2.VideoWriter(
                    file_path,
                    cv2.VideoWriter_fourcc(*"mp4v"),
                    int(self.videofps),    
                    (self.width, self.height), ) 

    def run(self):
        # capture from web camx
        while self.recordstatus:

            """cv2.putText(self.parent.currentframe,"frame: "+ str(self.parent.tracker.framenum),
                        (int(self.width / 8),
                        int(self.height / 30)),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=1, 
                        thickness=4,
                        color = (255, 255, 255))"""
            
            #frame = cv2.resize(frame, (self.width,self.height), interpolation = cv2.INTER_AREA)
            self.result.write(self.parent.currentframe)
            time.sleep(1/self.videofps)

           
                


    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        #blank = np.zeros((self.width, self.height, 3), dtype=np.uint8) 
        #self.change_pixmap_signal.emit(blank)
        self.recordstatus = False
        self.wait()
        self.result.release()
    
        



