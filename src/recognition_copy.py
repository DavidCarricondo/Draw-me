import cv2
import numpy as np

from src.utils import *

def cam(substitute = True):
    face_cascade = cv2.CascadeClassifier('./src/models/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('./src/models/haarcascade_eye.xml')
    nose_cascade = cv2.CascadeClassifier('./src/models/haarcascade_mcs_nose.xml')

    cap = cv2.VideoCapture(0)

    #Pictures to add to the video
    img_face = open_img('face')
    img_eye = open_img('eye')
    img_nose = open_img('nose')
        
    while True:
        ret, img = cap.read()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      
        #img_h, img_w, img_c = img.shape
        #Create overlay with B,G,R and alpha channels:
        #overlay = np.zeros((img_h, img_w, 4), dtype = 'uint8')
        #overlay[100:250, 100:125] = (255, 255,0, 1)
        #overlay[100:250, 150:255] = (0, 255, 0, 1)
        #cv2.imshow('overlay', overlay)

        
        #for i in range(0, pict_h):
        #    for j in range(0, pict_w):
        #        overlay[i+150, j+100] = pict_resize[i, j]

        #WIthout alpha
        #x_start= 50
        #y_start= 150
        #img[y_start:y_start+pict_h, x_start:x_start+pict_w] = pict_resize
        
        #cv2.addWeighted(overlay, 0.75, img, 1.0, 0, img)
        #cv2.imshow('gray', img)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for  (x,y,w,h) in faces:
            #font = cv2.FONT_HERSHEY_COMPLEX
            #cv2.putText(img,'Face',(x+w,y+h),font,1,(250,250,250),2,cv2.LINE_AA)
            if substitute==True:
                pass
            else:
                cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            nose = nose_cascade.detectMultiScale(roi_gray)
            
            #Within eyes rectangle:
            for (ex, ey, ew, eh) in eyes:
                if substitute==True:
                    if len(img_eye)!=0:
                        img_eye = image_resize(img_eye, width=ew, height=eh)
                        eye_h, eye_w, eye_c = img_eye.shape
                        roi_color[ey:ey+eye_h, ex:ex+eye_w] = img_eye
                else:
                    cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
            
            #Within nose rectangle:   
            for (sx, sy, sw, sh) in nose:
                if substitute == True:
                    if len(img_nose)!=0:
                        img_nose = image_resize(img_nose, width=sw, height=sh)
                        nose_h, nose_w, nose_c = img_nose.shape
                        roi_color[sy:sy+nose_h, sx:sx+nose_w] = img_nose
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
