#$$$  face comparison using the library dlib $$$#
import dlib
from skimage import io
from scipy.spatial import distance

#Create models for searching and finding persons in dlib¶
sp = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
facerec = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')
detector = dlib.get_frontal_face_detector()
# set the path of the  two images 
image1 = input("the path to the first image is  = ")
image2 = input("the path to the seconed image is  = ")
#uploading first image

img = io.imread(image1)

win1 = dlib.image_window()
win1.set_image(img)
win1.clear_overlay()

# find the face within image
dets = detector(img, 1)
for k, d in enumerate(dets):
    print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
        k, d.left(), d.top(), d.right(), d.bottom()))
    shape = sp(img, d)
    win1.clear_overlay()
    win1.add_overlay(d)
    win1.add_overlay(shape)
# extracting Descriptor  from the face
face_descriptor1 = facerec.compute_face_descriptor(img, shape)

print(face_descriptor1)
# uploading seconed image

img = io.imread(image2)
win2 = dlib.image_window()
win2.clear_overlay()
win2.set_image(img)
dets_webcam = detector(img, 1)
for k, d in enumerate(dets_webcam):
    print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
        k, d.left(), d.top(), d.right(), d.bottom()))
    shape = sp(img, d)
    win2.clear_overlay()
    win2.add_overlay(d)
    win2.add_overlay(shape)

face_descriptor2 = facerec.compute_face_descriptor(img, shape)

# Calculate the Euclidean distance between two dexryptors of individuals
# In dlib, it is recommended to use the boundary value of the Euclidian distance between face
#descriptors # equal to 0.6. If the Euclidean distance is less than 0.6, then the photos belong 
#to one person.
a = distance.euclidean(face_descriptor1, face_descriptor2)
print(a)
print("hit enter to exit")
dlib.hit_enter_to_continue()
