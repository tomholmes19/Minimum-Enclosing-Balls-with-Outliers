import numpy as np

from . import gurobi_solvers, geometry, meb_algorithms

"""
Algorithms used to compute MEBwO

All functions should start with 'alg__' to be captured in algorithms dictionary (see bottom of algorithms.py)
"""

sq_3 = np.sqrt(3)
def M_approx(data):
    _, _, diam = geometry.diameter_approx(data[0], data=data, return_diameter=True)
    M = sq_3*diam
    return M

def alg__exact(data, eta, M, relax=False, time_limit=None, log_file=""):
    c, r, xi, _  = gurobi_solvers.mebwo(data, eta, M, relax, time_limit, log_file)
    return c, r, xi

def alg__relaxation_heuristic(data, eta, M, eps=1e-4):

    n = len(data)
    k = int(eta*n)

    _, _, xi, _ = gurobi_solvers.mebwo(data=data, eta=eta, M=M, relax=True)
    
    indices = np.argsort(xi) # the indices of the sorted list
    indices_dash = indices[:k]

    data_dash = [data[i] for i in range(n) if i in indices_dash]

    c, r, _ = meb_algorithms.alg__socp_heuristic(data=data_dash, eps=eps)
    return c, r, None

def alg__heuristic_2(data, eta, eps):
    """
    Fits a MEB to the data, then deletes the core set, repeats until have MEB containing eta*n many points
    """
    n = len(data)
    k = int(np.floor(eta*n))

    num_contained = n
    A = data
    X = []

    while num_contained > k:
        A = [a for a in A if a not in X]
        num_contained -= len(X)
        c, r, X = meb_algorithms.alg__socp_heuristic(A, eps)
        
        
    return c, r, None

def alg__peeling(data, eta, eps=1e-4, **kwargs):
    """
    Fits a MEB to the data, then finds the k closest points such that eta% of the data is contained
    """
    c, _, _ = meb_algorithms.alg__socp_heuristic(data, eps)

    n = len(data)
    k = int(np.floor(eta*n))
    _, r = geometry.k_closest(data, c, k)

    return c, r, None

def alg__shenmaier(data, eta, **kwargs):
    """
    Algorithm 1 of Shenmaier 2015 https://link.springer.com/chapter/10.1007/978-88-7642-475-5_92

    For every point in data, find MEB of closest k=eta*n points to this point,
    return MEB with smallest radius
    """
    n = len(data)
    k = int(np.floor(eta*n))
    radii = [None]*n

    for i in range(n):
        _, radii[i] = geometry.k_closest(data, data[i], k)
    
    min_r_index = np.argmin(radii)
    
    return data[min_r_index], radii[min_r_index], None

def alg__maximin(data, eta, eps):
    """
    
    """
    num_outliers = int(np.ceil((1-eta)*len(data)))

    c_dash, _, _ = meb_algorithms.alg__socp_heuristic(data, eps)

    outliers = [geometry.find_furthest(c_dash, data)]
    inliers = [x for x in data if not np.array_equal(x, outliers[0])]

    for _ in range(num_outliers-1):
        distances = []
        for x in inliers:
            distances.append(
                min([np.linalg.norm(x-y) for y in outliers])
            )
        
        max_dist_index = np.argmax(distances)
        new_outlier = inliers[max_dist_index]
        outliers.append(new_outlier)
        inliers = [x for x in inliers if not np.array_equal(x, new_outlier)]
    
    c, r, _ = meb_algorithms.alg__socp_heuristic(inliers, eps)

    print(inliers)
    print("\n")
    print(outliers)
    return c, r, None

# dictionary of functions whose name starts with "alg__" (i.e. the ones in this file)
algorithms = {name: func for name, func in locals().copy().items() if name.startswith("alg__")}