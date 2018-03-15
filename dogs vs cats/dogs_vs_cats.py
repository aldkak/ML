# Recognition of dogs and cats on images using a convolutional neural network CNN
# Data source - Kaggle Dogs vs. competition. Cats.
# Before using, you must download and prepare data for training, testing

# step 1  import models 
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Conv2D, MaxPooling2D
from tensorflow.python.keras.layers import Activation, Dropout, Flatten, Dense
# step2 
# folder of trained data
train_dir = 'train'
# data for checking 
val_dir = 'val'
# test folder
test_dir = 'test'
# size of the image
img_width, img_height = 150, 150
# The dimension of the tensor on the basis of the image for the input data to the neural network
# backend Tensorflow, channels_last
input_shape = (img_width, img_height, 3)
# Number of epochs
epochs = 30
# Size of the mini-sample
batch_size = 16
# Number of images for training
nb_train_samples = 17500
# Number of images to check
nb_validation_samples = 3750
# Number of images for testing
nb_test_samples = 3750


# Create convolutional neural network
# Network Architecture
# Convolution layer, kernel size 3x3, number of feature cards - 32 pieces, activation function ReLU.
# Sub-sample layer, selection of the maximum value from the 2x2 square
# Convolution layer, kernel size 3x3, number of feature cards - 32 pieces, activation function ReLU.
# Sub-sample layer, selection of the maximum value from the 2x2 square
# Convolution layer, kernel size 3x3, number of feature cards - 64 pcs., Activation function ReLU.
# Sub-sample layer, selection of the maximum value from the 2x2 square
# Conversion layer from two-dimensional to one-dimensional representation
# Fully-knit layer, 64 neurons, activation function ReLU.
# Dropout layer.
# Output layer, 1 neuron, activation function sigmoid
# Layers 1 through 6 are used to highlight important characteristics in the image, and layers 7 to 10 -
# for classification.

#step 3
model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=input_shape))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))
# Compile the neural network

# step4
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
# Create an image generator
# The image generator is created based on the ImageDataGenerator class. The generator divides the values
# all pixels of the image at 255.

#step5
datagen = ImageDataGenerator(rescale=1. / 255)
# Data generator for learning based on images from the folder

#step6
train_generator = datagen.flow_from_directory(
    train_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary')

# Data generator for checking based on images from the folder
#step7
val_generator = datagen.flow_from_directory(
    val_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary')
# Data generator for testing based on images from the folder
#step8
test_generator = datagen.flow_from_directory(
    test_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary')

# Train a model using generators
#train_generator - data generator for learning

#validation_data 

#step9
model.fit_generator(
    train_generator,
    steps_per_epoch=nb_train_samples // batch_size,
    epochs=epochs,
    validation_data=val_generator,
    validation_steps=nb_validation_samples // batch_size)

scores = model.evaluate_generator(test_generator, nb_test_samples // batch_size)

print("Accuracy on the test data: %.2f%%" % (scores[1]*100))
