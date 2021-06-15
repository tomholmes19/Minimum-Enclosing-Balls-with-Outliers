import data.loading, data.generation
from meb.ball import Ball, MEB, MEBwO
import numpy as np

import timeit

test_data = data.loading.from_csv(r"src\test\normal_test.csv")
start = timeit.default_timer()
ball = MEBwO().fit(data=test_data, method="exact", eta=0.9)
elapsed = timeit.default_timer() - start
print("Total time:\t", elapsed)

ball.plot(data=test_data)