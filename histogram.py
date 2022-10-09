import cv2  
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('nature.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

hist = cv2.calcHist([image], [0], None, [256], [0, 256])
plt.plot(hist)

image_hist = cv2.equalizeHist(image)
hist = cv2.calcHist([image_hist], [0], None,  [256], [0, 256])
plt.plot(hist)  

cv2.imshow('Original image', image)
cv2.imshow('applied histogram', image_hist)

plt.show()

cv2.waitKey (0)
cv2.destroyAllWindows()