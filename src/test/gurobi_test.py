import numpy as np
import matplotlib.pyplot as plt
import gurobipy as gp
from gurobipy import GRB

d = 2 # dimension
n = 10 # number of data points
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

#m.Params.NonConvex = 2

c = m.addMVar(shape=d, lb=-GRB.INFINITY, name="center")
xi = m.addMVar(shape=n, vtype=GRB.BINARY)
r = m.addVar(name="radius")

m.setObjective(r, GRB.MINIMIZE)

Q = np.identity(d)
print(Q)
for i in range(n):
    m.addMQConstr(
        Q=Q,
        c=np.concatenate((-2*data[i], -1*(M**2)*np.ones(n), -1), axis=None),
        sense=GRB.LESS_EQUAL,
        rhs= -1*(data[i]@data[i]),
        xQ_L=c.tolist(),
        xQ_R=c.tolist(),
        xc=c.tolist() + xi.tolist() + [r]
    )

m.addConstr(sum(xi[i] for i in range(n)) <= k)

m.optimize()

center = [v.x for v in c.tolist()]
radius = np.sqrt(m.getVarByName(name="radius").x)

print("center:\t", center)
print("radius:\t", radius)
print("xi:\t", [v.x for v in xi.tolist()])

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