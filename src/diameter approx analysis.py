import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import data.generation
import meb.geometry

n = 1000
d = 10

np.random.seed(1234)
data = data.generation.normal(0,1,n,d)

D_list = [None]*n
for i in range(n):
    if i % 10 == 0:
        print(i)
    _, _, D = meb.geometry.diameter_approx(data[i], data, return_diameter=True)
    D_list[i] = D

print(np.mean(D_list))
print(np.var(D_list))

sns.set_theme()
sns.displot(x=D_list, kind="kde")
plt.xlabel("M")
plt.savefig(r"images/pw M density.png")
plt.show()