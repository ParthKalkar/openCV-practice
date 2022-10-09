import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('nature.jpg')
b, g, r = cv2.split(image)

image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

h, s, v = cv2.split(image_hsv)

v = cv2.equalizeHist(v)
merged_hsv = cv2.merge([h, s, v]) 

bgr_enhanced = cv2.cvtColor(merged_hsv, cv2.COLOR_HSV2BGR)

cv2.imshow('Original image', image)

cv2.imshow('Enhanced image', bgr_enhanced)
hist = cv2.calcHist([b], [0], None, [256], [0, 256])
plt.plot(hist)

hist = cv2.calcHist([g], [0], None, [256], [0, 256])
plt.plot(hist)

hist = cv2.calcHist([r], [0], None, [256], [0, 256])
plt.plot(hist)

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

