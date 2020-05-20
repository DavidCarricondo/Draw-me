import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D

num_classes = 5 #glasses, eyes, hat, mouth, nose
img_rows, img_cols = 28, 28 # Input image dimensions
input_shape = (img_rows, img_cols, 1)


def build_model(num_classes, input_shape):
    model = Sequential()
    #Convolution
    model.add(Conv2D(32, kernel_size=(2, 2),
                    activation='relu',
                    input_shape=input_shape))
    #Convolution and reduction
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    #Convolution and reduction
    model.add(Conv2D(128, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    #Regularization and flattening
    model.add(Dropout(0.35))
    model.add(Flatten())
    #Fully conected layers
    model.add(Dense(128, activation='relu'))
    model.add(Dense(50, activation='relu'))
    model.add(Dense(num_classes, activation='softmax'))

    loss_function = keras.losses.categorical_crossentropy
    optimizer = keras.optimizers.Adam()

    model.compile(loss=loss_function, optimizer=optimizer, metrics=['accuracy'])

    return model

#Test loss: 0.116
#Test accuracy: 0.967
