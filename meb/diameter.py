import numpy as np

def find_furthest(p,data):
    """
    Finds the furthest point in data from p (l2 norm)

    Input:
        p (array like): initial point
        data (array like): list of points to find furthest point from p

    Return:
        furthest_point (array like): point in data which is furthest from p
    """
    furthest_dist = 0
    furthest_point = p
    for x in data:
        dist = np.linalg.norm(p-x)
        if dist > furthest_dist:
            furthest_dist = dist
            furthest_point = x
        
    return furthest_point

def diameter_approx(p, data, return_diameter=False):
    """
    Given an initial point p in data, finds q which is furthest from p and qdash which
    is furthest from q and if desired calculates diameter
    
    Input:
        p (array like): initial point
        data (array like): list of points to approximate diameter for
        return_diameter (bool): if True, also return distance (l2 norm) between q and qdash

    Return:
        out (tuple): tuple containing q, qdash, and if desired diameter
    """
    q = find_furthest(p, data)
    qdash = find_furthest(q, data)

    out = (q, qdash)
    if return_diameter:
        diameter = np.linalg.norm(q-qdash)
        out = out + (diameter,)
    
    return out