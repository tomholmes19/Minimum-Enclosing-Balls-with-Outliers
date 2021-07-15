import numpy as np

from meb import geometry

from meb.ball import MEBwO
from data import generation

np.random.seed(1234)
d = 1000
data = generation.uniform_ball_with_ouliters(
    n=10000,
    d=d,
    eta=0.9,
    r1=10,
    r2=20,
    sep=5
)

inliers = [x for x in data if np.linalg.norm(x) <= 11]
c = geometry.find_furthest([0]*d, data=inliers, find_closest=True)
r = max([np.linalg.norm(c-x) for x in inliers])
gamma = r**2
a = geometry.find_furthest(c, inliers)

MEBwO(c, r).plot(data, show=False)

x = min([geometry.Q(c, a, point, gamma) for point in inliers])

new_c = c - (c-a)*x/2
new_r = max([np.linalg.norm(new_c - point) for point in inliers])

new_ball = MEBwO(new_c, new_r)

print(r, new_r)
print(new_ball.check_subset(inliers))

new_ball.plot(data=data)