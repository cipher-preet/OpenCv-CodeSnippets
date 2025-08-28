import cv2

# for loadimng the Image
image = cv2.imread("Pahse 1\insta.jpeg")

if image is not None:
    cv2.imshow("Image is showing",image)  # open the window
    cv2.waitKey(0)                         # wait for a key
    cv2.destroyAllWindows()                # cloase the window
else:
    print("could not load image") 
    
    
    
    