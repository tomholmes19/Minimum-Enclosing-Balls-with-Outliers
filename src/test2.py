import data.loading, data.generation
from meb.ball import Ball, MEB

import timeit

test_data = data.generation.normal(0,1,2,2)


start_time = timeit.default_timer()
ball = MEB(radius=5).fit(test_data, eps=1e-4, method="socp_heuristic")
elapsed = timeit.default_timer() - start_time
#print("Elapsed: {}".format(elapsed))

#print(ball)
ball.plot(test_data)