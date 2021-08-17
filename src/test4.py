import pandas as pd

from meb.gurobi_solvers import mebwo

df = pd.read_csv(r"datasets/mnist_train.csv", header=None)

zeros = df[df[0] == 0]
data = zeros.to_numpy()
print("Starting")
c, r, xi = mebwo(data, 0.9, M=5000, relax=True, outputflag=1)