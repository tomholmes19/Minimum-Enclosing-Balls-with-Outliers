import data.loading, data.generation
from meb.ball import Ball, MEB, MEBwO
import numpy as np

import timeit

eta = 0.55

test_data = data.generation.normal(0,1,100,2)

start = timeit.default_timer()
ball = MEBwO().fit(calc_pct=True, data=test_data, method="exact", eta=eta)
elapsed = timeit.default_timer() - start

print("Total time:\t", elapsed)
print(ball)
ball.plot(data=test_data)