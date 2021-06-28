import numpy as np
import tensorflow_datasets as tfds

from data.loading import to_csv

ds = tfds.load("mnist", split="train", as_supervised=True)

data = []

for image, label in tfds.as_numpy(ds):
    im = np.array([image[i].flatten() for i in range(28)]).flatten()
    im = np.insert(im, 0, label)
    data.append(im)

data = np.array(data)

to_csv(data, filename="src\data\datasets\mnist\mnist_train.csv")