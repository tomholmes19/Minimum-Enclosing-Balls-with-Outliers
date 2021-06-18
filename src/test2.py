import data.loading, data.generation
from meb.ball import Ball, MEB, MEBwO
import numpy as np

import timeit

test_data = data.generation.uniform_ball_with_ouliters(n=10000, d=2, eta=0.9, c=np.array([0,0]), r1=1, r2=5)
start = timeit.default_timer()
#ball = MEBwO().fit(data=test_data, method="exact", eta=0.9)
ball = Ball(center=np.array([0,0]), radius=1)
elapsed = timeit.default_timer() - start
print("Total time:\t", elapsed)
#print("Contains:\t{}%".format(ball.pct_containment(test_data)*100))
ball.plot(data=test_data)