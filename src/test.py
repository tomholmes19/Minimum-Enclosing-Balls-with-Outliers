import numpy as np

import data.generation
from meb.ball import MEBwO



n = 10000
d = 2
r = 1
c = None

data =  data.generation.uniform_ball_with_ouliters(n=n, d=d, eta=0.9, r=1 ,r1=2, r2=3)

ball = MEBwO(center=[0]*d, radius=0)

ball.plot(data, alpha=0.5)
