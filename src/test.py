import numpy as np
import timeit

import data.generation, data.loading
from meb import geometry, meb_algorithms
from meb.ball import Ball, MEBwO
import timeit

n = 10000
d = 30

data_ = data.generation.normal(0, 1, n, d)

start = timeit.default_timer()
M = geometry.M_estimate(data_)
elapsed = timeit.default_timer() - start

print(elapsed)