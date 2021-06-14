import numpy as np
import matplotlib.pyplot as plt
import gurobipy as gp
from gurobipy import GRB

d = 2 # dimension
n = 1000 # number of data points
eta = 0.9
k = n*(1-eta)
M = 10

def gen_data(n,d):
    data = [0]*n
    for i in range(n):
        data[i] = np.array([np.random.normal(0,1) for _ in range(d)])
    return data

data = gen_data(n,d)



m = gp.Model("MEB")

# m.Params.NonConvex = 2

c = m.addVars(d, lb=-GRB.INFINITY, name="center")
xi = m.addVars(n, vtype=GRB.BINARY)
r = m.addVar(name="radius")

y = m.addVars(d)

m.setObjective(r, GRB.MINIMIZE)

for i in range(n):
    m.addConstr(
        sum([c[j]*c[j] - 2*c[j]*data[i][j] + (data[i][j]**2) for j in range(d)]) - r - M*xi[i] <= 0
    )

m.addConstr(sum(xi[i] for i in range(n)) <= k)

m.optimize()

center = [c[i].x for i in range(d)]
radius = np.sqrt(m.getVarByName(name="radius").x)

print("center:\t", center)
print("radius:\t", radius)
print("xi:\t", [xi[i].x for i in range(n)])

if d == 2:
    fig,ax = plt.subplots(figsize=(8,8))
            
    x = [data[i][0] for i in range(n)]
    y = [data[i][1] for i in range(n)]

    plt.scatter(x, y, color="blue", label="data")    

    plt.scatter(center[0], center[1], color="red", marker="x", label="center")
    ax.add_patch(
        plt.Circle(center, radius, color="red", fill=False, label="ball")
    )

    plt.legend()

    plt.show()