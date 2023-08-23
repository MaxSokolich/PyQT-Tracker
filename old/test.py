import cv2
import numpy as np




import cv2
import numpy as np

# Load the original image and the mask
frame = cv2.imread('/Users/bizzarohd/Desktop/Screenshot 2023-08-08 at 10.25.56 AM.png')


# Invert the mask

def zoom_at(img, zoom=1, angle=0, coord=None):
    
    cy, cx = [ i/2 for i in img.shape[:-1] ] if coord is None else coord[::-1]
    rot_mat = cv2.getRotationMatrix2D((cx,cy), angle, zoom)
    result = cv2.warpAffine(img, rot_mat, img.shape[1::-1], flags=cv2.INTER_LINEAR)
    
    return result



x = 500
y = 500
w = 300
h = 300
coord = (w, h)
angle=0
zoom = 1.5


cv2.rectangle(frame, (x-w, y-h), (x + w, y + h), (0, 0, 0), 1)

# step 1: cropped a frame around the coord you wont to zoom into
zoomedframe = frame[y-w:y+w , x-h:x+h] 


# step 2: zoom into the zoomed frame a certain zoom amount

rot_mat = cv2.getRotationMatrix2D((w,h), angle, zoom)
zoomedframe = cv2.warpAffine(zoomedframe, rot_mat, zoomedframe.shape[1::-1], flags=cv2.INTER_LINEAR)

#step 3: replace the original cropped frame with the new zoomed in cropped frame
frame[y-w:y+w , x-h:x+h] = zoomedframe

cv2.imshow("final_image", frame)


cv2.waitKey(0)
cv2.destroyAllWindows()

# To save the image:

