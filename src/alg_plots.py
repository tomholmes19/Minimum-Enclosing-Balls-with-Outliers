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

temp = {
    "n": [1000 + 3000*i for i in range(10)],
    "d": [10 + 10*i for i in range(10)],
    "eta": [0.5+0.1*i for i in range(5)]
}

axes = {
    "relaxation_heuristic": temp,
    "shenmaier": {
        "n": [1000 + 3000*i for i in range(8)],
        "d": temp["d"],
        "eta": temp["eta"]
    },
    "shrink": temp
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
            plt.plot(axes[heuristic][param], times, marker=markers[heuristic], color=colours[heuristic], linestyle=":", label=labels[heuristic])
        
        plt.legend()
        plt.show()
