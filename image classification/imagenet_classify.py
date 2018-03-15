# import the necessary packages
from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input, decode_predictions
import numpy as np
import argparse
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the input image")
args = vars(ap.parse_args())
 
# load the original image via OpenCV so we can draw on it and display
# it to our screen later
orig = cv2.imread(args["image"])

# load the input image using the Keras helper utility while ensuring
# that the image is resized to 224x224 pxiels, the required input
# dimensions for the network -- then convert the PIL image to a
# NumPy array
print("[INFO] loading and preprocessing image...")
img = image.load_img(args["image"], target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

# load the VGG16 network
print("[INFO] loading network...")
model = VGG16(weights='imagenet')

# classify the image
print("[INFO] classifying image...")
preds = model.predict(x)
#print('the result is:', decode_predictions(preds, top=3)[0])
p = decode_predictions(preds)
(imagenetID, label, prob) = p[0][0]
# display the predictions to our screen
print("imagenetID: {}, label: {} , Probability: {}".format(imagenetID, label,prob))
cv2.putText(orig, "Label: {}".format(label), (10, 30),
	cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
cv2.imshow("Classification", orig)
cv2.waitKey(0)
