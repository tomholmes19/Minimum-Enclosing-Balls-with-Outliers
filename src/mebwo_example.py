import numpy as np
import matplotlib.pyplot as plt

from meb.ball import MEBwO
import data.generation
from meb.geometry import M_estimate
import plot_settings

n = 1000
d = 2

np.random.seed(2000)
data = data.generation.normal(0,1,n,d)
M = M_estimate(data)
ball = MEBwO().fit(data=data, method="exact", eta=0.9, M=M, outputflag=1)

ball.plot(data, show=False)
plt.legend()
plt.savefig(r"images/sample_mebwo.png", bbox_inches="tight")
plt.show()