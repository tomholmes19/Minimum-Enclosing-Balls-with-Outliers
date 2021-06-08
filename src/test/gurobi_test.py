import numpy as np

import gurobipy as gp
from gurobipy import GRB

d = 2 # dimension
n = 10 # number of data points

def gen_data(n,d):
    data = [0]*n
    for i in range(n):
        data[i] = np.array([np.random.normal(0,1) for _ in range(d)])
    return data

data = gen_data(n,d)

m = gp.Model("MEB")

c = m.addMVar(shape=d, lb=-GRB.INFINITY, name="center")
r = m.addVar(name="radius")

m.setObjective(r, GRB.MINIMIZE)

for i in range(n):
    m.addMQConstr(
        Q=np.identity(d),
        c=np.append(-2*data[i],-1),
        sense=GRB.LESS_EQUAL,
        rhs=-1*(data[i]@data[i]),
        xQ_L=c,
        xQ_R=c,
        xc=c.tolist().append(r)
    )

#m.addConstrs(
#    ( (data[i] @ data[i]) - 2*(data[i] @ c) + (c @ c)  <= r for i in range(n) )
#)

m.optimize()

print([v.x for v in c.tolist()])