import cv2

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()  #ret = True/False  frame=image
    
    if not ret:
        print("could not read Frame")
        break
    
    cv2.imshow("webcam feed", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quitting...")
        break
        
    
cap.release()
cv2.destroyAllWindows()