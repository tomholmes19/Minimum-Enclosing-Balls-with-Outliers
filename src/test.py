import numpy as np
import timeit

import data.generation, data.loading
from meb import geometry, meb_algorithms
from meb.ball import Ball, MEBwO

n = 5000
d = 2
r = 10

data_ = data.generation.uniform_ball_with_ouliters(n, d, 0.9, 1, 2, 3)

ball = MEBwO(center=[0]*d, radius=1.5)
ball.calc_pct(data_)
print(ball.pct_containment)
ball.plot(data_, alpha=0.25)