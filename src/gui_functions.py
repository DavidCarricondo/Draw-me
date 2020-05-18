from tkinter import *
from tkinter import messagebox as mb
from PIL import ImageDraw, Image
from src.Predict_input import predict_class
import os
import cv2
import numpy as np
#import sys

##Button:
def delete(cv, e, draw):
    """Reset the canvas and the picture and removes the previous prediction"""
    e.delete(0,END)
    #Delete image in the canvas:
    cv.delete(ALL)
    #Delete content in the image by redrawing a white rectangle covering the whole area
    draw.rectangle([(0,0),(350,350)], fill=(255,255,255))
    
def save_predict(imag,e, model):
    """Use the model to predict the drawing and saves the image"""
    imag.save("./OUTPUT/pred.jpg")
    obj, prediction = predict_class(model, "./OUTPUT/pred.jpg")
    text = obj.upper() + ' Accuracy:' + str(round(prediction, 2) * 100) + '%'
    e.insert(0, text)
    name = e.get()

    """
    Trying transparency:
    ig = cv2.imread('./OUTPUT/pred.jpg')
    iga = cv2.cvtColor(ig, cv2.COLOR_BGR2BGRA)
    white = np.all(ig == [255, 255, 255], axis=-1)
    iga[white, -1] = 0
    cv2.imwrite('./OUTPUT/test.jpg', iga)
    """

    filename = f"./OUTPUT/{obj}.jpg"
    #filename = "./OUTPUT/image.jpg"
    imag.save(filename)
    mb.showinfo("Info", "You're image have been saved")
    

def paint(event, cv, draw):
    """Paints both in the canvas and in the picture by drawing ovales and lines respectivelly"""
    # python_green = "#476042"
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    cv.create_oval(x1, y1, x2, y2, fill="black",width=12)
    draw.line([x1, y1, x2, y2],fill="black",width=12)

def exit(root):
    classes = ['eyeglasses', 'eyes', 'hat', 'mouth', 'nose', 'pred']
    for e in classes:
        if os.path.exists(f"./OUTPUT/{e}.jpg"):
            os.remove(f"./OUTPUT/{e}.jpg")
    root.quit()

