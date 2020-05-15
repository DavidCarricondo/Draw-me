import prep_data_functions.py as pf
import numpy as np

#Load the data by batches so you do not saturate the RAM:
mouth = np.load('./INPUT/mouth.npy')
nose = np.load('./INPUT/nose.npy')
eyes =  np.load('./INPUT/eye.npy')
eyeglasses = np.load('./INPUT/eyeglasses.npy')
hat = np.load('./INPUT/hat.npy')



sketch_data = {'mouth' : mouth,'nose': nose, 'eyes' : eyes, 'eyeglasses': eyeglasses, 'hat': hat}


X = pf.create_x(sketch_data)
y = y = pf.create_y(sketch_data)


#np.save('../../OUTPUT/X_clean.npy', X)
#np.save('../../OUTPUT/y.npy', y)