import cv2
import os
dirname = os.path.dirname(__file__)
image_relative = os.path.join(dirname, 'PortfolioMilestone1Image.jpg')
desktop_path = os.path.expanduser('~/Desktop')

#1. Write Python code to import the following image
image = cv2.imread(image_relative)

#2. Write Python code to display the image.
cv2.imshow('image', image)
cv2.waitKey(0)

#3. Write Python code to write a copy of the image to any directory on your desktop.
cv2.imwrite(desktop_path + "/CSUGlobal/new_brain_image.jpg", image)
