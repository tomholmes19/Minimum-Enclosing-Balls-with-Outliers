import numpy as np

def find_furthest(p,data, return_index=False) -> np.array:
    """
    Finds the furthest point in data from p (l2 norm)

    Input:
        p (array like): initial point
        data (array like): list of points to find furthest point from p
        return_index (bool): if True return the index of the furthest point, if False return the furthest point

    Return:
        furthest_point (array like): point in data which is furthest from p
    """
    # initial values set to return point p if data is empty or only contains p
    furthest_dist = 0
    furthest_point = p
    furthest_index = 0
    n = len(data)
    for i in range(n):
        x = data[i]
        dist = np.linalg.norm(p-x)
        if dist > furthest_dist:
            furthest_dist = dist
            furthest_point = x
            furthest_index = i
    
    if return_index:
        return furthest_index
    else:
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

def mean_vector(data) -> np.array:
    """
    Calculates the mean vector from a set of d-dimensional vectors

    Input:
        data (array like): set of vectors to calculate the mean for

    Return:
        mean (np.array): mean vector
    """
    d = len(data[0])
    
    # calculate mean for each column in data
    # e.g.
    #   a = [
    #       [1,2],
    #       [3,4],
    #       [5,6]    
    #   ]
    #   calculate mean of [1,3,5], [2,4,6], return results as elements of array
    mean = np.array([
        np.mean([x[i] for x in data]) for i in range(d)
    ])
    return mean