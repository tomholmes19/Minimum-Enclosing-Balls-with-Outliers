import pandas as pd
import matplotlib.pyplot as plt

import plot_settings

heuristics = ["dcmeb", "dcssh"]
data_types = ["hyperspherical_shell", "normal", "uniform_ball", "uniform_ball_with_outliers"]
params = ["n", "d"]

colours = {"dcmeb": "r", "dcssh": "b"}
markers = {"dcmeb": "o", "dcssh": "^"}

for data_type in data_types:
    for param in params:
        # load dataframes
        dfs = {heuristic: None for heuristic in heuristics}
        for heuristic in heuristics:
            # construct filename
            filename = "avg_pct_func_{}".format(param)
            if param == "n":
                filename += "_d100"
            else:
                filename += "_n1000"
            filename += "_eta0p9_{}".format(data_type)

            # load from csv
            dfs[heuristic] = pd.read_csv(r"benchmarks/{0}/{1}/{2}.csv".format(heuristic, data_type, filename))

        # get avg% lists
        pct_lists = {heuristic: df["avg%"] for heuristic, df in dfs.items()}

        plt.figure()
        plt.xlabel(param)
        plt.ylabel("avg%")
            
        if param == "n":
            x_axis = [500+500*i for i in range(10)]
        else:
            x_axis = [10+10*i for i in range(15)]
        
        for heuristic, pct_list in pct_lists.items():
            marker = markers[heuristic]
            colour = colours[heuristic]
            
            plt.plot(x_axis, pct_list, marker=marker, linestyle=":", color=colour, label=heuristic.upper())

        plt.legend()
        
        plt.savefig(r"images/improvement_r_benchmarks/{}".format(filename), bbox_inches="tight")

