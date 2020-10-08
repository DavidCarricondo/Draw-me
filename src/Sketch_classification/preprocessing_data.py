import prep_data_functions.py as pf
import numpy as np
import random

#Load the data by batches so you do not saturate the RAM:
mouth = np.load('./INPUT/mouth.npy')
nose = np.load('./INPUT/nose.npy')
eyes =  np.load('./INPUT/eye.npy')
#eyeglasses = np.load('./INPUT/eyeglasses.npy')
hat = np.load('./INPUT/hat.npy')

#TRimm the data to balance the samples. One at a time because of performance issues:
rnd_mouth = random.sample(range(len(mouth)), len(eyes))
mouth_clean = mouth[rnd_mouth]
len(mouth_clean)

rnd_nose = random.sample(range(len(nose)), len(eyes))
nose_clean = nose[rnd_nose]

rnd_hat = random.sample(range(len(hat)), len(eyes))
hat_clean = hat[rnd_hat]

#rnd_eyeglasses = random.sample(range(len(eyeglasses)), len(eyes))
#eyeglasses_clean = eyeglasses[rnd_eyeglasses]


sketch_data = {'mouth' : mouth_clean,'nose': nose_clean, 'eyes' : eyes,  'hat': hat_clean} #'eyeglasses': eyeglasses_clean,


X = pf.create_x(sketch_data)
y = y = pf.create_y(sketch_data)


#np.save('../../OUTPUT/X_trimm.npy', X)
#np.save('../../OUTPUT/y_trimm.npy', y)

"""
Visualize layers:

def convolution(im, kernel):
  result = np.zeros(im.shape)
  # Output array
  for ii in range(im.shape[0] - 2):
      for jj in range(im.shape[1] - 2):
          result[ii, jj] = (im[ii:ii+2, jj:jj+2] *kernel).sum()
  return result

conv1 = model.layers[0]

weights1 = conv1.get_weights()
len(weights1)
kernels1 = weights1[0]
kernels1.shape

kernel1_1 = kernels1[:, :, 0, 0]
kernel1_1.shape 

#plt.imshow(kernel1_1)

ima = im[0,:,:,0]
#plt.imshow(ima)

filtered_image = convolution(ima, kernel1_1)
#plt.imshow(filtered_image, cmap='gray')
"""