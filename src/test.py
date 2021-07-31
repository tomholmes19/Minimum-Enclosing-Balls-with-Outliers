import meb.gurobi_solvers
import data.generation

from meb.ball import MEBwO

import numpy as np

n = 1000
d = 2

np.random.seed(1234)
data = data.generation.normal(0,1,n,d)

ball = MEBwO(center=[0]*d, radius=1)
ball.improve(data, method="dcmeb", )
ball.plot(data)