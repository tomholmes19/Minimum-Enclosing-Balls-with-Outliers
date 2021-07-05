import data.loading, data.generation
from meb.ball import Ball, MEB, MEBwO
import numpy as np

import timeit
eta = 0.9

normal = data.loading.from_csv(r"src\data\datasets\normal.csv")
test_data = data.loading.subset_data(normal, rows=range(500), columns=range(4))

start = timeit.default_timer()
ball = MEBwO().fit(data=test_data, method="exact", eta=eta, calc_pct=True)
elapsed = timeit.default_timer() - start

print("Total time:\t", elapsed)
print(ball)
ball.plot(data=test_data)