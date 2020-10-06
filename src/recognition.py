import cv2
import numpy as np
from src.utils import *

##NOTE FOR MY FUTURE ME: IN CV2 THE Y AXIS GOES INCREASINGLY FROM THE TOP --> DOWN.

def trackbars(x):
    pass

def cam(substitute = True, transparency = 0):
    """
    Recognize and substitute a haar feature by a corresponding drawing
    and tracks and redraw the object with the cam movement
    """
    face_cascade = cv2.CascadeClassifier('./src/models/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('./src/models/haarcascade_eye.xml')
    nose_cascade = cv2.CascadeClassifier('./src/models/haarcascade_mcs_nose.xml')
    mouth_cascade = cv2.CascadeClassifier('./src/models/haarcascade_mcs_mouth.xml')

    cv2.namedWindow('img')
    cap = cv2.VideoCapture(0)

    
    #Pictures to add to the video
    img_eye = open_img('eyes', test=False)
    img_nose = open_img('nose', test=False)
    img_hat = open_img('hat', test=False)
    img_mouth = open_img('mouth', test=False)
        
    while True:
        ret, img = cap.read()
        
        img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.3, minNeighbors = 5)

        #TRack bars:
        cv2.createTrackbar('Blue', 'img', 255, 255, trackbars)
        cv2.createTrackbar('Green', 'img', 255, 255, trackbars)
        cv2.createTrackbar('Red', 'img', 255, 255, trackbars)

        b = cv2.getTrackbarPos('Blue', 'img')
        r = cv2.getTrackbarPos('Green', 'img')
        g = cv2.getTrackbarPos('Red', 'img')

        color = [b, r, g, 1]

        img_h, img_w, img_c = img.shape

        for  (x,y,w,h) in faces:
            #font = cv2.FONT_HERSHEY_COMPLEX
            #cv2.putText(img,'Face',(x+w,y+h),font,1,(250,250,250),2,cv2.LINE_AA)
            
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor = 1.03, minNeighbors = 7)
            nose = nose_cascade.detectMultiScale(roi_gray, scaleFactor = 1.5, minNeighbors = 7)
            mouth = mouth_cascade.detectMultiScale(roi_gray, scaleFactor = 2, minNeighbors = 7)

            
            ###Hats:
            if substitute==True:
                obj_swapping(image = img_hat, frame=img, x=x, y=y, h=h, w=w, transparency=transparency, color=color, top=True)
            else:
                cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
            #Within eyes rectangle:
            for (ex, ey, ew, eh) in eyes:
                if substitute==True:
                    obj_swapping(image = img_eye, frame=roi_color, x=ex, y=ey, h=eh, w=ew, transparency=transparency, color=color)
                else:
                    cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
            #Within nose rectangle:   
            for (sx, sy, sw, sh) in nose:
                if substitute == True:
                    obj_swapping(image = img_nose, frame=roi_color, x=sx, y=sy, h=sh, w=sw, transparency=transparency, color=color)
                else:
                    cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 0, 255), 2)
            #Within mouth rectangle:   
            for (mx, my, mw, mh) in mouth:
                if substitute == True:
                    obj_swapping(image = img_mouth, frame=roi_color, x=mx, y=my, h=mh, w=mw, transparency=transparency, color=color)
                else:
                    cv2.rectangle(roi_color, (mx, my), (mx+mw, my+mh), (255, 0, 255), 2)

        cv2.imshow('img', img)
        #cv2.imshow('pict_resized', pict_resized)
        k = cv2.waitKey(1) & 0xff
        if k == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
