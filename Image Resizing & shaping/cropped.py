import cv2


image = cv2.imread("Pahse 1\insta.jpeg")


if image is not None:
    
    cropped = image[200:300,100:150]
    
    cv2.imshow("original", image)
    cv2.imshow("cropped", cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()