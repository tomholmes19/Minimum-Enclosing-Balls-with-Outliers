import data.loading, data.generation
from meb.ball import Ball, MEB, MEBwO
import numpy as np

import timeit
eta = 0.9

test_data = data.generation.uniform_ball_with_ouliters(2000,2,eta,[0,0],1,3,1)
test_data = data.loading.subset_data(test_data, range(100), [0,1])

start = timeit.default_timer()
ball = MEBwO().fit(data=test_data, method="shenmaier", eta=eta, calc_pct=True)
elapsed = timeit.default_timer() - start

print("Total time:\t", elapsed)
print(ball)
ball.plot(data=test_data)