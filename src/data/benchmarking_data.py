import numpy as np

from loading import to_csv
import generation

n = 100000
d = 1000

np.random.seed(seed=10)

normal_data = generation.normal(mean=0, variance=1, n=n, dimension=d)
to_csv(data=normal_data, filename=r"src\data\datasets\normal.csv")