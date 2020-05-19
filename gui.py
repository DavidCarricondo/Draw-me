from tkinter import *
from PIL import Image, ImageDraw, ImageTk
import PIL
from src.gui_functions import *
from src.recognition import *
from tkinter import messagebox as mb
from keras.models import load_model

def main():

    #Load model:
    #Maybe I have to move this to the main.py...
    model = load_model('./src/models/model_sketch_extended_v3.h5') #_extended

    root = Tk()
    root.title('Draw on me!!')
    #root.bind("<Escape>", root.quit)

    #Picture canvas:
    cv2 = Canvas(root)
    img = ImageTk.PhotoImage(Image.open("./INPUT/background.gif"))
    cv2.create_image(0,0, anchor=NW, image=img)
    cv2.place(x=0, y=0, relwidth=1, relheight=1)#grid(row=0, column=0, columnspan=3, rowspan=5)
    """
    background_image=PhotoImage('./OUTPUT/background.jpg')
    background_label = Label(root, image=background_image)
    background_label.image = background_image
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    """
    e = Entry(root, width=35, borderwidth=5, text='Your prediction')
    e.grid(row=4, column=1)

    # Create an empty PIL image to draw on it.
    image1 = PIL.Image.new("RGB", (350, 350), (255,255,255))
    #image1 = PIL.Image.open('./OUTPUT/canvas.jpg')
    draw = ImageDraw.Draw(image1)

    ##Labels for location
    myLabel1 = Label(root, text = 'Paint here your feature!!', bd=5,bg="#898989")
    myLabel2 = Label(root, text = '')

    myLabel1.grid(row=0, column=1)
    myLabel2.grid(row=0, column=3)

    var = IntVar()

    #Create canvas paint:
    cv = Canvas(root, width=350, height=350, borderwidth=2, bg='#dedad9')
    cv.grid(row=1, column=0, columnspan=3, rowspan=3)
    cv.bind("<B1-Motion>", lambda x: paint(event=x, cv=cv, draw=draw))
   
    #Buttons    
    button = Button(root, text = 'Ready!!', padx=25, pady=15, bd=5,bg="#898989", command=lambda: save_predict(image1, e, model))
    button.grid(row=4, column=0)

    button2 = Button(root, text = 'Reset', padx=25, pady=15, bd=5,bg="#898989", command=lambda: delete(cv, e, draw))
    button2.grid(row=4, column=2)

    button3 = Button(root, text = 'Exit', padx=25, pady=15, bd=5,bg="#898989", command=lambda: exit(root))
    button3.grid(row=5, column=1 )

    button4 = Button(root, text = 'Features cam', padx=25, pady=15, bd=5,bg="#898989", command=lambda:cam(substitute=False))
    button4.grid(row=1, column=3 )

    button5 = Button(root, text = 'Drawing cam', padx=25, pady=15, bd=5,bg="#898989", command=lambda:cam(substitute=True, transparency=var.get()))
    button5.grid(row=2, column=3 )

    check = Checkbutton(root, text='Transparent features', bd=5, bg="#898989", variable=var)
    check.grid(row=3, column=3)

    root.mainloop()

if __name__=='__main__':
    main()