import cv2

image = cv2.imread("../Pahse 1/insta.jpeg")

if image is None:
    print("image not found")
else:
    print("Image loadeed")
    
    resized = cv2.resize(image,(200,600))
    
    cv2.imshow("original image",image)
    cv2.imshow("Resized image",resized)
    
    cv2.imwrite("resized image.png",resized)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

