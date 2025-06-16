import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
dirname = os.path.dirname(__file__)
image_relative_1 = os.path.join(dirname, 'shutterstock147979985--250.jpg')
image_relative_2 = os.path.join(dirname, 'PortfolioMilestone1Image.jpg')

image_1 = cv2.imread(image_relative_1)
image_2 = cv2.imread(image_relative_2)

image_1[image_1[:, :, 1:].all(axis=-1)] = 0
image_2[image_2[:, :, 1:].all(axis=-1)] = 0

dst = cv2.addWeighted(image_1, 1, image_2, 1, 0)



cv2.imshow("This is me", dst)
cv2.waitKey(0)


