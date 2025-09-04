"""
1- cv2.bitwise_and(img1, img2)
2- cv2.bitwise_or(img1, img2)
3- cv2.bitwise_not(img1)

* img1 img2 height width same
** use only black and white
*** 
"""


import cv2
import numpy as np

img1 = np.zeros((300,300), dtype='uint8')
img2 = np.zeros((300,300), dtype='uint8')

cv2.circle(img1, (150,150), 100, 255, -1)
cv2.rectangle(img2, (100,100),(250,250) , 255, -1)

betwise_and = cv2.bitwise_and(img1,img2)
betwise_or = cv2.bitwise_or(img1,img2)
betwise_not = cv2.bitwise_not(img1,img2)

cv2.imshow('circle',img1)
cv2.imshow('Rectangle',img2)
cv2.imshow('betwise_and',betwise_and)
cv2.imshow('betwise_or',betwise_or)
cv2.imshow('betwise_not',betwise_not)

cv2.waitKey(0)
cv2.destroyAllWindows()