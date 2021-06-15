import data.loading, data.generation
from meb.ball import Ball, MEB, MEBwO
import numpy as np

import timeit

test_data = data.generation.normal(0,1,1000,10)
start = timeit.default_timer()
ball = MEBwO().fit(data=test_data, method="exact", eta=0.9)
elapsed = timeit.default_timer() - start
print("Total time:\t", elapsed)
print("Contains:\t{}%".format(ball.pct_containment(test_data)*100))
ball.plot(data=test_data)