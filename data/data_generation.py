import numpy as np
import pandas as pd

def normal(mean, variance, n, dimension) -> np.array:
    data = np.array([np.random.normal(mean, variance, dimension) for _ in range(n)])
    return data

def uniform(lb, ub, n, dimension) -> np.array:
    data = np.array([np.random.uniform(lb, ub, dimension) for _ in range(n)])
    return data

def poisson(lam, n, dimension) -> np.array:
    data = np.array([np.random.poisson(lam, dimension) for _ in range(n)])
    return data

def to_csv(data, filename) -> None:
    df = pd.DataFrame(data)
    df.to_csv(r"{}.csv".format(filename))
    return None

data = normal(0,1,10,2)
to_csv(data, "C:\Users\holme\Documents\Programming\Python\Assignments\MSc Dissertation\Minimum-Enclosing-Balls-with-Outliers\data\_test")