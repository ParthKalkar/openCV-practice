# imports
import cv2
import numpy as np

# loading images and converting them to grayscale
image = cv2.imread('nature.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# performing the edge detection
gradients_sobelx = cv2.Sobel(image, -1, 1, 0)
gradients_sobely = cv2.Sobel(image, -1, 0, 1)
gradients_sobelxy = cv2.addWeighted(gradients_sobelx, 0.5, gradients_sobely, 0.5, 0)

gradients_laplacian = cv2.Laplacian(image, -1)

canny_output = cv2.Canny(image, 80, 150)

# display images
cv2.imshow('canny', canny_output)
cv2.imshow('gradients_laplacian', gradients_laplacian)
cv2.imshow('gradients_sobelx', gradients_sobelx)
cv2.imshow('gradients_sobely', gradients_sobely)   
cv2.imshow('gradients_sobelxy', gradients_sobelxy)


cv2.waitKey(0)
cv2.destroyAllWindows()
