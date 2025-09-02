import cv2

image = cv2.imread("../Pahse 1/download.jpg")

if image is None:
    print("image is not showns")
else:
    print("image load successfully")
    
    pt1 = (50,50)
    pt2 = (250,200)
    
    color = (0,0,255)
    thickness = 3
    
    cv2.rectangle(image,pt1,pt2,color)
    
    cv2.imshow("rectangle drawing",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()