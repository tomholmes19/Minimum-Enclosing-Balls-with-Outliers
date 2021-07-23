import numpy as np
import timeit

import data.generation, data.loading
from meb import geometry, meb_algorithms
from meb.ball import Ball, MEBwO

n = 10000
d = 30

data_ = data.generation.uniform_ball_with_ouliters(n, d, 0.5, 1, 2, 3)

ball = MEBwO(center=[0]*d, radius=1.5)
ball.calc_pct(data_)
print(data_.shape)
print(ball.pct_containment)
ball.plot(data_, alpha=0.25)