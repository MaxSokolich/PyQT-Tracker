from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread,QTimer
import numpy as np
import cv2
import matplotlib.pyplot as plt

from scipy import ndimage 
import time
    
#add unique crop length 
class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)
    cropped_frame_signal = pyqtSignal(np.ndarray)




    def __init__(self, cap):
        super().__init__()
        self._run_flag = True
        self._play_flag = True
        self.mask_flag = False
        #self.cap = cv2.VideoCapture(videopath)
        self.cap = cap
        self.fps = FPSCounter()
        self.width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.videofps = int(self.cap.get(cv2.CAP_PROP_FPS))
        self.totalnumframes = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))

        self.framenum = 0
        self.framenumlast = 0
        self.mask_sigma = 0.7
        self.maskinvert = True
        self.crop_length = 40
        self.robot_list = []

       

    def detect_robot(self, frame):
        """
        there are techincally 4 frames for analyse at a time:
        1) displayframe:  this is the raw BGR frame from the videofeed
        2) croppedframe: this is the cropped BGR frame surrounding the nearby robot 
        3) displaymask: this is the raw MONO mask from the videofeed
        4) croppedmask: this is the cropped MONO mask surrounding the nearby robot 
        
        """
        displayframe = frame.copy()
        
        if self.mask_flag == True:
            displaymask = self.find_mask(displayframe)
            displayframe = cv2.cvtColor(displaymask, cv2.COLOR_GRAY2BGR)
        
        if len(self.robot_list) > 0:
            
            color = plt.cm.rainbow(np.linspace(1, 0, len(self.robot_list))) * 255
            for (bot, botcolor) in zip(self.robot_list, color): #for each bot with a position botx, boty, find the cropped frame around the bot
               
                #current cropped frame dim
                x1, y1, w, h = bot.cropped_frame[-1]
                x1 = max(min(x1, self.width), 0)
                y1 = max(min(y1, self.height), 0)

                #crop the frame
                croppedframe = frame[y1 : y1 + h, x1 : x1 + w]
                
                #find the mask
                croppedmask  = self.find_mask(croppedframe)

                #find contours from the mask
                contours, _ = cv2.findContours(croppedmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                if len(contours) !=0:
                    max_cnt = contours[0]
                    for contour in contours:
                        if cv2.contourArea(contour) > cv2.contourArea(max_cnt): 
                            max_cnt = contour
                    area = cv2.contourArea(max_cnt)
                else:
                    area = 0
            

                #label the mask
                label_im, nb_labels = ndimage.label(croppedmask) 
                sizes = ndimage.sum(croppedmask, label_im, range(nb_labels + 1)) 
                num_bots=np.sum(sizes>50)
                
                if num_bots>0:
                    #find the center of mass from the mask
                    szsorted=np.argsort(sizes)
                    [ycord,xcord]=ndimage.center_of_mass(croppedmask,labels=label_im,index = szsorted[-(1)])
                    ndimage.binary_dilation
                    
                    #derive the global current location
                    current_pos = [xcord + x1,   ycord + y1] #xcord ycord are relative to the cropped frame. need to convert to the overall frame dim

                    
                    #generate new cropped frame based on the new robots position
                    x1_new = int(current_pos[0] - self.crop_length/2)
                    y1_new = int(current_pos[1] - self.crop_length/2)
                    w_new = int(self.crop_length)
                    h_new = int(self.crop_length)
                    new_crop = [int(x1_new), int(y1_new), int(w_new), int(h_new)]

                    #find velocity:
                    displacement = (np.array(current_pos) - np.array(bot.position_list[-1])).astype(float).round(2)

                    #find blur of original crop
                    blur = cv2.Laplacian(croppedframe, cv2.CV_64F).var()
                    
                    #store the data in the instance of RobotClasss
                    
                    #if self.framenum != self.framenumlast:
                    bot.add_frame(self.framenum)
                    bot.add_time(self.cap.get(cv2.CAP_PROP_POS_MSEC)/1000) #original in ms
                    bot.add_position([current_pos[0], current_pos[1]])
                    bot.add_velocity(displacement)
                    bot.add_crop(new_crop)
                    bot.add_area(area)
                    bot.add_blur(blur)
                    bot.set_avg_area(np.mean(bot.area_list))
                    self.framenumlast = self.framenum
                    
                    
                    #display visuals
                    cv2.circle(displayframe,(int(xcord+ x1), int(ycord + y1)),5,(botcolor),-1,)
                    cv2.rectangle(displayframe, (x1_new, y1_new), (x1_new + w_new, y1_new + h_new), (botcolor), 3)
                    
                    pts = np.array(bot.position_list, np.int32)
                    cv2.polylines(displayframe, [pts], False, botcolor, 3)
                             

                
            #constantly display the cropped frame mask for parameter tuning
            
            #croppedmask = frame[y1_new : y1_new + h_new, x1_new : x1_new + w_new]
            #croppedmask  = self.find_mask(croppedframe)
            croppedmask = cv2.cvtColor(croppedmask, cv2.COLOR_GRAY2BGR)
            if len(contours) !=0:
                cv2.drawContours(croppedmask, [max_cnt], -1, (0, 255, 255), 1)

        else:
            croppedmask = np.zeros((200, 200, 3), dtype=np.uint8) 

        return displayframe, croppedmask
 

            


    def find_mask(self, frame):

        im1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        invert = self.maskinvert
        mask_sigma= self.mask_sigma
        img_threshold=0


        BackgroundImg =  np.ones_like(im1)#BackgroundImage;#I only take every 10th image, any more is likely unnecessary, depends on fps but this can be slow
        meanBackgroundImg = np.median(BackgroundImg)
        
        imgdiff=(-(meanBackgroundImg-np.median(im1))+  BackgroundImg - im1)
        if not invert:
            imgdiff = np.mean(imgdiff)-imgdiff;#if invert is true then just keep the img as it is, this is for dark subjects. If invert is false then make it negative and shift by mean, this is for bright subjects
        
        maskdiff = imgdiff < img_threshold
        finalimg= np.where(maskdiff,np.zeros_like(im1),imgdiff)#setting dark pixels to zero
            
        mask = finalimg > (finalimg.mean() + mask_sigma*finalimg.std())

        mask = mask.astype(np.uint8)  #convert to an unsigned byte
        mask*=255
    
        return mask
    




  
        
    def run(self):
        # capture from web cam
        
        
        while self._run_flag:
            self.fps.update()

            #set and read frame
            if self._play_flag == True:
                self.framenum +=1
            
            

            if self.totalnumframes !=0:
                if self.framenum >  self.totalnumframes:
                    self.framenum = 0
                
                self.cap.set(1, self.framenum)
            
            
            ret, frame = self.cap.read()
        

            if ret:
                cv2.putText(frame,str(int(self.fps.get_fps())),
                    (int(self.width  / 40),int(self.height / 30)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=1, 
                    thickness=4,
                    color = (255, 255, 255))
                
                #step 1 detect robot
                frame, croppedframe = self.detect_robot(frame) 

                
                 #display graphics and emit the frame to the gui
                self.cropped_frame_signal.emit(croppedframe)
                self.change_pixmap_signal.emit(frame)
          

                if self.totalnumframes !=0:
                    interval = int(1000/self.videofps)  #use original fps used to record the video if not live
                    cv2.waitKey(interval)



    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        #blank = np.zeros((self.width, self.height, 3), dtype=np.uint8) 
        #self.change_pixmap_signal.emit(blank)

        self._run_flag = False
        self.wait()
        self.cap.release()
        cv2.destroyAllWindows

class FPSCounter:
    """
    Class for managing the FPS of the microbot tracker

    Args:
        None
    """

    def __init__(self):
        self.t0 = time.time()
        self.t1 = self.t0
        self.fps = 0

    def update(self):
        self.t1 = time.time()
        try:
            self.fps = 1 / (self.t1 - self.t0)
        except ZeroDivisionError:
            self.fps = 0
        self.t0 = self.t1

    def get_fps(self):
        return self.fps