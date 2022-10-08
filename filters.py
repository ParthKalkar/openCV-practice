# import modules
import cv2
import numpy as np


# import image
img = cv2.imread('nature.jpg')


# form the filter
kernel_identity = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
kernel_3 = np.ones((3,3), dtype=np.float32)/9.0
kernel_5 = np.ones((5,5), dtype=np.float32)/25.0
kernel_7 = np.ones((7,7), dtype=np.float32)/49.0

# apply the filter
output_id = cv2.filter2D(img, -1, kernel_identity)
output_3 = cv2.filter2D(img, -1, kernel_3)
output_5 = cv2.filter2D(img, -1, kernel_5)
output_7 = cv2.filter2D(img, -1, kernel_7)

# show the image
cv2.imshow('Input', img)
cv2.imshow('Output_id', output_id)
cv2.imshow('Output_3', output_3)
cv2.imshow('Output_5', output_5)
cv2.imshow('Output_7', output_7)

if cv2.waitKey() == ord('q'):
    cv2.destroyAllWindows()
