import numpy as np
import matplotlib.pyplot as plt

from meb.ball import MEBwO
import data.generation

np.random.seed(1234)
n = 1000
d = 2
data = data.generation.normal(0, 1, n, d)

ball = MEBwO().fit(data, method="shenmaier", eta=0.9)
inliers = [x for x in data if np.linalg.norm(x-ball.center) <= ball.radius]
centers = [ball.center]

for _ in range(10):
    ball.improve(inliers, method="dcmeb")
    centers.append(ball.center)

centers = np.array(centers)
print(centers)
print(centers[:,0])
plt.plot(centers[:,0], centers[:,1])
plt.show()