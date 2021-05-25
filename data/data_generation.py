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

    Out:
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

    Out:
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

    Out:
        data (np.array): generated data 
    """
    data = np.array([np.random.poisson(lam, dimension) for _ in range(n)])
    return data

def cube():
    #TODO: find out what this means
    pass