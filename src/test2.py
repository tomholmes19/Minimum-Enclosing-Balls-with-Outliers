import data.loading, data.generation
from meb.ball import Ball, MEB
import numpy as np

import timeit

test_data = data.generation.normal(0,1,1000,50)


start_time = timeit.default_timer()
ball = MEB().fit(test_data, eps=1e-4, method="socp_heuristic")
print(ball.check_subset(test_data))
elapsed = timeit.default_timer() - start_time
print("Elapsed: {}".format(elapsed))

#print(ball)
ball.plot(test_data)