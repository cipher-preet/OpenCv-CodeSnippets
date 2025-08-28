import cv2

image = cv2.imread("Pahse 1\insta.jpeg")

if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray",gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
else:
    print("error")
