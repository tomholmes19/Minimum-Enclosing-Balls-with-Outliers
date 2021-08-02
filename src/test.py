import data.generation
import plot_settings
from meb.ball import MEBwO

import numpy as np
import matplotlib.pyplot as plt

n = 1000
d = 100

np.random.seed(3412)
data = data.generation.normal(0,1,n,d)

c = np.array([0]*d)

ball = MEBwO().fit(data, method="shenmaier", eta=0.9)
inliers = [x for x in data if np.linalg.norm(x-c) <= ball.radius]
r = [ball.radius]

for _ in range(100):
    ball.improve(inliers, method="dcmeb")
    r.append(ball.radius)

print(r)
print(ball.check_subset(inliers))

plt.plot(range(101), r)
plt.show()