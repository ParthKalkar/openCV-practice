import cv2
import numpy as np

# reading the image
image =  cv2.imread('nature.jpg')
rows, cols = image.shape[:2]

# generating vigenette mask 
kernel_x = cv2.getGaussianKernel(cols, 200)
kernel_y = cv2.getGaussianKernel(rows, 200)
kernel =  kernel_y * kernel_x.T

# normalize kernel
kernel = kernel/np.linalg.norm(kernel)

# generating mask 
mask = 255 * kernel
output = np.copy(image)

# applying the mask to each channel in the input image
for i in range(3):
    output[:,:,i] = output[:,:,i] * mask

cv2.imshow('Original image', image)
cv2.imshow('Vigenette mask', output)

cv2.waitKey(0)
cv2.destroyAllWindows()
