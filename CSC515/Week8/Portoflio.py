import cv2
import numpy as np
import matplotlib.pyplot as plt

import os

dirname = os.path.dirname(__file__)
image_relative_multiple = os.path.join(dirname, 'Multiple.jpg')
image_relative_bad_light = os.path.join(dirname, 'BadLight.jpg')
image_relative_fullbody_far = os.path.join(dirname, 'FullBodyFar.jpg')


img_bad_light = cv2.imread(image_relative_bad_light)
img_multiple = cv2.imread(image_relative_multiple)
img_full_far = cv2.imread(image_relative_fullbody_far)


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')

# Takes a an image of a face and returns the (x, y, w, h) of the eyes
def find_eyes(image):
    eye_image = image.copy()
    eye_square = eye_cascade.detectMultiScale(eye_image, scaleFactor=1.2, minNeighbors=2)
    return eye_square

# Takes the image of a face, the original image and the blur intensity and blurs the eyes 
def find_and_blur_eyes(face, img, blur_intensity):
    x = face[0]
    y = face[1]
    w = face[2]
    h = face[3]    
    img_face = img[y:y+h, x:x+w]
    
    eye_rect = find_eyes(img_face)
    for (x, y, w, h) in eye_rect:
        region_to_blur = img_face[y:y+h, x:x+w]
        region_blur = cv2.blur(region_to_blur,ksize=(blur_intensity,blur_intensity))
        img_face[y:y+h, x:x+w] = region_blur
    return img_face

#### Multiple subjects ####
def find_face_multiple(image):
    face_image = image.copy()
    face_square = face_cascade.detectMultiScale(face_image, scaleFactor=1.1, minNeighbors=5, minSize=(100,100)) 
    return face_square

img_multiple_blur = img_multiple.copy()
faces = find_face_multiple(img_multiple_blur) 

# Iterate through each face and add them back to the original image
for face in faces:
    img = find_and_blur_eyes(face, img_multiple_blur, 20)
    x = face[0]
    y = face[1]
    w = face[2]
    h = face[3]
    img_multiple_blur[y:y+h, x:x+w] = img


#### Bad Lighting ####
def find_face_bad_light(image):
    face_image = image.copy()
    face_square = face_cascade.detectMultiScale(face_image, scaleFactor=1.1, minNeighbors=2, minSize=(400,400)) 
    return face_square

img_bad_light_blur = img_bad_light.copy()
bad_light_face = find_face_bad_light(img_bad_light_blur)
bad_light_face_only = find_and_blur_eyes(bad_light_face[0], img_bad_light_blur, 60)


#### Full body and far ####
def find_face_fullbody_far(image):
    face_image = image.copy()
    face_square = face_cascade.detectMultiScale(face_image, scaleFactor=1.1, minNeighbors=5, minSize=(100,100)) 
    return face_square

img_full_far_blur = img_full_far.copy()
full_far_face = find_face_fullbody_far(img_full_far_blur)
full_far_img_post = find_and_blur_eyes(full_far_face[0], img_full_far_blur, 10)



#=========Image Display=========#
fig, axes = plt.subplots(3, 2, figsize=(20, 10)) # 3 row, 2 columns

axes[0, 0].imshow(cv2.cvtColor(img_full_far, cv2.COLOR_BGR2RGB))
axes[0, 0].set_title('Original')

axes[0, 1].imshow(cv2.cvtColor(full_far_img_post, cv2.COLOR_BGR2RGB))
axes[0, 1].set_title('Blurred Eyes')

axes[1, 0].imshow(cv2.cvtColor(img_bad_light, cv2.COLOR_BGR2RGB))
axes[1, 0].set_title('Original')

axes[1, 1].imshow(cv2.cvtColor(img_bad_light_blur, cv2.COLOR_BGR2RGB))
axes[1, 1].set_title('Blurred Eyes')

axes[2, 0].imshow(cv2.cvtColor(img_multiple, cv2.COLOR_BGR2RGB))
axes[2, 0].set_title('Original')

axes[2, 1].imshow(cv2.cvtColor(img_multiple_blur, cv2.COLOR_BGR2RGB)) 
axes[2, 1].set_title('Blurred Eyes')


for i in range(3):
    for j in range(2):
        axes[i, j].axis("off") 

plt.tight_layout()
plt.show()
