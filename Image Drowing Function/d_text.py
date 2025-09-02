import cv2

image = cv2.imread("../Pahse 1/download.jpg")

if image is None:
    print("image is not showns")
else:
    print("image load successfully")
    
    cv2.putText(image,"ghello Open Cv",(50,300),cv2.FONT_HERSHEY_DUPLEX,1.2,(255,0,0),2)
    
    
    cv2.imshow("Adding text To image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()