import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
dirname = os.path.dirname(__file__)
image_relative = os.path.join(dirname, 'Selfie.JPG')

image = cv2.imread(image_relative)

### Rectangle around eyes ###
eyes_top_left = (300,850)
eyes_bot_tight = (1150, 1100)
eye_color = (0, 0, 255) # bgR as OpenCV uses inverse RGB
eye_thickness = 7
cv2.rectangle(image, eyes_top_left, eyes_bot_tight, eye_color, eye_thickness)

### Circle/ellipse around head ###
face_center = (725, 1020)
face_dim = (760, 500)

# Angle that the ellipse is rotated
face_angle = 90

# Start and end of the ellipse drawing
face_start_angle = 0
face_end_angle = 360

face_color = (0, 255, 0) # bGr as OpenCV uses inverse RGB 
face_thickness = 7
cv2.ellipse(image, face_center, face_dim, face_angle, face_start_angle, face_end_angle, face_color, face_thickness)


cv2.imshow("This is me", image)
cv2.waitKey(0)


