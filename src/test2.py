import data.loading, data.generation
from meb.ball import Ball, MEB, MEBwO
import numpy as np

import benchmarking.trials, benchmarking.utils

df = benchmarking.trials.run_trials_improvement_r("dcssh", [500, 1000], 100, 2, 10, "normal")
print(df)

benchmarking.utils.plot_times(
    x_axis=[500, 1000],
    times=df["avg%"],
    xlabel="n",
    ylabel="avg%",
    title="aaa",
    plot=True
)

df.to_csv(r"src/test.csv", index=False)