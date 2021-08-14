"""
Constructs plots of construction algorithms benchmarks from logs
"""

import matplotlib.pyplot as plt

import plot_settings
import benchmarking.utils

heuristics = ["relaxation_heuristic", "shenmaier", "shrink"]
data_types = ["hyperspherical_shell", "normal", "uniform_ball", "uniform_ball_with_outliers"]
#data_types = ["hyperspherical_shell", "uniform_ball"]
params = ["n", "d", "eta"]

colours = {
    "relaxation_heuristic": "r",
    "shenmaier": "b",
    "shrink": "g"
}

markers = {
    "relaxation_heuristic": "o",
    "shenmaier": "^",
    "shrink": "D"
}

labels = {
    "relaxation_heuristic": "RBH",
    "shenmaier": "Shenmaier",
    "shrink": "Shrink"
}

axes = {
    "n": [1000 + 3000*i for i in range(10)],
    "d": [10 + 10*i for i in range(10)],
    "eta": [0.5+0.1*i for i in range(5)]
}

fixed_params = {
    "n": "d30",
    "d": "n10000",
    "eta": "n10000_d30"
}

for data_type in data_types:
    for param in params:
        # construct filename
        filename = "func_{0}_{1}".format(param, fixed_params[param])
        if param != "eta":
            filename += "_eta0p9"
        filename += "_{}".format(data_type)

        # get times from log
        times_dict = {heuristic: benchmarking.utils.get_times_from_log(r"benchmarks/{0}/{1}/{2}.log".format(heuristic, data_type, filename)) for heuristic in heuristics}
        
        plt.figure()
        plt.xlabel(param)
        plt.ylabel("Time (s)")

        for heuristic, times in times_dict.items():
            if heuristic == "shenmaier" and param == "n":
                x_axis = [1000 + 3000*i for i in range(8)]
            elif heuristic == "relaxation_heuristic" and data_type == "uniform_ball_with_outliers" and param == "d":
                x_axis = [10 + 10*i for i in range(8)]
            else:
                x_axis = axes[param]

            plt.plot(x_axis, times, marker=markers[heuristic], color=colours[heuristic], linestyle=":", label=labels[heuristic])
        
        if data_type == "normal" and param == "eta":
            plt.legend(loc="best", bbox_to_anchor=(0.5,0.,0.5,0.5))
        else:
            plt.legend()

        plt.savefig("images/alg_benchmarks/{}".format(filename), bbox_inches="tight")
