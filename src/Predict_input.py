import src.preprocessing_input_sketch.py as pi
from keras.models import load_model
import numpy as np
from PIL import Image

#Load model:
#Maybe I have to move this to the main.py...
model = load_model('./OUTPUT/model_scketch_extended.h5') 

def predict_class(model=model):
    #Load and preprocess input
    im = pi.process_input('./INPUT/image.jpg')

    #predict the class
    pred = model.predict(im)

    #format prediction
    classes = ['ejeglasses', 'eyes', 'hat', 'mouth', 'nose']
    ind = np.where(pred==max(pred))[0][0]

    return classes[ind]
