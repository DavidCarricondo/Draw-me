import cv2
import numpy as NotImplemented

def cam():
    face_cascade = cv2.CascadeClassifier('./src/models/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('./src/models/haarcascade_eye.xml')
    smile_cascade = cv2.CascadeClassifier('./src/models/haarcascade_smile.xml')


    cap = cv2.VideoCapture(0)

    while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for  (x,y,w,h) in faces:
            #font = cv2.FONT_HERSHEY_COMPLEX
            #cv2.putText(img,'Face',(x+w,y+h),font,1,(250,250,250),2,cv2.LINE_AA)
            cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            smile = smile_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
            for (sx, sy, sw, sh) in smile:
                cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 0, 255), 2)

        cv2.imshow('img', img)
        k = cv2.waitKey(0) & 0xff
        if k == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()