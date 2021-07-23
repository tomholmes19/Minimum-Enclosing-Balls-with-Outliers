import numpy as np

import benchmarking.trials, benchmarking.utils
import data.loading
from meb import mebwo_algorithms

num_trials = 5

# data and M value pairs
data_types = {"uniform_ball": 2, "hyperspherical_shell": 4}

# func name and func pairs
func_names = {"relaxation_heuristic": mebwo_algorithms.alg__relaxation_heuristic}
for func_name in func_names:
    for data_type in data_types:
        if True:
            n = [1000 + 3000*i for i in range(10)]
            d = 30
            eta = 0.9

            if func_name == "relaxation_heuristic":
                M = data_types[data_type]
            else:
                M = None

            path = r"benchmarks/{0}/{1}/func_n_d{2}_eta{3}_{4}".format(func_name, data_type, d, benchmarking.utils.format_eta(eta), data_type)

            times = benchmarking.trials.run_trials_alg(
                func=func_names[func_name],
                n=n,
                d=d,
                eta=eta,
                num_trials=num_trials,
                data_type=data_type,
                log_file=r"{}.log".format(path),
                M=M
            )

            benchmarking.utils.plot_times(
                x_axis=n,
                times=times,
                xlabel="n",
                ylabel="Time",
                title="Runtime for Relaxation-Based Heuristic as a function of n, d={0}, eta={1}".format(d,eta),
                plot=False,
                filepath=r"{}.png".format(path)
            )

            benchmarking.utils.notify()