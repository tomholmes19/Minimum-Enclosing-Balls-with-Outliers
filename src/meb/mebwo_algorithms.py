import numpy as np

from . import gurobi_solvers, geometry, meb_algorithms

"""
Algorithms used to compute MEBwO

All functions should start with 'alg_' to be captured in algorithms dictionary (see bottom of algorithms.py)
"""

sq_3 = np.sqrt(3)
def M_approx(data):
    _, _, diam = geometry.diameter_approx(data[0], data=data, return_diameter=True)
    M = sq_3*diam
    return M

def alg_exact(data, eta, M=None, LP_relax=False):
    if M is None:
        M_ = M_approx(data)
    else:
        M_ = M

    c, r, xi  = gurobi_solvers.mebwo_exact(data, eta, M_, LP_relax)
    return c, r, xi

def alg_heuristic(data, eta, eps=1e-4, M=None):
    if M is None:
        M_ = M_approx(data)
    else:
        M_ = M

    n = len(data)
    k = int(eta*n)

    _, _, xi = gurobi_solvers.mebwo_exact(data=data, eta=eta, M=M_, LP_relax=True)
    
    indices = np.argsort(xi) # the indices of the sorted list
    indices_dash = indices[:k]

    data_dash = [data[i] for i in range(n) if i in indices_dash]

    c, r, _ = meb_algorithms.alg_socp_heuristic(data=data_dash, eps=eps)
    return c, r, None

def alg_heuristic_2(data, eta, eps):
    """
    Fits a MEB to the data, then deletes the core set, repeats until have MEB containing eta*n many points
    """
    n = len(data)
    k = int(eta*n)

    num_contained = n
    A = data
    X = []

    while num_contained > k:
        A = [a for a in A if a not in X]
        num_contained -= len(X)
        c, r, X = meb_algorithms.alg_socp_heuristic(A, eps)
        
        
    return c, r, None
# dictionary of functions whose name starts with "alg_" (i.e. the ones in this file)
algorithms = {name: func for name, func in locals().copy().items() if name.startswith("alg_")}