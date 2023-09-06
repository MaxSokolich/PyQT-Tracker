
import numpy as np
Bxu = .5
Byu = .5
Bzu = .5

Bxr = 1
Byr = 0
Bzr = .5

if Bxu > 0 and Bxr > 0:
    Bx = (Bxu + Bxr)/2
elif Bxu == 0 and Bxr > 0:
    Bx = Bxr
elif Bxu > 0 and Bxr == 0:
    Bx = Bxu
else:
    Bx = 0

if Byu > 0 and Byr > 0:
    By = (Byu + Byr)/2
elif Byu == 0 and Byr > 0:
    By = Byr
elif Byu > 0 and Byr ==0:
    By = Byu
else:
    By = 0

if Bzu > 0 and Bzr > 0:
    Bz = (Bzu + Bzr)/2
elif Bzu == 0 and Bzr > 0:
    Bz = Bzr
elif Bzu > 0 and Bzr ==0:
    Bz = Bzu
else:
    Bz = 0

print(Bx, By, Bz)
#Bx = (Bxu + Bxr) / np.sqrt(Bxu**2 + Bxr**2)
#By = (Byu + Byr) / np.sqrt(Byu**2 + Byr**2)
#Bz = (Bzu + Bzr) / np.sqrt(Bzu**2 + Bzr**2)


#Bx = (Bx / np.sqrt(Bx*Bx + By*By + Bz*Bz))/2
#By = (By / np.sqrt(Bx*Bx + By*By + Bz*Bz))/2
#Bz = (Bz / np.sqrt(Bx*Bx + By*By + Bz*Bz))/2

#print(Bx, By, Bz)
