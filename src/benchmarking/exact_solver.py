import gurobipy as gp
from gurobipy import GRB

import numpy as np

def mebwo_exact(data, eta, M, relax=False):
    """
    Copy of solver in gurobi_solvers.py but only returns the runtime
    """
    n = len(data) # number of points
    d = len(data[0]) # dimension TODO: make this better
    k = np.ceil(n*(1-eta)) # number of points that are outliers

    m = gp.Model("MEBwO")

    c = m.addMVar(shape=d, lb=-GRB.INFINITY, name="center")
    r = m.addVar(name="radius")

    if relax:
        xi = m.addVars(n, lb=0, ub=1, vtype=GRB.CONTINUOUS)
    else:
        xi = m.addVars(n, vtype=GRB.BINARY)

    m.setObjective(r, GRB.MINIMIZE)

    for i in range(n):
        m.addMQConstr(
            Q=np.identity(d),
            c=-1*np.concatenate((2*data[i], [M,1])),
            sense=GRB.LESS_EQUAL,
            rhs=-1*(data[i]@data[i]),
            xQ_L=c,
            xQ_R=c,
            xc=c.tolist() + [xi[i], r]
        )
    
    m.addConstr(gp.quicksum(xi[i] for i in range(n)) <= k)

    m.optimize()

    return m.Runtime