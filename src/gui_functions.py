from tkinter import *
from tkinter import messagebox as mb
from PIL import ImageDraw, Image
from src.Predict_input import predict_class
import sys

##Button:
def delete(cv, e, draw):
    e.delete(0,END)
    cv.delete(ALL)
    draw.rectangle([(0,0),(350,350)], fill=(255,255,255))
    
def save_predict(imag,e, model):
    """Use the model to predict the drawing and saves the image"""
    imag.save("./OUTPUT/pred.jpg")
    prediction = predict_class(model, "./OUTPUT/pred.jpg")
    e.insert(0, prediction)
    name = e.get()
    filename = f"./OUTPUT/{name}.jpg"
    #filename = "./OUTPUT/image.jpg"
    imag.save(filename)
    mb.showinfo("Info", "You're image have been saved")
    

def paint(event, cv, draw):
    # python_green = "#476042"
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    cv.create_oval(x1, y1, x2, y2, fill="black",width=12)
    draw.line([x1, y1, x2, y2],fill="black",width=12)

