import numpy as np
import matplotlib.pyplot as plt

from meb.gurobi_solvers import mebwo_exact
from data.loading import from_csv
from meb.geometry import M_estimate

data = from_csv(r"src\data\datasets\normal\normal_n200_d4.csv")

eta = 0.9
M_UB = M_estimate(data)

num_trials = 50
M_list = [M_UB*k/2 for k in range(1,num_trials+1)]

variances = {M: None for M in M_list}

for M in M_list:
    _, _, xi, _ = mebwo_exact(data=data, eta=eta, M=M, relax=True)
    variances[M] = np.var(xi)

plt.plot(variances.keys(), variances.values(), marker="o", linestyle=":", mec="r", mfc="r")

plt.xlabel("M")
plt.ylabel("Variance")
plt.show()