from tkinter import *

root = Tk()

myLabel1 = Label(root, text = 'Here comes the paint')
myLabel2 = Label(root, text = 'Here comes the webcam')

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=0, column=1)

##Button:
def myClick():
    dosome = Label(root, text = 'I do not do nothing yet :(')
    dosome.grid(row=2 , column=0)
    
button = Button(root, text = 'Ready!!', padx=25, pady=15, command=myClick)
button.grid(row=1, column=0)


root.mainloop()