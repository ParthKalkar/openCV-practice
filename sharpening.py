import cv2
import numpy as np

img = cv2.imread('nature.jpg')

# GaussianBlur
gaussian_blur = cv2.GaussianBlur(img, (7, 7), 2)

# sharpening image using addweighted ()
sharpening_1 = cv2.addWeighted(img, 1.5, gaussian_blur, -0.5, 0)
sharpening_2 = cv2.addWeighted(img, 3.5, gaussian_blur, -2.5, 0)
sharpening_3 = cv2.addWeighted(img, 7.5, gaussian_blur, -6.5, 0)

# show images
cv2.imshow('original', img)
cv2.imshow('sharpening_1', sharpening_1)
cv2.imshow('sharpening_2', sharpening_2)
cv2.imshow('sharpening_3', sharpening_3)
cv2.waitKey(0)
cv2.destroyAllWindows()
