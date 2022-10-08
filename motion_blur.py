import cv2
import numpy as np

img = cv2.imread('nature.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

size = 15
kernel = np.zeros((size, size))

kernel[int((size-1)/2), :] = np.ones(size)
kernel = kernel/size

output = cv2.filter2D(img, -1, kernel)

cv2.imshow('Input', img)
cv2.imshow('Output', output)

if cv2.waitKey() == ord('q'):
    cv2.destroyAllWindows()