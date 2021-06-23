import numpy as np

import gurobipy as gp
from gurobipy import GRB

def meb_exact(data):
    """
    Solves the MEB problem using Gurobi

    Input:
        data (array like): list of data points to compute the MEB for

    Return:
        c_soln (NumPy array): center of the MEB
        r_soln (float): radius of the MEB
    """
    n = len(data) # number of points
    d = len(data[0]) # dimension TODO: make this better

    m = gp.Model("MEB")

    c = m.addMVar(shape=d, lb=-GRB.INFINITY, name="center")
    r = m.addVar(name="radius")

    m.setObjective(r, GRB.MINIMIZE)

    #TODO: find a way to vectorise this
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
    
    m.optimize()

    c_soln = [v.x for v in c.tolist()]
    r_soln = np.sqrt(m.getVarByName(name="radius").x)

    return c_soln, r_soln, None

def mebwo_exact(data, eta, M, LP_relax=False):
    """
    Solves the MEBwO problem for eta% of the points covered using Gurobi

    Input:
        data (array like): list of data points to compute the MEB for
        eta (float): percentage of points to be covered, i.e. eta=0.9 means 90% of points in data are inside the ball
        M (float): value of M for big M constraint
        LP_relax (bool): if True then relax binary variables to 0 <= xi[i] <= 1 for all i

    Return:
        c_soln (NumPy array): center of the MEB
        r_soln (float): radius of the MEB
        xi_soln (int): binary variables for outlier or not outlier
    """
    n = len(data) # number of points
    d = len(data[0]) # dimension TODO: make this better
    k = np.ceil(n*(1-eta)) # number of points that are outliers

    m = gp.Model("MEBwO")

    c = m.addMVar(shape=d, lb=-GRB.INFINITY, name="center")
    r = m.addVar(name="radius")

    if LP_relax:
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

    c_soln = [c[i].x for i in range(d)]
    r_soln = np.sqrt(r.x)
    xi_soln = [xi[i].x for i in range(n)]

    return c_soln, r_soln, xi_soln