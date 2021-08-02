import numpy as np
import matplotlib.pyplot as plt

from meb.ball import MEB
import data.generation

n = 1000
d = 2

np.random.seed(1000)
data = data.generation.normal(0, 1, n, d)

ball = MEB().fit(data, method="socp_heuristic", eps=1e-4)
ball.plot(data)