import numpy as np

from meb import geometry

from meb.ball import MEBwO
from data import generation

np.random.seed(1234)
data = generation.normal(0,10,1000,100)

ball = MEBwO().fit(data=data, method="shenmaier", eta=0.9)
print("Finished Shenmaier")
ball.plot(data=data, show=False)
c = ball.center
r = ball.radius
gamma = r**2

inliers = [x for x in data if ball.contains(x)]
a = geometry.find_furthest(c, inliers)

x = min([geometry.Q(c, a, point, gamma) for point in inliers])

new_c = c - (c-a)*x/2
new_r = max([np.linalg.norm(new_c - point) for point in inliers])

new_ball = MEBwO(new_c, new_r)

print(r, new_r)

new_ball.plot(data=data)