import cv2
from matplotlib import pyplot as plt
import glob
import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import zipfile as zf
import matplotlib.image as mpimg




Test_tomato = ( './tomato/val/Tomato___Bacterial_spot/*.jgp')
A = len(Test_tomato)
print("Training sample: {}".format(A))
train_datagen = ImageDataGenerator(rescale = 1.0 / 255.0,
                                   zoom_range = 0.4,
                                   rotation_range = 10,
                                   horizontal_flip = True,
                                   vertical_flip = True,
                                   validation_split = 0.2)
train_dataset = train_datagen.flow_from_directory(directory =
                                                  './tomato/train/',
                                                  target_size = (224,224),
                                                   class_mode = 'binary',
                                                   batch_size = 128,
                                                   subset = 'training')
print(train_dataset.class_indices)



img = mpimg.imread('./tomato/val/Tomato___Bacterial_spot/0ab9c705-f29e-45ac-b786-9549b3c38f16___GCREC_Bact.Sp 3223.jpg')
print(img)
# This will show into a graph image plot
imgplot = plt.imshow(img)
# this allow to show the image
plt.show()
