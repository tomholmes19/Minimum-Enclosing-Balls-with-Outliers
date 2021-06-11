import timeit
import numpy as np

M = 10
size = 1000000000

full_start = timeit.default_timer()
a = np.full(size,M)
full_elapsed = timeit.default_timer() - full_start

zeros_start = timeit.default_timer()
b = np.zeros(size)
b = M*b
zeros_elapsed = timeit.default_timer() - zeros_start

print(full_elapsed, zeros_elapsed)