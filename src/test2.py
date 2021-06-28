import data.loading, data.generation
from meb.ball import Ball, MEB, MEBwO
import numpy as np

import timeit
eta = 0.9

test_data = data.generation.normal(0,1,10000,2)

start = timeit.default_timer()
ball = MEBwO().fit(data=test_data, method="heuristic", eta=eta, eps=1e-4, calc_pct=True)
elapsed = timeit.default_timer() - start

print("Total time:\t", elapsed)
print(ball)
ball.plot(data=test_data)