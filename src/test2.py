import data.loading, data.generation
from meb.ball import Ball, MEB
import numpy as np

import timeit

test_data = data.generation.normal(0,1,1000,5)

ball_1 = MEB().fit(test_data, eps=1e-2, method="heuristic_1")
ball_2 = MEB().fit(test_data, eps=1e-2, method="heuristic_2")

print(len(ball_1.core_set), len(ball_2.core_set))