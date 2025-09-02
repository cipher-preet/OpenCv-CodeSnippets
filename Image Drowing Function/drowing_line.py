import cv2

image = cv2.imread("../Pahse 1/download.jpg")

if image is None:
    print("image is not showns")
else:
    print("image load successfully")
    
    pt1 = (50,90)
    pt2 = (200,300)
    color = (255,0,0) 
    thickness = 20
    
    cv2.line(image,pt1,pt2,thickness)
    
    cv2.imshow("line drawing",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()