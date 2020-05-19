import cv2
import numpy as np
from src.utils import *

##NOTE FOR MY FUTURE ME: IN CV2 THE Y AXIS GOES INCREASINGLY FROM THE TOP --> DOWN.

def cam(substitute = True, transparency = 0):
    face_cascade = cv2.CascadeClassifier('./src/models/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('./src/models/haarcascade_eye.xml')
    nose_cascade = cv2.CascadeClassifier('./src/models/haarcascade_mcs_nose.xml')

    cap = cv2.VideoCapture(0)

    #Pictures to add to the video
    img_eye = open_img('eyes', test=False)
    img_nose = open_img('nose', test=False)
    img_hat = open_img('hat', test=False)
        
    while True:
        ret, img = cap.read()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      
        img_h, img_w, img_c = img.shape

        faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.3, minNeighbors = 5)
        for  (x,y,w,h) in faces:
            #font = cv2.FONT_HERSHEY_COMPLEX
            #cv2.putText(img,'Face',(x+w,y+h),font,1,(250,250,250),2,cv2.LINE_AA)
            
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor = 1.03, minNeighbors = 5)
            nose = nose_cascade.detectMultiScale(roi_gray, scaleFactor = 2, minNeighbors = 7)
            
            ###Hats:
            if substitute==True:
                if len(img_hat)!=0:
                    hat = image_resize(img_hat, width=w)
                    hat_h, hat_w, hat_c = hat.shape
                    if y-hat_h > 0:
                        if transparency==1:
                            for i in range(y-hat_h, y):
                                for e in range(x,x+w):
                                    if hat[i-y, e-x, 3] != 0:
                                        img[i,e] = hat[i-y, e-x]
                        else:                    
                            img[y-hat_h:y, x:x+w] = hat
            else:
                cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
            
            #Within eyes rectangle:
            for (ex, ey, ew, eh) in eyes:
                if substitute==True:
                    if len(img_eye)!=0:
                        eye = image_resize(img_eye, width=ew, height=eh)
                        eye_h, eye_w, eye_c = eye.shape
                        if transparency==1:
                            for i in range(ey, ey+eye_h):
                                for e in range(ex,ex+eye_w):
                                    if eye[i-ey, e-ex, 3] != 0:
                                        roi_color[i,e] = eye[i-ey, e-ex]
                        else:
                            roi_color[ey:ey+eye_h, ex:ex+eye_w] = eye
                else:
                    cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
            
            #Within nose rectangle:   
            for (sx, sy, sw, sh) in nose:
                if substitute == True:
                    if len(img_nose)!=0:
                        nose = image_resize(img_nose, width=sw, height=sh)
                        nose_h, nose_w, nose_c = nose.shape
                        if transparency==1:
                            for i in range(sy, sy+nose_h):
                                for e in range(sx,sx+nose_w):
                                    if nose[i-sy, e-sx, 3] != 0:
                                        roi_color[i,e] = nose[i-sy, e-sx]
                        else:    
                            roi_color[sy:sy+nose_h, sx:sx+nose_w] = nose
                        
                else:
                    cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 0, 255), 2)

             # if substitute==True:
             #     pict_resize  = image_resize(pict, width=w)
             #     pict_h, pict_w, pict_c = pict_resize.shape
             #     img[y:y+pict_h, x:x+pict_w] = pict_resize

        cv2.imshow('img', img)
        #cv2.imshow('pict_resized', pict_resized)
        k = cv2.waitKey(1) & 0xff
        if k == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
