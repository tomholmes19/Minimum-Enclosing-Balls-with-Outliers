import numpy as np

import gurobipy as gp
from gurobipy import GRB

def socp_solver(data):
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

    return c_soln, r_soln
    