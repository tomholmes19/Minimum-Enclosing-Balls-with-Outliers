import numpy as np
from pathlib import Path

import loading
import generation

def wrapper(data_type, func, **kwargs) -> None:
    """
    Generates data using func, saves to filepath, prints progress
    """
    filename = r"datasets/{}.csv".format(data_type)
    run = True

    if Path(filename).exists():
        msg = input("File {} already exists. Continue? (y/n)\n".format(filename))
        if msg == "n":
            run = False

    if run:
        print("Generating {}".format(data_type))
        data = func(**kwargs)
        print("Saving {}".format(data_type))
        loading.to_csv(data=data, filename=r"datasets/{}.csv".format(data_type))

    return None

n = 100000
d = 1000

np.random.seed(seed=1234)

wrapper(
    "normal",
    generation.normal,
    mean=0,
    variance=1,
    n=n,
    dimension=d
)

wrapper(
    "uniform",
    generation.uniform,
    lb=0,
    ub=1,
    n=n,
    dimension=d
)

wrapper(
    "poisson",
    generation.poisson,
    lam=1,
    n=n,
    dimension=d
)