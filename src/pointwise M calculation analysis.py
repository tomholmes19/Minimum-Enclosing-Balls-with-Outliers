import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import data.generation
import meb.geometry

n = 1000
d = 10

np.random.seed(1234)
data = data.generation.uniform_ball(n,d,1)

D_list = [None]*n
for i in range(n):
    if i % 10 == 0:
        print(i)
    _, _, D = meb.geometry.diameter_approx(data[i], data, return_diameter=True)
    D_list[i] = D


sns.set_theme()
sns.displot(x=D_list, kind="kde")
plt.show()