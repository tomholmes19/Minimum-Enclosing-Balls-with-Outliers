import data.loading, data.generation
from meb.ball import Ball, MEB, MEBwO
import numpy as np

import timeit

eta = 0.9

test_data = data.generation.uniform_ball_with_ouliters(
    n=100,
    d=2,
    eta=eta,
    c=[5,-10],
    r1=1,
    r2=3,
    sep=1
)

start = timeit.default_timer()
ball = MEBwO().fit(calc_pct=True, data=test_data, method="exact", eta=eta)
elapsed = timeit.default_timer() - start

print("Total time:\t", elapsed)
print(ball)
ball.plot(data=test_data)