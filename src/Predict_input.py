import numpy as np
from PIL import Image


def process_input(path):
    im = Image.open(path)
    im = im.resize((28,28),Image.ANTIALIAS)
    im = np.asarray(im.convert('L'))
    im = np.array([255-i for i in im]).astype('float32') / 255
    #plt.imshow(im, cmap='gray')
    return im.reshape(1,28, 28,1)


def predict_class(model, path):
    #Load and preprocess input
    im = process_input(path)

    #predict the class
    pred = model.predict(im)

    #format prediction
    #classes = ['eyes', 'mouth', 'nose']
    classes = ['eyes', 'hat', 'mouth', 'nose']
    ind = np.where(pred[0]==max(pred[0]))[0][0]

    return classes[ind], max(pred[0])
