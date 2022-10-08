import cv2 
import numpy as np

# scaling operations
# reading original image
image = cv2.imread('small.jpg')

# resize image
image_sized = cv2.resize(image, (640, 480))


# resize image using linear interpolation
image_re_linear = cv2.resize(image, None, fx=5.5, fy=5.5, interpolation=cv2.INTER_LINEAR)

# resize image using cubic interpolation
image_re_cubic = cv2.resize(image, None, fx=3.0, fy=3.0, interpolation=cv2.INTER_CUBIC)

# showing all images
cv2.imshow('original', image)
cv2.imshow('re_linear', image_re_linear)
cv2.imshow('re_cubic', image_re_cubic)
cv2.imshow('sized', image_sized)

if cv2.waitKey(0) == ord('q'):
    cv2.destroyAllWindows()
