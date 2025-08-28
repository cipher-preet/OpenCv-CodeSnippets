import cv2

image = cv2.imread("Pahse 1\insta.jpeg")

if image is not None:
    h,w,c = image.shape
    print(f"\n{h}\n{w}\n{c}")
else:
    print("could not load image")