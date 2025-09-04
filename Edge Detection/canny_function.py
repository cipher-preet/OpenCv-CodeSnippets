import cv2

img = cv2.imread("image.png", cv2.IMREAD_GRAYSCALE)

edges = cv2.Canny(img,50,150)

cv2.imshow("original image",img)
cv2.imshow("edges",edges)

cv2.waitKey(0)
cv2.destroyAllWindows()