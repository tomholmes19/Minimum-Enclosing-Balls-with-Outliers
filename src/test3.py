import timeit

from data.generation import normal
from meb.geometry import M_estimate
from meb.ball import Ball
from meb.mebwo_algorithms import M_approx

data = normal(0, 1, 1000, 2)
print("Calculating M1")
M1_start = timeit.default_timer()
M1 = M_estimate(data)
M1_elapsed = timeit.default_timer() - M1_start

print("Calculating M2")
M2_start = timeit.default_timer()
M2 = M_approx(data)
M2_elapsed = timeit.default_timer() - M2_start

print("M1:\t\t{}".format(M1))
print("Elapsed:\t{}s".format(M1_elapsed))

print("M2:\t\t{}".format(M2))
print("Elapsed:\t{}s".format(M2_elapsed))

Ball(radius=1, center=[0,0]).plot(data)
