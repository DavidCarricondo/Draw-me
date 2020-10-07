from tkinter import *
from PIL import Image, ImageDraw, ImageTk
import PIL
from src.gui_functions import *
from src.recognition import *
from tkinter import messagebox as mb
from keras.models import load_model


def main():

    #Load model:
    model = load_model('./src/models/model_sketch_revisit.h5') 
    
    root = Tk()
    root.geometry('700x520')
    root.title('Draw on me!!')
    #Shut down on escape
    root.bind('<Escape>', lambda e: exit(root))

    #Bckground picture canvas:
    cv_back = Canvas(root)
    img = ImageTk.PhotoImage(Image.open("./INPUT/background.gif"))
    cv_back.create_image(0,0, anchor=NW, image=img)
    cv_back.place(x=0, y=0, relwidth=1.5, relheight=1)#grid(row=0, column=0, columnspan=3, rowspan=5)

    e = Entry(root, width=45, borderwidth=5)
    e.insert(0, 'Your prediction will appear here')
    e.grid(row=4, column=1)

    # Create an empty PIL image to draw on it.
    image1 = PIL.Image.new("RGB", (350, 350), (255,255,255))
    #image1 = PIL.Image.open('./OUTPUT/canvas.jpg')
    draw = ImageDraw.Draw(image1)

    ##Labels for location
    myLabel1 = Label(root, text = 'Draw here your feature!!', bd=5,bg="#898989", font='Helvetica 16 bold')
    myLabel2 = Label(root, text = '')

    myLabel1.grid(row=0, column=1)
    myLabel2.grid(row=0, column=3)

    var = IntVar()

    #Create canvas paint:
    cv = Canvas(root, width=350, height=350, borderwidth=2, bg='#dedad9')
    cv.grid(row=1, column=0, columnspan=3, rowspan=3)
    cv.bind("<B1-Motion>", lambda x: paint(event=x, cv=cv, draw=draw))
   
    #Buttons

    button = Button(root, text = 'Ready!!', font='Helvetica 12 bold', padx=25, pady=15, bd=5,bg="#898989", command=lambda: save_predict(image1, e, model))
    button.grid(row=4, column=0)

    button2 = Button(root, text = 'Clear', font='Helvetica 12 bold', padx=25, pady=15, bd=5,bg="#898989", command=lambda: delete(cv, e, draw))
    button2.grid(row=4, column=2)

    button3 = Button(root, text = 'Exit', font='Helvetica 12 bold', padx=15, pady=5, bd=5,bg="#ff0000", command=lambda: exit(root))
    button3.place(x=630, y=480)

    button4 = Button(root, text = 'Features cam', font='Helvetica 12 bold', padx=25, pady=15, bd=5,bg="#898989", command=lambda:cam(substitute=False))
    button4.place(x=525, y=100)

    button5 = Button(root, text = 'Drawing cam', font='Helvetica 12 bold', padx=25, pady=15, bd=5,bg="#898989", command=lambda:cam(substitute=True, transparency=var.get()))
    button5.place(x=525, y=200)

    button6 = Button(root, text = 'Reset', font='Helvetica 12 bold', padx=25, pady=15, bd=5,bg="#898989", command=lambda:exit(root, reset=True))
    button6.grid(row=5, column=1)

    check = Checkbutton(root, text='Only trace', padx=5, pady=5, font='Helvetica 11 bold', bd=5, bg="#898989", variable=var)
    check.place(x=540, y=280)

    root.mainloop()

if __name__=='__main__':
    main()