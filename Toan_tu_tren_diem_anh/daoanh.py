import cv2
import numpy as np
# Load the image
img = cv2.imread('anh1.jpg', 0)
# Check the datatype of the image
print(img.dtype)
# Subtract the img from max value(calculated from dtype)
img_neg = 255 - img
# Show the image
cv2.imshow('negative',img_neg)
cv2.waitKey(0)