import cv2
import numpy as np

img = cv2.imread('noisy.jpg')
rows, cols = img.shape[:2]

# kernel blue using filter2D operation
kernel_25 = np.ones((25, 25), np.float32)/625.0
output_kernel = cv2.filter2D(img, -1, kernel_25)

# box filter and blur function 
output_blur = cv2.blur(img, (25, 25))
output_box = cv2.boxFilter(img, -1, (5, 5), normalize=True)

# GaussianBlur
output_gaussian = cv2.GaussianBlur(img, (5, 5), 0)

# MedianBlur - better when reducing noise 
output_median = cv2.medianBlur(img, 5)

# BilateralBlur (reduction of noise + preserving edges)
output_bilateral = cv2.bilateralFilter(img, 5, 6, 6)


# show images 
cv2.imshow('Original image', img)
cv2.imshow('kernel_25', output_kernel)
cv2.imshow('box', output_box)
cv2.imshow('blur', output_blur)
cv2.imshow('median_blur', output_median)
cv2.imshow('gaussian_blur', output_gaussian)
cv2.imshow('bilateral_blur', output_bilateral)

# close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
