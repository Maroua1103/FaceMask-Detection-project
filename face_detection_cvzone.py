from cvzone.FaceDetectionModule import FaceDetector
import cv2

cap = cv2.VideoCapture(0)
detector = FaceDetector()

while True:
    success, img = cap.read()
    img, bboxs = detector.findFaces(img)
    if bboxs:
        print(bboxs)
        box = bboxs[0]['bbox']
        cropped_image = img[   box[1]:box[1]+box[3]    ,  box[0]:box[0]+box[2] ]
                                  #height                         #width

    cv2.imshow("Image", img)
    cv2.imshow("cropped Image", cropped_image)
   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()