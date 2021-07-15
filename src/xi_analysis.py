import numpy as np
import matplotlib.pyplot as plt

from meb.gurobi_solvers import mebwo
from data.loading import from_csv, subset_data
from meb.geometry import M_estimate

data = from_csv(r"datasets/normal.csv")
data = subset_data(data, rows=range(300), columns=range(10))

eta = 0.9
M_UB = M_estimate(data)

num_trials = 50
M_list = [M_UB*k/2 for k in range(1,num_trials+1)]

variances = {M: None for M in M_list}

for M in M_list:
    _, _, xi, _ = mebwo(data=data, eta=eta, M=M, relax=True)
    variances[M] = np.var(xi)

plt.plot(variances.keys(), variances.values(), marker="o", linestyle=":", mec="r", mfc="r")

plt.xlabel("M")
plt.ylabel("Variance")
plt.show()