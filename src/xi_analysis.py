import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plot_settings

import data.generation
from meb.gurobi_solvers import mebwo
from meb.geometry import M_estimate

np.random.seed(1234)
data = data.generation.normal(0,1,300,10)

eta = 0.9
M_UB = M_estimate(data)

num_trials = 50
M_list = [M_UB*k/2 for k in range(1,num_trials+1)]

variances = {M: None for M in M_list}

for M in M_list:
    _, _, xi, _ = mebwo(data=data, eta=eta, M=M, relax=True, outputflag=1)
    variances[M] = np.var(xi)

# plt.plot(variances.keys(), variances.values(), marker="o", linestyle=":", mec="b", mfc="b")
sns.lineplot(x=M_list, y=variances.values())
plt.xlabel("M")
plt.ylabel("Variance")
plt.savefig(r"images/xi_analysis.png")
plt.show()