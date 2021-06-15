import numpy as np

from . import gurobi_solvers, geometry

"""
Algorithms used to compute MEBwO

All functions should start with 'alg_' to be captured in algorithms dictionary (see bottom of algorithms.py)
"""

def alg_exact(data, eta, M=None, LP_relax=False):
    if M is None:
        _, _, diam = geometry.diameter_approx(data[0], data, return_diameter=True)
        M_ = 1.732*diam
    else:
        M_ = M

    c, r, xi  = gurobi_solvers.mebwo_exact(data, eta, M_, LP_relax)
    return c, r, xi

# dictionary of functions whose name starts with "alg_" (i.e. the ones in this file)
algorithms = {name: func for name, func in locals().copy().items() if name.startswith("alg_")}