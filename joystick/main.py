from queue import Empty
from ControllerClass import Controller
from ArduinoHandler import ArduinoHandler


from multiprocessing import Process, Queue, Event
#from src.python.AcousticClass import AcousticClass
import time

"""
Bx             : magnetic field in x
By             : magnetic field in y
Bz             : magnetic field in z
Mx             : stage motor in x
My             : stage motor in y
Mz             : stage motor in z
alpha          : rolling polar angle 
gamma          : rolling azimuthal angle
freq.          : rolling frequency
acoustic_status: acoustic module status on or off
"""


class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)


if __name__ == "__main__":
    #create instance of motor stage class


    #create instance and connect to arduino module
    PORT = "/dev/ttyACM0"
    arduino = ArduinoHandler()
    arduino.connect(PORT)
    
    #create queue  to handle joystick commands
    joystick_q = Queue(1)
    controller = MyController(joystick_q=joystick_q,interface="/dev/input/js0", connecting_using_ds4drv=False)
    
    joystick_process = Process(target = controller.listen, args = (joystick_q,))
    joystick_process.start()

    while True:
        try:
            actions = joystick_q.get(0)

            if actions == False:
                print("breaking")
                break
            else:
                
                Bx,By,Bz,Mx,My,Mz,alpha,gamma,freq,acoustic_status = actions
                #arduino.send(Bx,By,Bz,alpha,gamma,freq)
           
 
                print(actions)
                #send Mx,My,Mz via adarduit motorkit libaray, not arduino for now
                
        except Empty:
            pass
 

    joystick_process.join()

  


