import cv2

image = cv2.imread("Pahse 1\insta.jpeg")

if image is not None:
    success = cv2.imwrite("output.png",image)  
    if success:
        print("image saves successfully")
    else:
        print("failed to save image")
else:
    print("Error: Could not load Image")