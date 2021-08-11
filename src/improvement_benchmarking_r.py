import benchmarking.trials, benchmarking.utils
import data.loading
from meb import improvement_algorithms

import pandas as pd

num_trials = 5
num_iter = 100

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
    "dcmeb": improvement_algorithms.alg__dcmeb,
    "dcssh": improvement_algorithms.alg__dcssh
}

param_types = {
    "n": False,
    "d": False
}

confirmed_funcs = benchmarking.utils.confirm_benchmark(func_types)
confirmed_data = benchmarking.utils.confirm_benchmark(data_types)

for param in param_types:
        msg = input("Run benchmarks for {}? (y/n) ".format(param))
        if msg == "y":
            param_types[param] = True

confirmed_params = {param: param_types[param] for param in param_types if param_types[param] == True}
print(confirmed_funcs.keys())
print(confirmed_data.keys())
print(confirmed_params.keys())
msg = input("Running {} benchmarks. Continue? (y/n) ".format(len(confirmed_funcs)*len(confirmed_data)*len(confirmed_params)))

if msg == "y":
    for func_name in confirmed_funcs:
        for data_type in confirmed_data:
            if param_types["n"]:
                n = [500+500*i for i in range(2)]
                d = 100
                eta = 0.9

                path = r"benchmarks/{0}/{1}/avg_pct_func_n_d{2}_eta{3}_{4}".format(func_name, data_type, d, benchmarking.utils.format_eta(eta), data_type)

                df = benchmarking.trials.run_trials_improvement_r(func_name, n, d, num_trials, num_iter, data_type)

                df.to_csv(r"{}.csv".format(path), index=False)

                benchmarking.utils.plot_times(
                    x_axis=n,
                    times=df["avg%"],
                    xlabel="n",
                    ylabel="avg%",
                    title="",
                    plot=False,
                    filepath=r"{}.png".format(path)
                )
            
            if param_types["d"]:
                n = 1000
                d = [50+10*i for i in range(10)]
                eta = 0.9

                path = r"benchmarks/{0}/{1}/avg_pct_func_d_n{2}_eta{3}_{4}".format(func_name, data_type, n, benchmarking.utils.format_eta(eta), data_type)

                df = benchmarking.trials.run_trials_improvement_r(func_name, n, d, num_trials, num_iter, data_type)

                df.to_csv(r"{}.csv".format(path), index=False)

                benchmarking.utils.plot_times(
                    x_axis=d,
                    times=df["avg%"],
                    xlabel="d",
                    ylabel="avg%",
                    title="",
                    plot=False,
                    filepath=r"{}.png".format(path)
                )

