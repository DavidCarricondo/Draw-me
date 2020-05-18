from tkinter import *
from PIL import Image, ImageDraw
import PIL
from src.gui_functions import *
from src.recognition_copy import *
from tkinter import messagebox as mb
from keras.models import load_model

def main():

    #Load model:
    #Maybe I have to move this to the main.py...
    model = load_model('./OUTPUT/model_sketch_extended_v2.h5') #_extended

    root = Tk()
    root.title('Draw on me!!')
    #root.bind("<Escape>", root.quit)

    e = Entry(root, width=35, borderwidth=5, text='Your prediction')
    e.grid(row=4, column=1)

    # Create an empty PIL image to draw on it.
    image1 = PIL.Image.new("RGB", (350, 350), (255,255,255))
    #image1 = PIL.Image.open('./OUTPUT/canvas.jpg')
    draw = ImageDraw.Draw(image1)

    ##Labels for location
    myLabel1 = Label(root, text = '')
    myLabel2 = Label(root, text = '')

    myLabel1.grid(row=0, column=0)
    myLabel2.grid(row=0, column=5)

    #Create canvas paint:
    cv = Canvas(root, width=350, height=350, bg='white')
    cv.grid(row=1, column=0, columnspan=3, rowspan=3)
    cv.bind("<B1-Motion>", lambda x: paint(event=x, cv=cv, draw=draw))

    
    #Picture canvas:
    #cv2 = Canvas(root, width=700, height=700, bg='white')
    #cv2.grid(row=1, column=5, columnspan=3)

    #img = PhotoImage(file="./OUTPUT/sample.png")
    #cv2.create_image(70,70, anchor=NW, image=img)

    #Buttons    
    button = Button(root, text = 'Ready!!', padx=25, pady=15, command=lambda: save_predict(image1, e, model))
    button.grid(row=4, column=0)

    button2 = Button(root, text = 'Reset', padx=25, pady=15, command=lambda: delete(cv, e, draw))
    button2.grid(row=4, column=2)

    button3 = Button(root, text = 'Exit', padx=25, pady=15, command=root.quit)
    button3.grid(row=5, column=1 )

    button4 = Button(root, text = 'Features cam', padx=25, pady=15, command=lambda:cam(substitute=False))
    button4.grid(row=2, column=3 )

    button5 = Button(root, text = 'Drawing cam', padx=25, pady=15, command=lambda:cam(substitute=True))
    button5.grid(row=3, column=3 )

    root.mainloop()

if __name__=='__main__':
    main()