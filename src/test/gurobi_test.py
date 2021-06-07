import numpy as np

import gurobipy as gp
from gurobipy import GRB

d = 4 # dimension
n = 1000 # number of data points

def gen_data(n,d):
    data = [0]*n
    for i in range(n):
        data[i] = np.array([np.random.normal(0,1) for _ in range(d)])
    return data

data = gen_data(n,d)

m = gp.Model("MEB")

r = m.addVar(name="radius")
c = m.addMVar(shape=d, lb=-GRB.INFINITY, name="center")

m.setObjective(r, GRB.MINIMIZE)

#TODO: figure out norm constraint
m.addConstrs(
    (sum((c[j] - data[i][j]) for j in range(d)) + r <= 0 for i in range(n))
)


m.optimize()

for v in m.getVars():
    print(v.varName, v.x)