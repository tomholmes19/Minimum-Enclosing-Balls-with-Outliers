import numpy as np

from data.loading import to_csv
from data.generation import normal

n_list = [100, 500, 1000, 5000, 10000]
d_list = [5, 10, 15, 20, 50, 100]

for n in n_list:
    for d in d_list:
        data = normal(mean=0, variance=1, n=n, dimension=d)
        filename = r"src\datasets\normal\normal_n{}_d{}".format(n,d)
        to_csv(data=data, filename=filename)