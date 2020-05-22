import numpy as np
import seaborn as sns
import pandas as pd
from sklearn.metrics import confusion_matrix
from model_builder import build_model
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
#from tensorflow.keras.preprocessing.image import ImageDataGenerator


##PREPARE THE DATA AND THE MODEL:
#Load preprocess data:
X = np.load('X_trim.npy')
y = np.load('y_trim.npy')

#Split data for train and test data:
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Number of classes to discriminate:
num_classes = 5 
# Input image dimensions:
img_rows, img_cols = 28, 28 

#Reshape the data for Tensorflow specifics:
X_train = X_train.reshape(X_train.shape[0], img_rows, img_cols, 1)
X_test = X_test.reshape(X_test.shape[0], img_rows, img_cols, 1)
input_shape = (img_rows, img_cols, 1)

#Rescale the pixel values so they go from 0 to 1:
X_train = X_train.astype('float32') / 255
X_test = X_test.astype('float32') / 255

print('X_train shape:', X_train.shape)
print(X_train.shape[0], 'train samples')
print(X_test.shape[0], 'test samples')

#Convert class vectors to binary class matrices:
y_train = to_categorical(y_train, num_classes)
y_test = to_categorical(y_test, num_classes)

##Import the model from the model_builder:
model = build_model(num_classes, input_shape)

# checkpoint
filepath="../models/weights-improvement-{epoch:02d}-{val_accuracy:.2f}.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='val_accuracy', verbose=1, save_best_only=True, mode='max')
callbacks_list = [checkpoint]

##MODELLING:
batch_size = 128 
epochs = 15 

batch_size = 200 # Train in batches of 128 images
epochs = 15 # Iterate over all data 4 times

history = model.fit(X_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_data=(X_test, y_test),
          callbacks=callbacks_list)

#Saving full model
model.save("../models/model_sketch_extended_v5.h5")
print('model saved')

#Loading checkpoint weights and saving the checkpoint model
model.load_weights('../models/weights-improvement-05-0.97.hdf5')
model.save('model_weighted.h5')

""" With data augmentation:
aug = ImageDataGenerator(rotation_range=20, zoom_range=0.15,
	width_shift_range=0.2, height_shift_range=0.2, shear_range=0.15,
	horizontal_flip=True, fill_mode="nearest")

history = model.fit(aug.flow(X_train, y_train, batch_size=batch_size),
	validation_data=(X_test, y_test), steps_per_epoch=len(X_train) // batch_size,
	epochs=epochs)
model.save("model_sketch_extended_augmented.h5")
print('model saved')
"""

##MODEL EVALUATION AND PLOTTING:
# Evaluate the model with test data
score = model.evaluate(X_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

# Plot training & validation accuracy values
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.savefig('../../OUTPUT/model_accuracy.png')
plt.close()

# Plot training & validation loss values
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.savefig('../../OUTPUT/model_loss.png')
plt.close()

#Plot confussion matrix
class_names=['eyeglasses', 'eyes', 'hat', 'mouth', 'nose']
## Use argmax to project output probabilites as class index label
proba = model.predict(X_test)
print(proba[0])
y_pred = np.argmax(proba, axis=1)
print(y_pred[0])
y_t = np.argmax(y_test, axis=1)
cm = pd.DataFrame(confusion_matrix(y_t, y_pred), index=class_names, columns=class_names) 
fig, ax = plt.subplots(figsize = (20,15))
sns.heatmap(cm, annot=True)
plt.xlabel("True value")
plt.ylabel("Predicted value")
plt.title(f"Test data = {len(y_pred)} samples")
plt.savefig('../../OUTPUT/cm.png')
plt.close()