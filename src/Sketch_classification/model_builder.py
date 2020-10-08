import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D

num_classes = 5 #glasses, eyes, hat, mouth, nose
img_rows, img_cols = 28, 28 # Input image dimensions
input_shape = (img_rows, img_cols, 1)


def build_model(num_classes, input_shape):
    model = Sequential()
    model.add(Conv2D(64, kernel_size=(7, 7),activation='relu', padding='same', input_shape=input_shape))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
    model.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(256, (3, 3), activation='relu', padding='same'))
    model.add(Conv2D(256, (3, 3), activation='relu', padding='same'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(num_classes, activation='softmax'))

    loss_function = keras.losses.categorical_crossentropy
    optimizer = keras.optimizers.Adam()

    model.compile(loss=loss_function, optimizer=optimizer, metrics=['accuracy'])

    return model

#Test loss: 0.116
#Test accuracy: 0.967
