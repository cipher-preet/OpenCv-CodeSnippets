import cv2

img = cv2.imread("image.png", cv2.IMREAD_GRAYSCALE)

ret, thres_img = cv2.threshold(img,100,150,cv2.THRESH_BINARY)

cv2.imshow("original image",img)
cv2.imshow("thresholded image",thres_img)

cv2.waitKey(0)
cv2.destroyAllWindows()