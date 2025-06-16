import cv2
import numpy as np
import matplotlib.pyplot as plt


def mse(imageA, truth):
        # The 'Mean Squared Error' between the two images is the
        # sum of the squared difference between the two images;
        # NOTE: the two images must have the same dimension
        err = np.sum((imageA.astype("float") - truth.astype("float")) ** 2)
        err /= float(imageA.shape[0] * imageA.shape[1])
        return err

height = 500
width = 800

blank_image = np.zeros((height, width, 3), dtype=np.uint8) # 3 for RGB channels

image = cv2.rectangle(blank_image, (100, 100), (300, 300), (0, 0, 255), -1)
image = cv2.circle(blank_image, (500, 300), 100, (0,255,0), -1)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blank_image_truth = np.zeros((height, width, 3), dtype=np.uint8) # 3 for RGB channels
image_truth = cv2.rectangle(blank_image_truth, (100, 100), (300, 300), (255, 255, 255), 1)
image_truth = cv2.circle(blank_image_truth, (500, 300), 100, (255,255,255), 1)
image_truth = cv2.cvtColor(image_truth, cv2.COLOR_BGR2GRAY)


#Canny
canny_orig = cv2.Canny(image, 100, 200)

#Sobel
sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
magnitude = np.sqrt(sobelx**2 + sobely**2)
sobel_orig = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

#Laplac
dst = cv2.Laplacian(image, cv2.CV_16S, ksize=3)
lapac_orig = cv2.convertScaleAbs(dst)


####### NOISY #######
mean = 0
sigma = 0.4 # Standard deviation of the noi#
noise = np.random.normal(mean, sigma, image.shape)
# Add the noise to the image
noisy_img_float = image + noise
noisy_img_float = np.uint8(noisy_img_float)
#Canny
canny_error = cv2.Canny(np.uint8(noisy_img_float), 100, 200)

#Sobel
sobelx = cv2.Sobel(noisy_img_float, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(noisy_img_float, cv2.CV_64F, 0, 1, ksize=3)
magnitude = np.sqrt(sobelx**2 + sobely**2)
sobel_error = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

#Laplac
dst = cv2.Laplacian(noisy_img_float, cv2.CV_16S, ksize=3)
lapac_error = cv2.convertScaleAbs(dst)

print(mse(lapac_error, image_truth))
# Display the image (optional)
fig, axes = plt.subplots(2, 5, figsize=(10, 5)) # 3 row, 2 columns

#=========Image Display=========#
axes[0, 0].imshow(image, cmap='gray')
axes[0, 0].set_title('Original')

axes[0, 1].imshow(image_truth, cmap='gray')
axes[0, 1].set_title('Ground Truth')

axes[0, 2].imshow(canny_orig, cmap='gray')
axes[0, 2].set_title('Original Canny\n' + str(mse(canny_orig, image_truth)))

axes[0, 3].imshow(sobel_orig, cmap='gray')
axes[0, 3].set_title('Original Sobel\n' + str(mse(sobel_orig, image_truth)))

axes[0, 4].imshow(lapac_orig, cmap='gray')
axes[0, 4].set_title('Original Laplace\n' + str(mse(lapac_orig, image_truth)))

axes[1, 0].imshow(noisy_img_float, cmap='gray') 
axes[1, 0].set_title('Noisy')

axes[1, 1].imshow(image_truth, cmap='gray')
axes[1, 1].set_title('Noisy Truth')

axes[1, 2].imshow(canny_error, cmap='gray') 
axes[1, 2].set_title('Noisy Canny\n' + str(mse(canny_error, image_truth)))

axes[1, 3].imshow(sobel_error, cmap='gray') 
axes[1, 3].set_title('Noisy Sobel\n' + str(mse(sobel_error, image_truth)))

axes[1, 4].imshow(lapac_error, cmap='gray') 
axes[1, 4].set_title('Noisy Laplace\n' + str(mse(lapac_error, image_truth)))

for i in range(2):
    for j in range(5):
        axes[i, j].axis("off") 
plt.tight_layout()
plt.show()