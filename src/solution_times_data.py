import numpy as np

from data.loading import to_csv
from data.generation import normal

n_list = [100, 200, 300, 400]
d_list = [3, 7, 11, 15]

for n in n_list:
    for d in d_list:
        data = normal(mean=0, variance=1, n=n, dimension=d)
        filename = r"src\datasets\normal\normal_n{}_d{}.csv".format(n,d)
        to_csv(data=data, filename=filename)