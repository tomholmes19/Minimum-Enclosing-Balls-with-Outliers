import data.loading, data.generation
from meb.ball import Ball, MEB, MEBwO
import numpy as np

import timeit

eta = 0.9

test_data = data.generation.two_clusters(
    n=100,
    d=2,
    eta=eta,
    m1=0,
    v1=1,
    m2=10,
    v2=1
)

start = timeit.default_timer()
ball = MEBwO().fit(calc_pct=True, data=test_data, method="exact", eta=eta, relax=False)
elapsed = timeit.default_timer() - start

print("Total time:\t", elapsed)
print(ball)
ball.plot(data=test_data)