import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
dirname = os.path.dirname(__file__)
image_relative = os.path.join(dirname, 'Discussion2_image.jpg')

image = cv2.imread(image_relative)



# Grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Rotate
height, width = image.shape[:2]
center = (width/2, height/2)
degree = -12
scale = 0.8
alpha = np.cos(np.deg2rad(degree))*scale
beta = np.sin(np.deg2rad(degree))*scale
rotation_vector = np.float32([[alpha, beta, (1-alpha)*center[0]-beta*center[1]], [-beta, alpha, (beta*center[0]+(1-alpha)*center[1])]])
print(rotation_vector)
rotated_image = cv2.warpAffine(gray_image, rotation_vector, (gray_image.shape[1], gray_image.shape[0]))

# Crop
cropped_image = rotated_image[15:82, 66:103]
print(image.shape)


fig, axes = plt.subplots(1, 4, figsize=(10, 5)) # 1 row, 2 columns

# Display the first image
axes[0].imshow(image, cmap='gray')
axes[0].set_title('Original')
axes[0].axis('off') # Hide axes ticks and labels

# Display the first image
axes[1].imshow(gray_image, cmap='gray')
axes[1].set_title('Grayscale')
axes[1].axis('off') # Hide axes ticks and labels

# Display the second image
axes[2].imshow(rotated_image, cmap='gray')
axes[2].set_title('Scaled and Rotated')
axes[2].axis('off')

axes[3].imshow(cropped_image, cmap='gray')
axes[3].set_title('Cropped')
axes[3].axis('off')

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()



