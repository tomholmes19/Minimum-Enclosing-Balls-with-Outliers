import data.loading, data.generation
from meb.ball import Ball, MEB
import numpy as np

import timeit

test_data = data.generation.normal(0,1,100,2)
start = timeit.default_timer()
ball = MEB().fit(data=test_data, method="heuristic_1", eps=1e-3)
elapsed = timeit.default_timer() - start
print("Total time:\t", elapsed)