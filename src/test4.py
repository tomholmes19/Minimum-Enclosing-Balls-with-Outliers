import numpy as np

from meb import geometry, gurobi_solvers

from meb.ball import MEBwO
from data import generation

np.random.seed(1234)
d = 1000
data = generation.uniform_ball_with_ouliters(
    n=10000,
    d=10,
    eta=0.9,
    r=1,
    r1=2,
    r2=3
)

inliers = [x for x in data if np.linalg.norm(x) <= 11]
c = geometry.find_furthest([0]*d, data=inliers, find_closest=True)
r = max([np.linalg.norm(c-x) for x in inliers])
a = geometry.find_furthest(c, inliers)

MEBwO(c, r).plot(data, show=False)

x, new_r = gurobi_solvers.dc_meb(c, a, inliers)

new_c = c + x*(a-c)

new_ball = MEBwO(new_c, new_r)

print(r, new_r)
print(new_ball.check_subset(inliers))

new_ball.plot(data=data)