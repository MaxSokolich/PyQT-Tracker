import cv2
import numpy as np
def find_mask(frame):
        

    mask_thresh= int(128)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(frame, mask_thresh, 255, cv2.THRESH_BINARY)

    
    mask = cv2.bitwise_not(mask)

    return mask


# Read the image
image_path = '/Users/bizzarohd/Desktop/Screenshot 2023-08-08 at 10.25.56 AM.png'  # Replace with your image path
image = cv2.imread(image_path)



import cv2
import numpy as np

# Load the original image and the mask
original_image = cv2.imread('/Users/bizzarohd/Desktop/Screenshot 2023-08-08 at 10.25.56 AM.png')
mask = find_mask(original_image)

# Invert the mask
inverted_mask = cv2.bitwise_not(mask)

# Crop the desired portion from the original image
x, y, w, h = 100, 100, 200, 200
cropped_portion = original_image[y:y+h, x:x+w]
cropped_mask = find_mask(cropped_portion)

dilatedmask = cv2.dilate(mask, None, iterations=5)

# Apply the resized inverted mask to the cropped portion
#masked_cropped_portion = cv2.bitwise_and(cropped_portion, cropped_portion, mask=cropped_mask)

# Create a black canvas of the same size as the original image


# Insert the masked cropped portion back into the original image at the same location
dilatedmask[y:y+h, x:x+w] = cropped_mask

# Apply the original mask to the entire result
#final_result = cv2.bitwise_and(result, result, mask=mask)

# Display the final image
cv2.imshow("Final Image2", cropped_mask)
cv2.imshow("Final Image1", cropped_mask)

cv2.imshow("Final Image", dilatedmask)
cv2.waitKey(0)
cv2.destroyAllWindows()

# To save the image:

