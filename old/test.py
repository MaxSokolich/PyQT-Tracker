import cv2
import numpy as np




import cv2
import numpy as np

# Load the original image and the mask
frame = cv2.imread('/Users/bizzarohd/Desktop/Screenshot 2023-08-08 at 10.25.56 AM.png')


# Invert the mask



x = 5
y = 500
w = 300
h = 300

angle=0
zoom =1.01

if y-w < 0 and x-h < 0:
    zoomedframe = frame[0:y+h , 0:x+w]
    cv2.rectangle(frame, (0, 0), (x + w, y + h), (0, 255, 0), 2)
    warpx = x
    warpy = y
elif x-w < 0:
    zoomedframe = frame[y-h:y+h , 0:x+w] 
    cv2.rectangle(frame, (0, y-h), (x + w, y + h), (0, 255, 0), 2)
    warpx = x
    warpy = h
elif y-h < 0:
    zoomedframe = frame[0:y+h , x-w:x+w]
    cv2.rectangle(frame, (x-w, 0), (x + w, y + h), (0, 255, 0), 2)
    warpx = w
    warpy = h
else:
    zoomedframe = frame[y-h:y+h , x-w:x+w] 
    cv2.rectangle(frame, (x-w, y-h), (x + w, y + h), (0, 255, 0), 2)
    warpx = w
    warpy = h   


cv2.circle(frame,(int(x), int(y)),60,(0,255,0), -1,)
cv2.circle(zoomedframe,(int(warpx), int(warpy)),15,(255,0,0), -1,)
# step 1: cropped a frame around the coord you wont to zoom into


# step 2: zoom into the zoomed frame a certain zoom amount
rot_mat = cv2.getRotationMatrix2D((warpx,warpy), angle, zoom)
zoomedframe = cv2.warpAffine(zoomedframe, rot_mat, zoomedframe.shape[1::-1], flags=cv2.INTER_LINEAR)

#step 3: replace the original cropped frame with the new zoomed in cropped frame
#frame[0:y+w , 0:x+h] = zoomedframe
if y-h < 0 and x-w < 0:
    frame[0:y+h , 0:x+w] =  zoomedframe
elif x-w < 0:
    frame[y-h:y+h , 0:x+w] =  zoomedframe
elif y-h < 0:
    frame[0:y+h , x-w:x+w] =  zoomedframe
else:
    frame[y-h:y+h , x-w:x+w] =  zoomedframe


cv2.imshow("zoom", zoomedframe)
cv2.imshow("final_image", frame)


cv2.waitKey(0)
cv2.destroyAllWindows()

# To save the image:

