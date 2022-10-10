import cv2
import numpy as np

image = cv2.imread('pexels-photo-569986.png')
image = cv2.resize(image,None, fx=0.9, fy=0.9)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# converting the grayscale image to binary using threshold
ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# detect contours
contours, hierarchy = cv2.findContours(binary, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)

# visualize the data structures
print(f'Length of contours: {len(contours)}')
# print(contours)

# draw the contours on original image
image_copy = image.copy()
image_copy = cv2.drawContours(image_copy, contours, -1, (0, 255, 255), thickness=2, lineType=cv2.LINE_AA)

# visualize the results
cv2.imshow('Original', image)
cv2.imshow('Contours', image_copy)
cv2.imshow('Binary', binary)

cv2.waitKey(0)
cv2.destroyAllWindows()
