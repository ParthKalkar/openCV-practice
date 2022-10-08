import cv2
import numpy as np

# load the image
image = cv2.imread('nature.jpg')

height, width = image.shape[:2]

# translation matrix
matrix = cv2.getRotationMatrix2D((width/2, height/2), 10, 1)

# apply translation
translated = cv2.warpAffine(image, matrix, (height, width))

# showing the image
cv2.imshow('image', image)
cv2.imshow('translated', translated)
if cv2.waitKey() == ord('q'):
    cv2.destroyAllWindows()
