import cv2 as cv


haar=cv.CascadeClassifier('haarcascade_frontalface_default.xml')

capture= cv.VideoCapture(0) #webcam par default
capture.set(3,640)
capture.set(4,480)
capture.set(10,100)
minArea=500
color=(255,0,0)
while True:
    #read frames from a camera
    isTrue, frame=capture.read()

    #convert each frame to gray scale
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    #detect daces of different sizes
    faces_rect=haar.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=9)
    
    for (x,y,w,h) in faces_rect:

        #Draw rectangle in a face
        cv.rectangle(frame,(x,y),(x+w,y+h),color,thickness=2)
        #Put the text
        cv.putText(frame,'Face',(x,y-5),cv.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,0),2)
    cv.imshow('Video',frame)
    if cv.waitKey(10) & 0xFF==ord('d'):
        break

#release capture and destroy all the windows
capture.release()
cv.destroyAllWindows() 



#haar cascade are really sensitive to noises in a image
#if we want to detect it in a video we needt to do it for each frame
