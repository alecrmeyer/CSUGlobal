import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

dirname = os.path.dirname(__file__)
image_relative = os.path.join(dirname, 'barnaby-fingerprint.jpg')
img = cv2.imread(image_relative)

(thresh, binary_img) = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
binary_img = (255-binary_img) #Invert so that fingerprint is in foreground
kernel = np.ones((5,5),np.uint8)

erosion = cv2.erode(binary_img,kernel,iterations = 1)
dilation = cv2.dilate(binary_img,kernel,iterations = 1)
opening = cv2.morphologyEx(binary_img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(binary_img, cv2.MORPH_CLOSE, kernel)

fig, axes = plt.subplots(2, 2, figsize=(10, 5)) # 2 row, 2 columns

#=========Image Display=========#
# Display the blue channel image
axes[0, 0].imshow(erosion)
axes[0, 0].set_title('Erosion')

# Display the green channel image
axes[0, 1].imshow(dilation)
axes[0, 1].set_title('Dilation')

# Display the red channel image
axes[1, 0].imshow(opening)
axes[1, 0].set_title('Opening')

# Display the blue color image
axes[1, 1].imshow(closing) 
axes[1, 1].set_title('Closing')

for i in range(2):
    for j in range(2):
        axes[i, j].axis("off") 

plt.tight_layout()
plt.show()

