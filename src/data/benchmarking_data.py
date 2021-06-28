from loading import to_csv
from generation import normal

n_list = [100 + 50*i for i in range(10)]
d_list = [2 + 2*i for i in range(10)]

for n in n_list:
    for d in d_list:
        data = normal(mean=0, variance=1, n=n, dimension=d)
        filename = r"src\data\datasets\normal\normal_n{}_d{}.csv".format(n,d)
        to_csv(data=data, filename=filename)
