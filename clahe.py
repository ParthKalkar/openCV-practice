import cv2
import numpy as np

image = cv2.imread('nature.jpg')
image_bw = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# declaring clahe
# clipLimit -> threshold for contrast limiting
clahe = cv2.createCLAHE(clipLimit = 5)
final_image = clahe.apply(image_bw)

normal = cv2.equalizeHist(image_bw)
# showing all the images
cv2.imshow('original',image)
cv2.imshow('final',final_image) 
cv2.imshow('normal',normal)

cv2.waitKey(0)
cv2.destroyAllWindows()