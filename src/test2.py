import data.loading, data.generation
from meb.ball import Ball

import timeit

print("generating data")
test_data = data.generation.normal(0,1,10000,200)
print("finished data")

start_time = timeit.default_timer()
ball = Ball().fit(test_data, eps=1e-4, method="heuristic")
elapsed = timeit.default_timer() - start_time
print("Elapsed: {}".format(elapsed))

print(len(ball.core_set))