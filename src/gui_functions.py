from tkinter import *
from tkinter import messagebox as mb
from PIL import ImageDraw, Image
from src.Predict_input import predict_class
import sys

##Button:
def delete(cv, e):
    cv.delete(ALL)
    e.delete(0,END)
    

def save_predict(imag,e, model):
    filename = "./OUTPUT/image.jpg"
    imag.save(filename)
    mb.showinfo("Info", "You're image have been saved")
    prediction = predict_class(model, "./OUTPUT/image.jpg")
    e.insert(0, prediction)

def paint(event, cv, draw):
    # python_green = "#476042"
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    cv.create_oval(x1, y1, x2, y2, fill="black",width=8)
    draw.line([x1, y1, x2, y2],fill="black",width=8)

def exit():
    sys.exit()