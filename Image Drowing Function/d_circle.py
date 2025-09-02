import cv2

image = cv2.imread("../Pahse 1/download.jpg")

if image is None:
    print("image is not showns")
else:
    print("image load successfully")
    
    cv2.circle(image,(150,150),50,(255,0,0),5)
    
    cv2.imshow("circle drawing",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()