import prep_data_functions.py as pf
import numpy as np
import random

#Load the data by batches so you do not saturate the RAM:
mouth = np.load('./INPUT/mouth.npy')
nose = np.load('./INPUT/nose.npy')
eyes =  np.load('./INPUT/eye.npy')
eyeglasses = np.load('./INPUT/eyeglasses.npy')
hat = np.load('./INPUT/hat.npy')

#TRimm the data to balance the samples. One at a time because of performance issues:
rnd_mouth = random.sample(range(len(mouth)), len(eyes))
mouth_clean = mouth[rnd_mouth]
len(mouth_clean)

rnd_nose = random.sample(range(len(nose)), len(eyes))
nose_clean = nose[rnd_nose]

rnd_hat = random.sample(range(len(hat)), len(eyes))
hat_clean = hat[rnd_hat]

rnd_eyeglasses = random.sample(range(len(eyeglasses)), len(eyes))
eyeglasses_clean = eyeglasses[rnd_eyeglasses]


sketch_data = {'mouth' : mouth_clean,'nose': nose_clean, 'eyes' : eyes, 'eyeglasses': eyeglasses_clean, 'hat': hat_clean}


X = pf.create_x(sketch_data)
y = y = pf.create_y(sketch_data)


#np.save('../../OUTPUT/X_trimm.npy', X)
#np.save('../../OUTPUT/y_trimm.npy', y)