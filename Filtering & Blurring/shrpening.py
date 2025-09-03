import cv2
import numpy as np

image = cv2.imread("../Pahse 1/download.jpg")

sharpen_kernal = np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
])

sharpened = cv2.filter2D(image,-1, sharpen_kernal)

cv2.imshow("original Image", image)
cv2.imshow("Sharpened Image ", sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()