import cv2
import numpy as np


# load image 
image = cv2.imread('nature.jpg')

# translation matrix
matrix = np.float32([[1, 0, 100], [0, 1, 100]])

# apply translation
translated = cv2.warpAffine(image, matrix, (image.shape[1]+100, image.shape[0]+100))

# showing the image
cv2.imshow('image', image)
cv2.imshow('translated', translated)
if cv2.waitKey() == ord('q'):
    cv2.destroyAllWindows()
