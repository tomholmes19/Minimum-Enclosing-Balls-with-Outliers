import numpy as np
from pathlib import Path

import loading
import generation

def wrapper(data_type, func, num_trials=5, **kwargs) -> None:
    """
    Generates data using func, saves to filepath, prints progress
    """
    if data_type == "normal":
        filename = r"datasets/{}.csv".format(data_type)
    elif data_type == "uniform_ball_with_outliers":
        raise ValueError("Use other function for {}".format(data_type))
    else:
        n = kwargs["n"]
        d = kwargs["d"]
        filename = r"datasets/{0}/{1}_n{2}_d{3}".format(data_type, data_type, n, d)
    
    for i in range(num_trials):

        print("Generating {} {}".format(filename, i))
        data = func(**kwargs)
        print("Saving {} {}".format(filename, i))
        loading.to_csv(data=data, filename=r"{0}_{1}.csv".format(filename, i))

    return None





if False:
    np.random.seed(seed=1234)
    n = 100000
    d = 1000

    wrapper(
        "normal",
        generation.normal,
        num_trials=1,
        mean=0,
        variance=1,
        n=n,
        dimension=d
    )
#===================================================

n_list = [1000 + 3000*i for i in range(10)]
d_list = [10 + 10*i for i in range(10)]

if False:
    np.random.seed(1235)
    for n in n_list:
        d = 30
        wrapper(
            "uniform_ball",
            generation.uniform_ball,
            n=n,
            d=d,
            r=1,
            c=[0]*d
        )
    
    for d in d_list:
        n = 10000
        wrapper(
            "uniform_ball",
            generation.uniform_ball,
            n=n,
            d=d,
            r=1,
            c=[0]*d
        )

if False:
    np.random.seed(1236)
    for n in n_list:
        d = 30
        wrapper(
            "hyperspherical_shell",
            generation.hyperspherical_shell,
            n=n,
            d=d,
            r1=1,
            r2=2
        )
    
    for d in d_list:
        n = 10000
        wrapper(
            "hyperspherical_shell",
            generation.hyperspherical_shell,
            n=n,
            d=d,
            r1=1,
            r2=2
        )
