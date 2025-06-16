import numpy as np

import cv2
import os
import matplotlib.pyplot as plt
dirname = os.path.dirname(__file__)
image_relative = os.path.join(dirname, 'Mod4CT1.jpg')

# Read image
img = cv2.imread(image_relative)

kernel_sizes = [(3,3), (5,5), (7,7)]
sigma_1 = 2
sigma_2 = 8
blurs = []
for kernel_size in kernel_sizes:
    # Mean filtered
    mean_blur_5 = cv2.blur(img, kernel_size)

    # Median filtered
    median_blur_5 = cv2.medianBlur(img, kernel_size[0])

    # Gaussian filtered with variable sigma
    gaus_blue_5_1 = cv2.GaussianBlur(img, kernel_size, sigma_1)
    gaus_blue_5_2 = cv2.GaussianBlur(img, kernel_size, sigma_2)
    blurs.append([mean_blur_5, median_blur_5, gaus_blue_5_1, gaus_blue_5_2])

fig, axes = plt.subplots(len(kernel_sizes), len(blurs[0]), figsize=(10, 5)) # 1 row, 2 columns

for i in range(len(blurs)):
    for j in range(len(blurs[i])):
        axes[i, j].imshow(cv2.cvtColor(blurs[i][j], cv2.COLOR_BGR2RGB)) # Convert because OpenCV uses BGR order

        # Hide uneeded tick values on each image
        axes[i, j].set_yticklabels([])
        axes[i, j].set_xticklabels([])


col_titles = ["Mean Filtered", "Median Filtered", r"Gaussian Filtered $\sigma$ = " + str(sigma_1), r"Gaussian Filtered $\sigma$ = " + str(sigma_2)] 
row_titles = ["3x3 Kernel", "5x5 Kernel", "7x7 Kernel"]       
for ax, col in zip(axes[0], col_titles):
    ax.set_title(col)

for ax, row in zip(axes[:,0], row_titles):
    ax.set_ylabel(row, size='large')

fig.tight_layout()
plt.show()