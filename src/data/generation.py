import numpy as np

# Functions to generate data from a specific distribution with given parameters, dimension, and number of points

def normal(mean, variance, n, dimension) -> np.array:
    """
    Generates n data points from Normal(mean, variance) distribution with given dimension
    Input:
        mean (float): mean of normal distribution
        variance (float): variance of normal distribution
        n (int): number of data points to generate
        dimension (int): dimension of the data points

    Return:
        data (np.array): generated data 
    """
    data = np.array([np.random.normal(mean, variance, dimension) for _ in range(n)])
    return data

def uniform(lb, ub, n, dimension) -> np.array:
    """
    Generates n data points from Uniform(lb,ub) distribution with given dimension
    Input:
        lb (float): lower bound of uniform distribution
        ub (float): upper bound of uniform distribution
        n (int): number of data points to generate
        dimension (int): dimension of the data points

    Return:
        data (np.array): generated data 
    """
    data = np.array([np.random.uniform(lb, ub, dimension) for _ in range(n)])
    return data

def poisson(lam, n, dimension) -> np.array:
    """
    Generates n data points from Poisson(lam) distribution with given dimension
    Input:
        lam (float): rate parameter of Poisson distribution
        n (int): number of data points to generate
        dimension (int): dimension of the data points

    Return:
        data (np.array): generated data 
    """
    data = np.array([np.random.poisson(lam, dimension) for _ in range(n)])
    return data

def cube():
    #TODO: find out what this means
    pass

def uniform_point_in_ball(d, lb, ub):
    """
    Generates a uniform point in d-dimensions in a ball with minimum length lb and maximum length ub

    Input:
        d (int): dimension of points
        lb (float): lower bound for length
        ub (float): ubber bound for length
    
    Return:
        point (np.array): data point
    """
    length = np.random.uniform(low=lb, high=ub)
    direction = np.random.uniform(low=-1, high=1, size=d)
    direction = direction/np.linalg.norm(direction)
    point = length*direction
    return point

def uniform_ball_with_ouliters(n, d, eta, c, r1, r2, sep=0) -> np.array:
    """
    Generates n many data points where eta*n many are uniformly inside a ball B1 with centre c and radius r1,
    and (1-eta)*n many are uniformly inside a ball B2 with centre c and radius r2 but not in B1

    Input:
        n (int): total number of data points to generate
        d (int): dimension of data points
        eta (float): percentage of data points to be inside B1
        c (np.array): centre of balls
        r1 (float): radius of inner ball
        sep (float): separation between inner ball and lower bound of outer ball
        r2 (float): radius of outer blal
    
    Return:
        data (np.array): generated data
    """
    if r1+sep > r2:
        raise ValueError("Value of r1+sep greater than r2")

    n_inner = int(np.floor(eta*n))
    n_outer = int(np.ceil((1-eta)*n))

    data_inner = [uniform_point_in_ball(d=d, lb=0, ub=r1) for _ in range(n_inner)]
    data_outer = [uniform_point_in_ball(d=d, lb=r1+sep, ub=r2) for _ in range(n_outer)]

    data = data_inner + data_outer
    np.random.shuffle(data)
    return np.array(data)

def two_clusters(n, d, eta, m1, v1, m2, v2) -> np.array:
    """
    Generates two clusters of normally distributed data with means and variances m1,m2, and v1,v2 respectively

    Input:
        n (int): total number of points to generate
        d (int): dimension of data
        eta (float): proportion of points to be in cluster 1 (with (1-eta)% in cluster 2)
        m1 (float): mean of normal distribution for cluster 1
        v1 (float): variance of normal distribution for cluster 1
        m1 (float): mean of normal distribution for cluster 2
        v1 (float): variance of normal distribution for cluster 2
    
    Return:
        data (np.array): generated data
    """
    k = int(np.floor(n*eta)) # number of points in cluster 1

    print(n, k, n-k)

    cluster1 = normal(m1, v1, k, d)
    cluster2 = normal(m2, v2, n-k, d)

    data = np.concatenate((cluster1, cluster2))

    return data