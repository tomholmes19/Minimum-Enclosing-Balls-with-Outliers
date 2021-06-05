import numpy as np
from . import geometry, socp_solver, ball

"""
Algorithms used to compute MEB

All functions should start with 'alg_' to be captured in algorithms dictionary (see bottom of algorithms.py)
"""

def alg_socp_exact(data, eps): # solves the exact optimisation problem for MEB
        c, r = socp_solver.socp_solver(data)
        return c, r, None

def alg_socp_heuristic(data, eps): # algorithm 1 https://dl.acm.org/doi/10.1145/996546.996548
    p = data[0]
    q, qdash = geometry.diameter_approx(p, data)
    X = np.array([q,qdash])
    delta = eps/163

    while True: # might want to set a max number of iterations
        c, r = socp_solver.socp_solver(X) # compute MEB(X)
        r_dash = r*(1+delta) # get radius for (1+delta) approximation to MEB(X)
        temp_ball = ball.Ball(c,r_dash*(1+eps/2)) # set temp ball

        if temp_ball.check_subset(data): # check if all the data is contained in temp ball
            break
        else:
            p = geometry.find_furthest(c, data) # p = argmax_(x\in S) [||c'-x||]
        
        X = np.vstack((X,p)) # X := X U {p}

    return c, r, X

def alg_heuristic_1(data, eps): # algorithm 3.1 https://www.researchgate.net/publication/220133011_Two_Algorithms_for_the_Minimum_Enclosing_Ball_Problem
    #TODO: finish this
    alpha = geometry.find_furthest(data[0], data)
    beta = geometry.find_furthest(data[alpha], data)

    n = len(data)
    u = np.zeros(n)
    u[alpha] = 1/2
    u[beta] = 1/2

    X = np.array([data[alpha], data[beta]])

    return None

# dictionary of functions whose name starts with "alg_" (i.e. the ones in this file)
algorithms = {name: func for name, func in locals().copy().items() if name.startswith("alg_")}
