import numpy as np

import benchmarking.trials, benchmarking.utils
import data.loading
from meb import mebwo_algorithms

num_trials = 5

# data and M value pairs
data_types = {
    "uniform_ball": 2,
    "hyperspherical_shell": 4,
    "uniform_ball_with_outliers": 6,
    "normal": None,
    "mnist": None
}

# func name and func pairs
func_types = {
    "relaxation_heuristic": mebwo_algorithms.alg__relaxation_heuristic,
    "shrink": mebwo_algorithms.alg__shrink,
    "shenmaier": mebwo_algorithms.alg__shenmaier
}

experiment_types = {
    "n": True,
    "d": True,
    "eta": True
}

confirmed_funcs = benchmarking.utils.confirm_benchmark(func_types)
confirmed_data = benchmarking.utils.confirm_benchmark(data_types)
confirmed_experiments = benchmarking.utils.confirm_benchmark(experiment_types)

print(confirmed_funcs.keys())
print(confirmed_data.keys())
print(confirmed_experiments.keys())
msg = input("Running {} benchmarks. Continue? (y/n) ".format(len(confirmed_funcs)*len(confirmed_data)*len(confirmed_experiments)))

if msg == "y":
    for func_name in confirmed_funcs:
        for data_type in confirmed_data:
            if confirmed_experiments["n"]:
                n = [1000 + 3000*i for i in range(10) if 1000 + 3000*i > 13000]
                d = 30
                eta = 0.9

                if func_name == "relaxation_heuristic":
                    M = confirmed_data[data_type]
                else:
                    M = None

                path = r"benchmarks/{0}/{1}/func_n_d{2}_eta{3}_{4}".format(func_name, data_type, d, benchmarking.utils.format_eta(eta), data_type)

                times = benchmarking.trials.run_trials_alg(
                    func=confirmed_funcs[func_name],
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