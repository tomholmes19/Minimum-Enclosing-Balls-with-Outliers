import data.loading, data.generation
from meb.ball import Ball, MEB
import numpy as np

import timeit

test_data = data.generation.normal(0,1,10000,20)

ball = MEB().fit(data=test_data, method="socp_heuristic")

print(ball)