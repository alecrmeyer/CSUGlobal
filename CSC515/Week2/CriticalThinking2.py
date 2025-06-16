import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
dirname = os.path.dirname(__file__)
image_relative = os.path.join(dirname, 'shutterstock147979985--250.jpg')

image = cv2.imread(image_relative)
image_original = image.copy()

# split the n x n x 3 array into three separate n x n arrays for each BGR color 
# These will appear greyscale becasue they only have a single channel (0 - 255) 
blue_channel, green_channel, red_channel = cv2.split(image)
print("Blue channel shape: " + str(blue_channel.shape))
print("Green channel shape: " + str(green_channel.shape))
print("Red channel shape: " + str(red_channel.shape))

# Merge the three 2D channels into a single n x n x 3 array
channel_merged = np.zeros((blue_channel.shape[0], blue_channel.shape[1], 3)) # Initialize n x n x 3 array
for i in range(len(blue_channel)):
    for j in range(len(blue_channel[i])):       
        # Combine the blue, green and red channels into a 1x3 vector for each pixel
        # BGR order because it is the order opencv2 stores its color arrays
        channel_merged[i, j] = [blue_channel[i, j], green_channel[i, j], red_channel[i, j]]
channel_merged = channel_merged.astype('uint8') # Convert to opencv readable format

# [blue, 0, 0]
blue_color = image.copy()
blue_color[:,:,1] = 0
blue_color[:,:,2] = 0

# [0, green, 0]
green_color = image.copy()
green_color[:,:,0] = 0
green_color[:,:,2] = 0

# [0, 0, red]
red_color = image.copy()
red_color[:,:,0] = 0
red_color[:,:,1] = 0

# Merge in GRB order (BRG because opencv2 order) using built in merge() method
channel_merged_GRB = cv2.merge([blue_channel, red_channel, green_channel])

# Initialize sublot
fig, axes = plt.subplots(3, 3, figsize=(10, 5)) # 1 row, 2 columns

#=========Image Display=========#
# Display the blue channel image
axes[0, 0].imshow(blue_channel, cmap = 'gray')
axes[0, 0].set_title('Blue Channel')

# Display the green channel image
axes[0, 1].imshow(green_channel, cmap = 'gray')
axes[0, 1].set_title('Green Channel')

# Display the red channel image
axes[0, 2].imshow(red_channel, cmap = 'gray')
axes[0, 2].set_title('Red Channel')

# Display the blue color image
axes[1, 0].imshow(cv2.cvtColor(blue_color, cv2.COLOR_BGR2RGB)) # using cvtColor beause matplot default is RGB
axes[1, 0].set_title('Blue RGB')

# Display the green color image
axes[1, 1].imshow(cv2.cvtColor(green_color, cv2.COLOR_BGR2RGB)) 
axes[1, 1].set_title('Green RGB')

# Display the red color image
axes[1, 2].imshow(cv2.cvtColor(red_color, cv2.COLOR_BGR2RGB)) 
axes[1, 2].set_title('Red RGB')

# Display the original image
axes[2, 0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)) 
axes[2, 0].set_title('Original')

# Display the merged channel image
axes[2, 1].imshow(cv2.cvtColor(channel_merged, cv2.COLOR_BGR2RGB)) 
axes[2, 1].set_title('Channel Merged')

# Display the merged channel in GRB order image
axes[2, 2].imshow(cv2.cvtColor(channel_merged_GRB, cv2.COLOR_BGR2RGB)) 
axes[2, 2].set_title('GRB Channel Merged')

# Remove axis from images
for i in range(3):
    for j in range(3):
        axes[i, j].axis("off") 

plt.tight_layout()
plt.show()

